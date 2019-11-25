from flask import Blueprint
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')