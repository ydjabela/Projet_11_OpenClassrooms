import pytest
from ... import server
from ... server import create_app
clubs = [
    {
        "name": "Cinho-Club",
        "email": "cinhoclub@gmail.com",
        "points": "15"
    },
    {
        "name": "She Lifts",
         "email": "kate@shelifts.co.uk",
         "points": "12"
    },
    {
        "name": "",
        "email": '',
        "points": ""
    }
]
competitions = [
    {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    },
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
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal" in data


def test_show_summary(client):
    # if email is ok
    response = client.post("/showSummary", data={"email": clubs[1]["email"]})
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome, {}".format(clubs[1]["email"]) in data

    # if email is not ok
    response = client.post("/showSummary", data={"email": clubs[0]["email"]})
    assert response.status_code == 500

    # if email is not exist
    response = client.post("/showSummary", data={"email": clubs[2]["email"]})
    assert response.status_code == 500


def test_book(client):
    # if competition and club  founded
    competition_name = competitions[0]['name']
    competition_nbr_of_places = competitions[0]['numberOfPlaces']
    clubs_name = clubs[1]['name']
    response = client.get("/book/{}/{}".format(competition_name, clubs_name))
    data = response.data.decode()
    assert response.status_code == 200
    assert "Places available: {}".format(competition_nbr_of_places) in data

    # if competition and club not founded
    competition_name = competitions[1]['name']
    clubs_name = clubs[0]['name']
    response = client.get("/book/{}/{}".format(competition_name, clubs_name))
    assert response.status_code == 500

    # if club not founded
    competition_name = competitions[0]['name']
    clubs_name = clubs[0]['name']
    response = client.get("/book/{}/{}".format(competition_name, clubs_name))
    assert response.status_code == 500

    # if competition  not founded
    competition_name = competitions[1]['name']
    clubs_name = clubs[1]['name']
    response = client.get("/book/{}/{}".format(competition_name, clubs_name))
    assert response.status_code == 500


def test_purchase_places(client):
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": competitions[0]['name'],
            "club": clubs[1]['name'],
            "places": 13
        }
    )
    current_points = int(clubs[1]['points'])
    current_places = int(competitions[0]['numberOfPlaces'])
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome, {}".format(clubs[1]["email"]) in data
    assert str.encode(f"Points available: {current_points}") in response.data
    assert str.encode(f"Number of Places: {current_places}") in response.data


def test_logout(client):
    response = client.get("/logout", follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal" in data



