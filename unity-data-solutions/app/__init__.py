from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import endpoints
from app import utils
from app import data
from app import api
