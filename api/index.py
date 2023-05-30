""" test """
import json
from flask import Flask

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """Function printing path."""
    d = {
        "path": path
    }

    return json.dumps(d)

# @app.route("/api/python")
# def hello_world():
#     """Function printing python version."""
#     return '{"test": "yo"}'
