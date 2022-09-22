import pytest

from unitaires.test_server import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_should_status_code_ok(client):
    response = client.get('/')
    assert response.status_code ==200


def test_should_return_hello_world(client):
    response = client.get('/')
    data = response.data.decode()  # Permet de décoder la data dans la requête
    assert data == 'Hello, World! yacine'

