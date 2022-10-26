import pytest
from ...server import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_server(client):
    club_1 = {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}
    competition_1 = {"name": "Spring Festival", "date": "2023-03-27 10:00:00", "numberOfPlaces": "25"}

    response = client.get('/')
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in data

    # if email is ok
    response_1 = client.post("/showSummary", data={"email": club_1['email']})
    data_1 = response_1.data.decode()
    assert response_1.status_code == 200
    assert data_1.find("<title>GUDLFT Registration</title>") == -1
    assert "Welcome, john@simplylift.co" in data_1

    # if competition and club  founded
    competition_nbr_of_places = competition_1['numberOfPlaces']
    response = client.get("/book/{}/{}".format(competition_1['name'], club_1['name']))
    data = response.data.decode()
    assert response.status_code == 200
    assert "Places available: {}".format(competition_nbr_of_places) in data

    for places in [-2, 0, 4, 6, 13, 26]:
        response = client.post(
            '/purchasePlaces',
            data={
                'competition': competition_1['name'],
                'club': club_1['name'],
                'places': places
            }
        )
        data_1 = response.data.decode()
        assert response.status_code == 200
        assert "Welcome, {}".format(club_1['email']) in data_1
        assert data_1.find("<title>Summary | GUDLFT Registration</title>") != -1
        if places <= 0:
            assert data_1.find('the  number  of  places need to be not negative') != -1
        elif places > 12:
            assert data_1.find('the  number  of  places need to be under to 12') != -1
        elif places > 25:
            assert data_1.find('Not enough places') != -1
        else:
            # if number of  places > int(club_1['points'])/3 = 5
            if places <= 5:
                club_1['points'] = '1'
                competition_1["numberOfPlaces"] = '21'
                assert club_1['points'] == str(13 - 3*places)
                assert competition_1["numberOfPlaces"] == str(25 - places)
            else:
                assert data_1.find('Not enough points') != -1


def test_clubs_display(client):
    response_1 = client.get("/clubs")
    data_1 = response_1.data.decode()
    assert response_1.status_code == 200
    assert data_1.find("<title>GUDLFT Registration</title>") == -1
    assert "Liste des clubs:" in data_1


def test_logout(client):
    response = client.get("/logout", follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal" in data
