import websocket
import ssl
import json
import pytest
from tests.utils.configuration import get_ws_url
import tests.utils.data as data

from tests.utils.utils import assert_structure

@pytest.mark.skip(reason="Сервер не отвечает на start_call — временно отключено до фикса")

def test_call_initiation(access_token):

    # Получаем url с токеном
    ws_url = get_ws_url(access_token)
    ws = websocket.create_connection(ws_url, sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.settimeout(5)
    try:
        # При подключении автоматически приходит chat_list
        response_raw = ws.recv()
        response_data = json.loads(response_raw)
        assert response_data.get("type") == "chat_list"  # автоматическая проверка

        # Инициируем звонок

        payload = data.WS_CALL_INITIATION_PAYLOAD
        ws.send(json.dumps(payload))

        # Получаем ответ

        response_raw = ws.recv()
        response_call_started = json.loads(response_raw)
        assert response_call_started.get("type") == "call_started"
        assert response_call_started.get("user_phone") == data.TEST_PHONE
        assert response_call_started.get("callee_phone") == data.WS_CALL_INITIATION_PAYLOAD["callee_phone"]

        # Проверяем структуру confirmation
        assert_structure(data.EXPECTED_CALL_STARTED_RESPONSE, response_call_started)
    
    finally:
        ws.close()


