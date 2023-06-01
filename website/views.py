from flask import Blueprint, render_template, session, redirect, url_for, flash
from .forms import OpinionForm
from .models import db, Opinion, Price, Hairdresser
import base64

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', current_page='home')

@views.route('/zespol', methods=['GET'])
def team():
    hairdresser_list = Hairdresser.query.all()  # zapytanie do bazy pobierające wszystkie obiekty klasy Hairdresser
    for hairdresser in hairdresser_list:  # dekodowanie obrazów zapisanych jako LargeBinary na utf8
        if hairdresser.picture:
            hairdresser.picture = base64.b64encode(hairdresser.picture).decode('utf-8')
    return render_template('team.html', current_page='zespol', hairdresser_list=hairdresser_list)

@views.route('/cennik', methods=['GET'])
def prices():
    price_list = Price.query.all()  # zapytanie do bazy pobierające wszystkie obiekty klasy Price
    return render_template('prices.html', current_page='cennik', price_list=price_list)

@views.route('/opinie', methods=['GET', 'POST'])
def opinions():
    form = OpinionForm()

    if form.validate_on_submit():
        session['name'] = form.name.data  # przechowywanie w session storage aby rozwiązać problem odświeżania
        session['rating'] = form.rating.data
        session['opinion'] = form.opinion.data

        new_opinion = Opinion(name=session['name'], rating=session['rating'], opinion=session['opinion'])
        db.session.add(new_opinion)
        db.session.commit()  # stworzenie nowego obiektu klasy Opinion i dodanie do bazy

        session.pop('name', None)
        session.pop('rating', None)
        session.pop('opinion', None)

        flash('Dodano nową opinię!')

        return redirect(url_for('views.opinions'))

    opinion_list = Opinion.query.order_by(Opinion.date.desc()).all()   # zapytanie do bazy pobierające wszystkie obiekty
                                                                       # klasy Opinion posortowane po dacie malejąco

    return render_template('opinions.html', current_page='opinie', form=form, opinion_list=opinion_list)