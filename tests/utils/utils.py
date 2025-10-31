## В этом модуле вспомогательные функцмм, не завязанные на конкретные данные

import json 
import time

# Функция проверки структуры сообщения
def assert_structure(expected, actual, path="root"):
    assert isinstance(actual, dict), f"{path}: expected dict, got {type(actual).__name__}"

    for key, expected_value in expected.items():
        assert key in actual, f"{path}: missing key '{key}'"
        actual_value = actual[key]

        if expected_value is None:
            # Поле может быть любого типа или None
            continue

        if isinstance(expected_value, dict):
            if actual_value is None:
                continue  # допускаем None, если в expected dict
            assert isinstance(actual_value, dict), f"{path}.{key}: expected dict"
            assert_structure(expected_value, actual_value, path=f"{path}.{key}")

        elif isinstance(expected_value, list):
            assert isinstance(actual_value, list), f"{path}.{key}: expected list"
            if expected_value:
                # Если ожидаемый элемент — dict, делаем рекурсию
                if isinstance(expected_value[0], dict):
                    for i, item in enumerate(actual_value):
                        assert_structure(expected_value[0], item, path=f"{path}.{key}[{i}]")
                else:
                    # Иначе просто проверяем тип каждого элемента
                    expected_type = type(expected_value[0])
                    for i, item in enumerate(actual_value):
                        assert isinstance(item, expected_type), (
                            f"{path}.{key}[{i}]: expected {expected_type.__name__}, got {type(item).__name__}"
                        )

        else:
            if actual_value is not None:
                assert isinstance(actual_value, type(expected_value)), (
                    f"{path}.{key}: expected {type(expected_value).__name__}, got {type(actual_value).__name__}"
                )

# Функция проверки того, что пользователь находится во всех выданных чатах

def assert_user_in_all_chats(response_data, user_id):
    print("Функция вызвалась")  # отладка
    chats = response_data.get("chats", [])
    missing_in = []

    for chat in chats:
        participant_ids = chat.get("participantId", [])
        if user_id not in participant_ids:
            missing_in.append(chat.get("id"))

    if missing_in:
        print(f"[WARN] Пользователь {user_id} не найден в участниках чатов: {missing_in}")
    else:
        print(f"[INFO] Пользователь {user_id} найден во всех {len(chats)} чатах.")

# Функция ожидания сообщения конкретного типа 


def wait_for_types_multiple(ws, expected_counts, timeout=10):
    """
    Ждём несколько сообщений разных типов.

    :param ws: WebSocket соединение
    :param expected_counts: dict, ключ — тип сообщения, значение — сколько таких ждать
    :param timeout: таймаут
    :return: dict с типами, где значение — список сообщений данного типа
    """
    start = time.time()
    found = {msg_type: [] for msg_type in expected_counts}

    while any(len(found[msg_type]) < count for msg_type, count in expected_counts.items()):
        if time.time() - start > timeout:
            missing = {t: c - len(found[t]) for t, c in expected_counts.items() if len(found[t]) < c}
            raise AssertionError(f"Не получили сообщения: {missing}")

        raw = ws.recv()
        msg = json.loads(raw)
        msg_type = msg.get("type")

        if msg_type in found and len(found[msg_type]) < expected_counts[msg_type]:
            found[msg_type].append(msg)

    return found



# Функция отправки сообщения в группу

def send_message_to_group(ws, chat_id, message_text="", attachments=None):
    """
    Отправляет сообщение через WebSocket.

    :param ws: WebSocket-соединение
    :param chat_id: ID чата
    :param message_text: Текст сообщения
    :param attachments: Список вложений (списки словарей с id и типом)
    :param message_type: Тип сообщения (по умолчанию TEXT)
    :param parent_id: ID родительского сообщения (если это ответ)
    """
    payload = {
        "action": "send_message",
        "chat_id": chat_id,
        "message": message_text,
        "documents": attachments or []
    }
    ws.send(json.dumps(payload))

    responses = wait_for_types_multiple(ws,{"confirmation":1,"chat_message":1})
    return responses["chat_message"][0]  

# Функция отправки сообщения пользователю                            

def send_message_to_user(ws, participant_id, message_text="", attachments=None):
    payload = {
        "action": "send_message",
        "participant_id": participant_id,
        "message": message_text,
        "documents": attachments or []
    }
    ws.send(json.dumps(payload))

    responses = wait_for_types_multiple(ws, {"confirmation": 1, "chat_message": 1})
    return responses["chat_message"][0]
