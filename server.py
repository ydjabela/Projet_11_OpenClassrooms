from flask import Flask, render_template, request, redirect, flash, url_for
from .repository.loadcompetitions import Competitions
from .repository.loadclub import Club


def create_app():
    app = Flask(__name__)
    app.secret_key = 'something_special'

    competitions = Competitions().load_competition()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary', methods=['POST'])
    def showSummary():
        club = Club().load_clubs_by_email(club_email=request.form['email'])
        if club is not None:
            return render_template('welcome.html', club=club, competitions=competitions)
        else:
            return render_template("index.html"), 404

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        foundClub = Club().load_clubs_by_name(club_name=club)
        foundCompetition = Competitions().load_competition_by_name(competition_name=competition)
        if foundClub and foundCompetition:
            return render_template('booking.html', club=foundClub, competition=foundCompetition)
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions)

    @app.route('/purchasePlaces', methods=['POST'])
    def purchasePlaces():
        competition = Competitions().load_competition_by_name(competition_name=request.form['competition'])
        club = Club().load_clubs_by_name(club_name=request.form['club'])
        placesRequired = int(request.form['places'])
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)

    # TODO: Add route for points display

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app
