import websocket
import ssl
import json

from tests.utils.configuration import get_ws_url


from urllib.parse import quote
from tests.utils.utils import assert_structure 
from tests.utils.sender_stand_requests import get_user_id_by_token 

from tests.utils.data import EXPECTED_MESSAGE_STRUCTURE, WS_GET_MESSAGES_TEMPLATE

def test_get_messages(access_token):
    user_id = get_user_id_by_token(access_token)
    ws = websocket.create_connection(get_ws_url(access_token), sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.settimeout(5)

    try:
        # Получаем автоматический chat_list
        chat_list_raw = ws.recv()
        chat_list = json.loads(chat_list_raw)
        assert chat_list.get("type") == "chat_list"
        chats = chat_list.get("chats", [])
        assert chats, "Список чатов пуст"

        chat_id = chats[0]["id"]

        # Отправляем запрос на сообщения
        get_messages_payload = WS_GET_MESSAGES_TEMPLATE.copy()
        get_messages_payload["chat_id"] = chat_id
        ws.send(json.dumps(get_messages_payload))

        messages_raw = ws.recv()
        messages_response = json.loads(messages_raw)

        assert messages_response["type"] == "search_results"
        assert "messagesList" in messages_response
        assert isinstance(messages_response["messagesList"], list)
        assert len(messages_response["messagesList"]) > 0, "Список сообщений пуст"

        # Проверка структуры сообщений
        for i, group in enumerate(messages_response["messagesList"]):
            messages = group.get("messagesInDate", [])
        for j, msg in enumerate(messages):
            assert_structure(EXPECTED_MESSAGE_STRUCTURE, msg, path=f"messagesList[{i}].messagesInDate[{j}]")

    finally:
        ws.close()
