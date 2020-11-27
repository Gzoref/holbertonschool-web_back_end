#!/usr/bin/env python3

"""Route module for the API
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Available languages class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return:
        Hello world
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ Determine best match for supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")