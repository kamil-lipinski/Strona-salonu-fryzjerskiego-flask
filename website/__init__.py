from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    bootstrap.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import Opinion
    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        if not os.path.exists(os.path.join(basedir, 'database.sqlite')):
            db.create_all() # utworzenie bazy jeśli nie istnieje
            print('Created Database!')
            
            from .models import Price, Hairdresser # dodanie elementow do bazy
            new_price = Price(name='Włosy krótkie', price=140, type='damskie')
            db.session.add(new_price)

            new_price = Price(name='Włosy średnie', price=150, type='damskie')
            db.session.add(new_price)

            new_price = Price(name='Włosy długie', price=160, type='damskie')
            db.session.add(new_price)

            new_price = Price(name='Włosy krótkie', price=70, type='męskie')
            db.session.add(new_price)

            new_price = Price(name='Włosy długie', price=100, type='męskie')
            db.session.add(new_price)

            new_price = Price(name='Strzyżenie wąsów i brody', price=60, type='męskie')
            db.session.add(new_price)

            new_price = Price(name='Koloryzacja włosów', price=120, type='dodatkowe')
            db.session.add(new_price)

            new_price = Price(name='Trwała ondulacja włosów', price=200, type='dodatkowe')
            db.session.add(new_price)

            new_price = Price(name='Przedłużanie włosów', price=400, type='dodatkowe')
            db.session.add(new_price)
            
            new_hairdresser = Hairdresser(name='Joanna Kowalska',desc='Utalentowana fryzjerka z wieloletnim doświadczeniem i wyczuciem najnowszych trendów. Wnosi kreatywność i precyzję do każdej fryzury. Jej ekspertyza polega na tworzeniu personalizowanych stylizacji, które doskonale podkreślają indywidualność klientów, zapewniając im olśniewające i pewne siebie metamorfozy.')
            with open(os.path.join(basedir, 'static/images/fryzjer1.png'), 'rb') as file:
                new_hairdresser.picture = file.read()
            db.session.add(new_hairdresser)

            new_hairdresser = Hairdresser(name='Jan Kowalski',desc='Niezwykle doświadczony fryzjer o ogromnej pasji do swojego rzemiosła. Czerpie satysfakcję z dostarczania wyjątkowych strzyżeń i stylizacji, które przekraczają oczekiwania klientów. Dzięki metodycznemu podejściu i dbałości o detale, każdy klient opuszcza jego fotel odświeżony i zadowolony.') 
            with open(os.path.join(basedir, 'static/images/fryzjer2.png'), 'rb') as file:
                new_hairdresser.picture = file.read()
            db.session.add(new_hairdresser)

            new_hairdresser = Hairdresser(name='Anna Nowak',desc='Znana z innowacyjnych technik i wyjątkowej wiedzy o koloryzacji. Fryzjerka, która dodaje życia i intensywności każdemu klientowi. Z wyczuciem tworzy piękne pasemka, balayage i transformacje kolorystyczne, a jej artystyczne podejście i zaangażowanie w zadowolenie klientów czynią ją jedną z najlepszych w branży.') 
            with open(os.path.join(basedir, 'static/images/fryzjer3.jpg'), 'rb') as file:
                new_hairdresser.picture = file.read()
            db.session.add(new_hairdresser)

            new_hairdresser = Hairdresser(name='Adam Polański',desc='Fryzjer o wyjątkowym zmyśle artystycznym. Jego kreatywność i wyczucie stylu sprawiają, że każda fryzura staje się prawdziwym dziełem sztuki. Z pasją podchodzi do pracy, dbając o najmniejsze detale i indywidualne potrzeby klientów. Jest ekspertem w tworzeniu modnych i nowoczesnych fryzur.') 
            with open(os.path.join(basedir, 'static/images/fryzjer4.jpg'), 'rb') as file:
                new_hairdresser.picture = file.read()
            db.session.add(new_hairdresser)

            db.session.commit()

