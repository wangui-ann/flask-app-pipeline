from app import app

def test_root():
    response = app.test_client().get('/')
    assert response.status_code == 200
