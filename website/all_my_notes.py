from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Category

all_my_notes = Blueprint("all_my_notes", __name__)


@all_my_notes.route("/all-my-notes", methods=["GET"])
@login_required
def get():
    category_list = Category.query.filter_by(user_id=current_user.id).all()
    category_id_list = [category.id for category in category_list]
    return render_template(
        "all_my_notes.html", user=current_user, category_id_list=category_id_list
    )
