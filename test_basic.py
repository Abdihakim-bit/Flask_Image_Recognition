# tests_basic.py
from io import BytesIO

def test_prediction_route_exists(client):
    """
    Ensure the /prediction route exists and can handle a POST request (even without data).
    - Expected: Status code 200 and error message displayed.
    """
    response = client.post("/prediction", data={}, content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed" in response.data or b"error" in response.data.lower()


def test_upload_executable_file(client):
    """Uploading a non-image file like .exe should be rejected."""
    fake_exe = BytesIO(b"fake exe data")
    fake_exe.name = "malware.exe"
    response = client.post("/prediction", data={"file": (fake_exe, fake_exe.name)}, content_type="multipart/form-data")
    assert response.status_code == 400 or b"Invalid file type" in response.data
