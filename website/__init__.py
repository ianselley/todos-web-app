from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user

db = SQLAlchemy()
DB_NAME = "database.db"


def page_not_found(e):
    return render_template("404.html", user=current_user), 404


def create_app():
    from random import choice
    from string import printable
    app = Flask(__name__)
    app.static_folder = "static"
    app.config["SECRET_KEY"] = ''.join(choice(printable) for _ in range(20))
    app.register_error_handler(404, page_not_found)
    # To not show notifications every time main.py gets executed
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.sign_up"
    login_link = '<a href="/login" class="alert-link">log in</a>'
    login_manager.login_message = f"Please, sign up before you enter the page, or {login_link} if you already have an account"
    login_manager.login_message_category = "error"

    from .views import views
    from .auth import auth
    from .my_notes import my_notes
    from .my_categories import my_categories

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(my_notes, url_prefix="/")
    app.register_blueprint(my_categories, url_prefix="/")

    from .models import User

    create_db(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(int(id))

    return app


def create_db(app):
    if not path.exists("/website/" + DB_NAME):
        db.create_all(app=app)


app = create_app()
