# tests_basic.py

def test_homepage_accessible(client):
    """Ensure the homepage (index.html) loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data.lower()

def test_prediction_route_exists(client):
    """
    Ensure the /prediction route exists and can handle a POST request (even without data).
    - Expected: Status code 200 and error message displayed.
    """
    response = client.post("/prediction", data={}, content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed" in response.data and b"File cannot be processed" in response.data


