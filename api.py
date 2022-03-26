from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/peem")
def hello_world():
    app.logger.info('API return to log in')


    return jsonify(
        username="daniel",
        email="daniel@godpeem.com",
        id="123",
    )