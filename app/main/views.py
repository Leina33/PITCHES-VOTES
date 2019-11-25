from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to wise users pitches'
    return render_template('index.html',title = title)

#dynamic route for pitch.html
@main.route('/pitches/<int:pitches_id>')
def pitches(pitches_id):

    '''
    View pitches page function that returns the pitches details page and its data
    '''
    return render_template('pitches.html',id = pitches_id)
