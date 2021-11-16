from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Category, Note
from . import db
import json


my_categories = Blueprint("my_categories", __name__)


@my_categories.route("/my-categories", methods=["GET"])
@login_required
def get():
    return render_template("my_categories.html", user=current_user)


@my_categories.route("/post-category", methods=["POST"])
@login_required
def post_category():
    name = request.form['category_name']
    categories = Category.query.filter_by(user_id=current_user.id).all()
    if name in [category.name for category in categories]:
        flash("That category already exists", category="error")
        return jsonify({})
    new_category = Category(name=name, user_id=current_user.id)
    db.session.add(new_category)
    db.session.commit()
    return redirect(url_for('.get'))


@my_categories.route("/delete-category/<category_id>", methods=["POST"])
@login_required
def delete_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    notes = Note.query.filter_by(category_id=category_id).all()
    if category:
        if category.user_id != current_user.id:
            flash("You are not allowed to modify this category!", category="error")
            return redirect("/my-categories")
        else:
            db.session.delete(category)
            for note in notes:
                db.session.delete(note)
            db.session.commit()
    return redirect(url_for('.get'))


@my_categories.route("/edit-category/<category_id>", methods=["POST"])
@login_required
def edit_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if category:
        if category.user_id != current_user.id:
            flash("You are not allowed to modify this category!", category="error")
            return redirect(url_for("my_categories.get"))
        category.name = request.form[f"content-{category_id}"]
        db.session.commit()
    else:
        flash("That note does not exist", category="error")
    return redirect(url_for('.get'))
