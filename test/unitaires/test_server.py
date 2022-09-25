import pytest

from ... server import create_app
clubs = [
    {
        "name": "Cinho-Club",
        "email": "cinhoclub@gmail.com",
        "points": "15"
    },
    {
        "name": "OPC-Club",
        "email": 'admin@irontemple.com',
        "points": "16"
    },
    {
        "name": "",
        "email": '',
        "points": ""
    }
]
competitions = [
    {
        "name": "MLB World Series",
        "date": "2022-09-26 00:19:00",
        "numberOfPlaces": "20"
    },
    {
        "name": "Devon Fall Classic",
        "date": "2022-10-26 00:19:00",
        "numberOfPlaces": "22"
    }
]

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_should_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_showSummary(client):
    # if email is ok
    response = client.post("/showSummary", data={"email": clubs[1]["email"]})
    assert response.status_code == 200

    # if email is not ok
    response = client.post("/showSummary", data={"email": clubs[0]["email"]})
    assert response.status_code == 500


# if email is not exist
    response = client.post("/showSummary", data={"email": clubs[2]["email"]})
    assert response.status_code == 500



