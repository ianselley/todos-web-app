from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User, Note
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user


auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_confirm = request.form['password-confirm']
        user = User.query.filter_by(username=username).first()

        if user:
            flash('username already exists')

        elif password != password_confirm:
            flash('Both passwords must be the same')

        else:
            # Se utiliza la función hash "sha256" para no almacenar la contraseña tal cual, sino gurardar el hash
            new_user = User(username=username, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')
            # flash('WARNING! DO NOT INTRODUCE ANY SENSITIVE INFORMATION. The database is public on github', category='warning')

            if request.form.get('direct-login'):
                login_user(new_user, remember=True)
                return redirect(url_for('views.my_notes'))

            return redirect(url_for('auth.login'))

    # flash('WARNING! DO NOT INTRODUCE ANY SENSITIVE INFORMATION. Although the passwords are hashed, the database is public on github', category='warning')
    return render_template('sign_up.html', user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                # flash('WARNING! DO NOT INTRODUCE ANY SENSITIVE INFORMATION. The database is public on github', category='warning')
                login_user(user, remember=True)
                return redirect(url_for('views.my_notes'))
            else:
                flash('Invalid password, try again.')
        else:
            flash('username does not exist, try again.')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', category='success')
    db.session.close()
    return redirect(url_for('auth.login'))
