import pytest
from Projet_11_OpenClassrooms.server import create_app
from Projet_11_OpenClassrooms.models.club import Club_model
from Projet_11_OpenClassrooms.models.competitions import Competitions_model
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
def client(mocker):
    clubs = [Club_model("Cinho-Club", "cinhoclub@gmail.com", "15"),
             Club_model("Raf-Club", "rafclub@gmail.com", "10"),
             Club_model("Francoise-Club", "Francoiseclub@gmail.com", "5")
             ]
    competitions =[
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
    assert "Welcome to the GUDLFT Registration Portal" in data


def test_show_summary(client, mocker):
    club_1 = Club_model("Cinho-Club", "cinhoclub@gmail.com", "15")
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_email', return_value=club_1)
    # if email is ok
    response_1 = client.post("/showSummary", data={"email": club_1.email})
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
    club_1 = Club_model("Cinho-Club", "cinhoclub@gmail.com", "15")
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_1)
    competition_1 = Competitions_model("first competitions", "2022-09-26 00:19:00", "15")
    mocker.patch('Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name', return_value=competition_1)
    competition_nbr_of_places = competition_1.numberOfPlaces
    response = client.get("/book/{}/{}".format(competition_1.name, club_1.name))
    data = response.data.decode()
    assert response.status_code == 200
    assert "Places available: {}".format(competition_nbr_of_places) in data

    # if competition and club not founded
    club_2 = None
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_2)
    competition_2 = None
    mocker.patch('Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name', return_value=competition_2)
    response = client.get("/book/competitionsnotok/Club not exist")
    assert response.status_code == 404

    # if club not founded
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_2)
    mocker.patch('Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name', return_value=competition_1)
    response = client.get("/book/{}/Club not exist".format(competition_1.name))
    assert response.status_code == 404

    # if competition  not founded
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_1)
    mocker.patch('Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition_by_name', return_value=competition_2)
    response = client.get("/book/{}/Cinho-Club".format(club_1.name))
    assert response.status_code == 404


def test_purchase_places(client, mocker):
    club_1 = Club_model("Cinho-Club", "cinhoclub@gmail.com", "15")
    mocker.patch('Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs_by_name', return_value=club_1)
    competition_1 = Competitions_model("first competitions", "2022-09-26 00:19:00", "30")
    mocker.patch('Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition', return_value=competition_1)
    response = client.post(
        "/purchasePlaces",
        data={
            'competition': 'competitions_name',
            'club': 'club_name',
            "places": 4
        }
    )
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome, {}".format(club_1.email) in data
    assert str.encode(f"Points available: {club_1.points}") in response.data
    assert str.encode(f"Number of Places: {competition_1.numberOfPlaces}") in response.data


def test_logout(client):
    response = client.get("/logout", follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal" in data
