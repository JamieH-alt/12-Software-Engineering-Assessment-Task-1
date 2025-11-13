from flask import render_template
from app import app, db
from app.models import User
from app.forms import RegistrationForm
from datetime import datetime

@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def login():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(name=form.name.data, email=form.email.data, dob=form.dob.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', title='Register', form=form)
