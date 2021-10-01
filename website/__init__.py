from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config['SECRET_KEY'] = 'ian'
    # To not show notifications every time main.py gets executed
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    create_db(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(int(id))

    return app


def create_db(app):
    if not path.exists('/website/' + DB_NAME):
        db.create_all(app=app)
