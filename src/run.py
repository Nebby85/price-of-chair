from src.app import app
import os

__author__ = 'nebby85'


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], port=5000)
