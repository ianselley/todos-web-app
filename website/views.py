from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


views = Blueprint("views", __name__)


@views.route("/")
def redirect_to_manual():
    return redirect(url_for("views.manual"))


@views.route("/manual")
def manual():
    return render_template("manual.html", user=current_user)
