import pytest
from pathlib import Path
import requests

import tests.utils.configuration as configuration


def test_file_image_upload(access_token):
    filename = "test_image.jpg"
    current_dir = Path(__file__).parent
    file_path = current_dir / "assets" / filename

    url = configuration.BASE_URL + configuration.FILE_UPLOAD_PATH

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    with open(file_path, "rb") as f:
        files = {
            "file": (filename, f, "image/jpeg")
        }
        data = {
            "scale": "1.0",
            "positionX": "0.0",
            "positionY": "0.0"
        }

        response = requests.post(url, headers=headers, files=files, data=data)

    assert response.status_code == 200
    json_data = response.json()
    assert "url" in json_data
    assert json_data["filename"] == filename
