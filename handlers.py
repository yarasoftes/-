from flask import render_template, redirect, url_for, request
from forms import UserForm
from models import db, User

def index():
    users = User.query.all()
    return render_template('index.html', users=users)

def add_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html', form=form)