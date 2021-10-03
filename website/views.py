from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User, Note
from . import db


views = Blueprint('views', __name__)


@views.route('/manual')
def manual():
    return render_template('manual.html', user=current_user)


@views.route('/', methods=['GET'])
@login_required
def my_notes():
    return render_template('my_notes.html', user=current_user)


@views.route('/post-note', methods=['POST'])
@login_required
def post_note():
    content = request.form['note_content']
    new_note = Note(content=content, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    flash('Note added successfully', category='success')
    return redirect(url_for('views.my_notes'))


@views.route('/delete-note/<note_id>', methods=['GET'])
@login_required
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note.user_id != current_user.id:
        flash('You are not allowed to modify this note!', category='error')
        return redirect(url_for('views.my_notes'))
    if note:
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for('views.my_notes'))


@views.route('/check-note/<note_id>', methods=['GET'])
@login_required
def check_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note.user_id != current_user.id:
        flash('You are not allowed to modify this note!', category='error')
        return redirect(url_for('views.my_notes'))
    if note:
        note.complete = not note.complete
        db.session.commit()
    else:
        flash('That note does not exist any more', category='error')
    return redirect(url_for('views.my_notes'))


@views.route('/edit_note/<note_id>', methods=['POST'])
@login_required
def edit_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note.user_id != current_user.id:
        flash('You are not allowed to modify this note!', category='error')
        return redirect(url_for('views.my_notes'))
    if note:
        new_content = request.form[f'content{note_id}']
        change = False if note.content.strip() == new_content.strip() else True
        note.content = new_content
        db.session.commit()
        if change:
            flash('Note edited successfully', category='success')
    else:
        flash('That note does not exist', category='error')
    return redirect(url_for('views.my_notes'))


@views.route('/more_info/<note_id>', methods=['GET', 'POST'])
@login_required
def more_info(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if note.user_id != current_user.id:
        flash('You are not allowed to modify this note!', category='error')
        return redirect(url_for('views.my_notes'))
    if note:
        pass
    else:
        flash('That note does not exist', category='error')
