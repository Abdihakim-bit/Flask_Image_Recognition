# test_advanced.py

from io import BytesIO
import numpy as np
from model import preprocess_img, predict_result

def test_upload_executable_file(client):
    """
    Upload an executable file to predictions.
    Expected: File cannot be processe error in response or 400."""
    fake_exe = BytesIO(b"fake exe data")
    fake_exe.name = "malware.exe"
    response = client.post("/prediction", data={"file": (fake_exe, fake_exe.name)}, content_type="multipart/form-data")
    assert response.status_code == 400 or b"File cannot be processed" in response.data


def test_prediction_output_type():
    """
    Ensure the model prediction output is an integer class label.
    Expected: Output of predict_result() should be int or numpy integer type.
    """
    test_img = "test_images/1/Sign 1 (8).jpeg"
    processed = preprocess_img(test_img)
    prediction = predict_result(processed)

    assert isinstance(prediction, (int, np.integer)), "Prediction must be an integer label."