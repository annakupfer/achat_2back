import websocket
import ssl
import json
from tests.utils.configuration import get_ws_url
import tests.utils.data as data
from tests.utils.utils import assert_structure  

def test_add_contact(access_token):
    
    # Получаем url с токеном
    ws_url = get_ws_url(access_token)
    ws = websocket.create_connection(ws_url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.settimeout(5)

    try:

        # Получаем стартовое сообщение от сервера
        response_raw = ws.recv()
        response_data = json.loads(response_raw)
        assert response_data.get("type") == "chat_list"

        # Отправляем запрос на добавление контакта

        payload = data.WS_ADD_CONTACT_PAYLOAD
        ws.send(json.dumps(payload))

        # Получаем ответ и проверяем

        response_raw = ws.recv()
        response_data = json.loads(response_raw)
        assert response_data.get("type") == "contact_action"

        # Проверка структуры ответа

        assert_structure(data.EXPECTED_CONFIRMATION_ADD_CONTACT, response_data)
    
    finally:
        ws.close()