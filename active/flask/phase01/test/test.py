from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/search")
def search():

    return f"""
Path: {request.path}

Args: {request.args}
"""


if __name__ == "__main__":
    app.run(debug=True)
