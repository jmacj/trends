from flask import Blueprint, jsonify

from core.models import Delegates

from datetime import datetime, date, time

import json

app = Blueprint('api', __name__)

@app.route('/delegates', methods=['GET'])
def list_delegates():
	return jsonify([row for row in Delegates.select(Delegates).dicts()])
