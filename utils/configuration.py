from urllib.parse import urljoin, quote

BASE_URL = "https://api.jv.test.messenger.akatosphere.ru/"
BASE_WS_URL = "wss://api.jv.test.messenger.akatosphere.ru/"
FILE_UPLOAD_PATH = "api/v1/file/upload"
USER_GET_DATA_PATH = "api/v1/user/getData"
GET_OTP_CODE_PATH = "api/v1/auth/getOTPCode"
SIGN_IN_PATH = "api/v1/auth/signIn"
USER_GET_DATA_PATH = "api/v1/user/getData"
SEND_MESSAGE_PATH = "api/v1/ws/chat"

def get_ws_url(access_token: str) -> str:
    if not access_token:
        # Если токена нет, возвращаем URL без токена или с пустым параметром
        return BASE_WS_URL
    token_encoded = quote(access_token)
    ws_base_path = urljoin(BASE_WS_URL, SEND_MESSAGE_PATH)
    return f"{ws_base_path}?Authorization=Bearer%20{token_encoded}"