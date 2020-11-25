#!/usr/bin/env python3

"""Route module for the API
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_LOCALE'] = 'UTC'


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return:
        Hello world
    """
    return render_template('1-index.html')


class Config:
    """ Available languages class
    """

    LANGUAGES = ["en", "fr"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
