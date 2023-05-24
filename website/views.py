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
    hairdresser_list = Hairdresser.query.all()
    for hairdresser in hairdresser_list: # konwersja LargeBinary na obraz
        if hairdresser.picture:
            hairdresser.picture = base64.b64encode(hairdresser.picture).decode('utf-8')
    return render_template('team.html', current_page='zespol', hairdresser_list=hairdresser_list)

@views.route('/cennik', methods=['GET'])
def prices():
    price_list = Price.query.all()
    return render_template('prices.html', current_page='cennik', price_list=price_list)

@views.route('/opinie', methods=['GET', 'POST'])
def opinions():
    form = OpinionForm()
    opinion_list = []

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['rating'] = form.rating.data
        session['opinion'] = form.opinion.data

        new_opinion = Opinion(name=session['name'], rating=session['rating'], opinion=session['opinion'])
        db.session.add(new_opinion)
        db.session.commit()

        session.pop('name', None)
        session.pop('rating', None)
        session.pop('opinion', None)

        flash('Dodano nową opinię!')

        return redirect(url_for('views.opinions')) # przechowywane w session storage 
                                                   # aby rozwiązać problem odśwież

    opinion_list = Opinion.query.order_by(Opinion.id.desc()).all()

    return render_template('opinions.html', current_page='opinie', form=form, opinion_list=opinion_list)