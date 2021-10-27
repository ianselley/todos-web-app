from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Category
from . import db
import json
from datetime import date


my_notes = Blueprint("my_notes", __name__)

not_allowed = "You are not allowed to modify this note!"


@my_notes.route("/my-notes/<category_id>", methods=["GET"])
@login_required
def get(category_id):
    category = Category.query.filter_by(id=category_id).first()
    return render_template("my_notes.html", category=category, user=current_user)


@my_notes.route("/post-note/<category_id>", methods=["POST"])
@login_required
def post_note(category_id):
    content = request.form["note_content"]
    new_note = Note(content=content, category_id=category_id, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    return redirect(f"/my-notes/{category_id}")


@my_notes.route("/check-note", methods=["POST"])
@login_required
def check_note():
    data = json.loads(request.data)
    note_id = data["id"]
    note = Note.query.filter_by(id=note_id).first()
    category_id = note.category_id
    if note:
        if note.user_id != current_user.id:
            flash(not_allowed, category="error")
            return redirect(f"/my-notes/{category_id}")
        note.complete = not note.complete
        db.session.commit()
    else:
        flash("That note does not exist any more", category="error")
    return jsonify({})


@my_notes.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    data = json.loads(request.data)
    note_id = data["id"]
    note = Note.query.filter_by(id=note_id).first()
    category_id = note.category_id
    if note:
        if note.user_id != current_user.id:
            flash(not_allowed, category="error")
            return redirect(f"/my-notes/{category_id}")
        else:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


@my_notes.route("/edit-note", methods=["POST"])
@login_required
def edit_note():
    data = json.loads(request.data)
    note_id = data["id"]
    note_content = data["content"]
    note_category_id = data["category_id"]
    note_details = data["details"]
    note_expires = data["expires"]
    note = Note.query.filter_by(id=note_id).first()
    if note:
        if note.user_id != current_user.id:
            flash(not_allowed, category="error")
            return redirect(f"/my-notes/{note.category_id}")
        note.content = note_content
        note.category_id = note_category_id
        note.details = note_details
        if note_expires:
            note.expires = date(*map(int, note_expires.split("-")))
        elif note_expires == "":
            note.expires = None
        db.session.commit()
    else:
        flash("That note does not exist", category="error")
    return jsonify({})


@my_notes.route("/toggle-important", methods=["POST"])
@login_required
def toggle_important():
    data = json.loads(request.data)
    note_id = data["id"]
    note = Note.query.filter_by(id=note_id).first()
    if note:
        if note.user_id != current_user.id:
            flash("You are not allowed to modify this note!", category="error")
            return redirect(url_for("all_my_notes.get"))
        note.important = not note.important
        db.session.commit()
    else:
        flash("That note does not exist", category="error")
    return jsonify({})
