""" test """
from flask import Flask
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """Function printing path."""
    print(path)
    # return '{"path": "' + path + '"}'
    return f'{{"path": "{path}"}}'

# @app.route("/api/python")
# def hello_world():
#     """Function printing python version."""
#     return '{"test": "yo"}'
