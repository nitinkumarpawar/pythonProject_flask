from flask import Flask

app = Flask(__name__)
from controller import *


@app.route("/")
def hello():
    return "flask1"


@app.route("/flask")
def demo_flask():
    return "This is flask demo"
