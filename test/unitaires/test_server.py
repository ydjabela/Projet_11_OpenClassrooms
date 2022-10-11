import pytest
from Projet_11_OpenClassrooms.server import create_app
from Projet_11_OpenClassrooms.models.club import Club_model
from Projet_11_OpenClassrooms.models.competitions import Competitions_model

@pytest.fixture
def client(mocker):
    clubs = [Club_model("Cinho-Club", "cinhoclub@gmail.com", "15"),
             Club_model("Raf-Club", "rafclub@gmail.com", "10"),
             Club_model("Francoise-Club", "Francoiseclub@gmail.com", "5")
             ]
    competitions = [
        Competitions_model("first competitions", "2022-09-26 00:19:00", "15"),
        Competitions_model("second competitions", "2022-09-28 00:19:00", "20"),
        Competitions_model("third competitions", "2022-09-30 00:19:00", "5")
    ]
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs',
        return_value=clubs
    )
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition',
        return_value=competitions
    )
    app = create_app()
    with app.test_client() as client:
        yield client


def test_should_status_code_ok(client):
    response = client.get('/')
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in data


def test_show_summary(client, mocker):
    club_1 = {"name": "Cinho-Club", "email": "cinhoclub@gmail.com", "points": "15"}
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_email', return_value=club_1)
    # if email is ok
    response_1 = client.post("/showSummary", data={"email": club_1['email']})
    data_1 = response_1.data.decode()
    assert response_1.status_code == 200
    assert data_1.find("<title>GUDLFT Registration</title>") == -1
    assert "Welcome, cinhoclub@gmail.com" in data_1

    # if email is not ok
    club_2 = None
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_email', return_value=club_2)
    response_2 = client.post("/showSummary", data={"email": "email_not_ok@test@com"})
    data_2 = response_2.data.decode()
    assert response_2.status_code == 404
    assert data_2.find("<title>GUDLFT Registration</title>") != -1

    # if email is not exist
    club_3 = None
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_email', return_value=club_3)
    response_3 = client.post("/showSummary", data={"email": ""})
    assert response_3.status_code == 404


def test_book(client, mocker):
    # if competition and club  founded
    club_1 = {"name": "Cinho-Club", "email": "cinhoclub@gmail.com", "points": "15"}
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_1)
    competition_1 = {"name": "first competitions", "date": "2022-09-26 00:19:00", "numberOfPlaces": "25"}
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name',
        return_value=competition_1
    )
    competition_nbr_of_places = competition_1['numberOfPlaces']
    response = client.get("/book/{}/{}".format(competition_1['name'], club_1['name']))
    data = response.data.decode()
    assert response.status_code == 200
    assert "Places available: {}".format(competition_nbr_of_places) in data

    # if competition and club not founded
    club_2 = None
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_2)
    competition_2 = None
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name',
        return_value=competition_2
    )
    response = client.get("/book/competitionsnotok/Club not exist")
    assert response.status_code == 404

    # if club not founded
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name',
        return_value=club_2
    )
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name',
        return_value=competition_1
    )
    response = client.get("/book/{}/Club not exist".format(competition_1['name']))
    assert response.status_code == 404

    # if competition  not founded
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_1)
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name',
        return_value=competition_2
    )
    response = client.get("/book/{}/Cinho-Club".format(club_1['name']))
    assert response.status_code == 404


def test_purchase_places_nok(client, mocker):
    for places in [-2, 0, 4, 6, 13, 26]:
        club_1 = {"name": "Cinho-Club", "email": "cinhoclub@gmail.com", "points": "15"}
        mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_1)
        competition_1 = {"name": "first competitions", "date": "2022-09-26 00:19:00", "numberOfPlaces": "25"}
        mocker.patch('Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name',
                     return_value=competition_1)
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
                assert club_1['points'] == str(15 - 3*places)
                assert competition_1["numberOfPlaces"] == str(25 - places)
            else:
                assert data_1.find('Not enough points') != -1


def test_logout(client):
    response = client.get("/logout", follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal" in data
