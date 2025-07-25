#!/usr/bin/env python3
"""
Basic Flask app with Babel and internationalization
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """Get the best matching locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render the index page"""
    return render_template('3-index.html')
