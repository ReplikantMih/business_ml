import dill
import numpy as np
import pandas as pd
import os

import traceback
import json
import flask
import logging
from logging.handlers import RotatingFileHandler
from time import strftime
import warnings

dill._dill._reverse_typemap['ClassType'] = type
warnings.simplefilter("ignore")

model_path = "models/model_trained_forest.dill"



app = flask.Flask(__name__)

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def load_model(model_path):
	with open(model_path, 'rb') as f:
		return dill.load(f)


model = load_model(model_path)


@app.route("/", methods=["GET"])
def general():
	return 'UFC fights predictor'


@app.route("/predict", methods=["POST"])
def predict():
	if not flask.request.method == "POST":
		return 'Only POST method allowed.'


	request_json = flask.request.get_json()
	print(request_json)
	try:
		df = pd.DataFrame(json.loads(request_json))
		preds = list(model.predict_proba(df)[0])
		print(preds, preds[0])
		classes = list(model.classes_)
		results = {}
		for i in range(len(classes)):
			results[int(classes[i])] = preds[i]
		return json.dumps(results)
	except:
		print(traceback.format_exc())
		return 'Wrong format'


if __name__ == "__main__":
	print('\nApplication \"UFC fights predictor\" starting\n')
	port = 5000
	app.run(host='localhost', debug=False, port=port)
