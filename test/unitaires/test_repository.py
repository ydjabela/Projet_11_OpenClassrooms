from ...repository.loadcompetitions import Competitions
from ...repository.loadclub import Club


def test_load_competition_by_name(mocker):
    competition_1 = [
        {"name": "first competitions", "date": "2022-09-26 00:19:00", "numberOfPlaces": "25"},
        {"name": "second competitions", "email": "2022-09-28 00:19:00", "points": "20"},
                     ]
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition',
        return_value=competition_1
    )
    assert Competitions().load_competition_by_name(competition_name=competition_1[0]['name'])
    competition_2 = None
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadcompetitions.Competitions.load_competition',
        return_value=competition_2
    )
    assert Competitions().load_competition_by_name(competition_name="competionnotok") is None


def test_load_clubs_by_name(mocker):
    clubs_1 = [
        {"name": "first competitions", "email": "2022-09-26 00:19:00", "points": "25"},
        {"name": "Raf-Club", "email": "rafclub@gmail.com", "points": "10"},
     ]
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs',
        return_value=clubs_1
    )
    assert Club().load_clubs_by_name(club_name=clubs_1[0]['name'])
    clubs_2 = None
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs',
        return_value=clubs_2
    )
    assert Club().load_clubs_by_name(club_name="clubnamenotok") is None


def test_load_clubs_by_email(mocker):
    clubs_1 = [
        {"name": "first competitions", "email": "2022-09-26 00:19:00", "points": "25"},
        {"name": "Raf-Club", "email": "rafclub@gmail.com", "points": "10"},
     ]
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs',
        return_value=clubs_1
    )
    assert Club().load_clubs_by_email(club_email=clubs_1[0]['email'])
    clubs_2 = None
    mocker.patch(
        'Projet_11_OpenClassrooms.repository.loadclub.Club.load_clubs',
        return_value=clubs_2
    )
    assert Club().load_clubs_by_email(club_email="clubnamenotok") is None
