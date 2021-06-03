"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import Monte_Karlo

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
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

@route('/three-chanel_system_with_rejection')
@view('three-chanel_system_with_rejection')
def about():
    """Renders the about page."""
    return dict(
        output = "",
        title='About',
        year=datetime.now().year
    )
@route('/Monte_Karlo')
@view('Monte_Karlo.html')
def about(output=[],tre = 0,nad = 0):
    """Renders the about page."""
    return dict(
        output = output,
        tre = tre,
        nad = nad,
        title='Monte',
        message='Your application description page.',
        year=datetime.now().year
    )
