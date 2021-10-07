from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Category, Note
from . import db


my_categories = Blueprint("my_categories", __name__)


@my_categories.route("/my-categories", methods=["GET"])
@login_required
def get():
    return render_template("my_categories.html", user=current_user)


@my_categories.route("/post-category", methods=["POST"])
@login_required
def post_category():
    name = request.form["category_name"]
    new_category = Category(name=name, user_id=current_user.id)
    db.session.add(new_category)
    db.session.commit()
    flash("Category added successfully", category="success")
    return redirect(url_for("my_categories.get"))


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
    return redirect("/my-categories")


@my_categories.route("/edit-category/<category_id>", methods=["POST"])
@login_required
def edit_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if category:
        if category.user_id != current_user.id:
            flash("You are not allowed to modify this category!", category="error")
            return redirect(url_for("my_categories.get"))
        new_name = request.form[f"content{category_id}"]
        change = False if category.name.strip() == new_name.strip() else True
        category.name = new_name
        db.session.commit()
        if change:
            flash("Note edited successfully", category="success")
    else:
        flash("That note does not exist", category="error")
    return redirect("/my-categories")
