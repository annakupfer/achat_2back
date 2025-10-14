import websocket
import ssl
import json
import tests.utils.configuration as configuration
from tests.utils.configuration import get_ws_url
import tests.utils.data as data
from tests.utils.sender_stand_requests import request_otp, confirm_otp
from urllib.parse import quote
from tests.utils.utils import assert_structure  
from tests.utils.data import EXPECTED_CONFIRMATION

def test_create_group(access_token):
    ws_url = get_ws_url(access_token)
    ws = websocket.create_connection(ws_url, sslopt={"cert_reqs": ssl.CERT_NONE})

    try: 
        # Получаем список чатов
        response_raw = ws.recv()
        response_data = json.loads(response_raw)
        assert response_data.get("type") == "chat_list" 
        
        # Отправляем сообщение на создание группы
        payload = data.WS_CREATE_GROUP_PAYLOAD
        ws.send(json.dumps(payload))

    # Получаем подтверждение создания группы (confirmation)
        response_raw = ws.recv()
        response_data = json.loads(response_raw)
        assert response_data.get("type") == "confirmation"

    # Проверяем структуру confirmation
        assert_structure(EXPECTED_CONFIRMATION, response_data)

    finally:
        ws.close()
