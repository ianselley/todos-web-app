from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Note, Category


views = Blueprint("views", __name__)


@views.route("/")
def redirect_to_manual():
    return redirect(url_for("views.manual"))


@views.route("/manual")
def manual():
    return render_template("manual.html", user=current_user)


@views.route("/more-info/<note_id>", methods=["GET", "POST"])
@login_required
def more_info(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note.user_id != current_user.id:
        flash("You are not allowed to modify this note!", category="error")
        return redirect(url_for("my_notes.get"))
    if note:
        pass
    else:
        flash("That note does not exist", category="error")
