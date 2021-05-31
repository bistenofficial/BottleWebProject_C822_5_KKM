"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import Monte

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/Monte_Karlo')
@view('Monte_Karlo')
def about():
    """Renders the about page."""
    return dict(
        title='Monte_Karlo',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/Monte_Karlo_NEGR')
@view('Monte_Karlo_NEGR')
def about():
    """Renders the about page."""
    return dict(
        title='Four-channel queuing system with limited queue',
        message='GG',
        year=datetime.now().year
    )
