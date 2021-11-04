from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


views = Blueprint("views", __name__)


@views.route("/")
def redirect_to():
    if current_user.is_authenticated:
        return redirect(url_for("my_categories.get"))
    return redirect(url_for("views.guide"))


@views.route("/guide")
def guide():
    return render_template("guide.html", user=current_user)
