#!/usr/bin/env python3
""" Babel setup """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Babel Configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def hello_world():
    """ 
        simply outputs “Welcome to Holberton” as page title (<title>)
        and “Hello world” as header (<h1>
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")