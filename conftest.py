import pytest
from tests.utils.sender_stand_requests import request_otp, confirm_otp
from tests.utils.data import TEST_PHONE, OTP_CODE

@pytest.fixture(scope="session")
def access_token():

    request_otp(TEST_PHONE)
    response = confirm_otp(TEST_PHONE, OTP_CODE)
    token = response.json().get("accessToken")
    assert token is not None
    return token