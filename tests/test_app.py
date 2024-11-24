def test_home_page():
    from app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to DevOps Demo" in response.data