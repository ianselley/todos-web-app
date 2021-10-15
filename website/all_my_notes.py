from flask import Blueprint, render_template, redirect, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


all_my_notes = Blueprint("all_my_notes", __name__)


@all_my_notes.route("/all-my-notes", methods=["GET"])
@login_required
def get():
    return render_template("all_my_notes.html", user=current_user)


@all_my_notes.route("/all-check-note", methods=["POST"])
@login_required
def check_note(note_id):
    data = json.loads(request.data)
    note_id = data["id_"]
    note = Note.query.filter_by(id=note_id)
    if note:
        if note.user_id != current_user.id:
            flash("You are not allowed to modify this note!", category="error")
            return redirect("/all-my-notes")
        note.complete = not note.complete
        db.session.commit()
    else:
        flash("That note does not exist any more", category="error")
    return jsonify({})


@all_my_notes.route("/all-delete-note", methods=["POST"])
@login_required
def delete_note(note_id):
    data = json.loads(request.data)
    note_id = data["id_"]
    note = Note.query.filter_by(id=note_id).first()
    if note:
        if note.user_id != current_user.id:
            flash("You are not allowed to modify this note!", category="error")
            return redirect("/all-my-notes")
        else:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


@all_my_notes.route("/all-edit-note", methods=["POST"])
@login_required
def edit_note(note_id):
    data = json.loads(request.data)
    note_id = data["id_"]
    note = Note.query.filter_by(id=note_id).first()
    if note:
        if note.user_id != current_user.id:
            flash("You are not allowed to modify this note!", category="error")
            return redirect("/all-my-notes")
        new_content = request.form[f"content{note_id}"]
        change = False if note.content.strip() == new_content.strip() else True
        note.content = new_content
        db.session.commit()
        if change:
            flash("Note edited successfully", category="success")
    else:
        flash("That note does not exist", category="error")
    return jsonify({})
