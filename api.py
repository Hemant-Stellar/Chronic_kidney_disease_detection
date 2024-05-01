from flask import Flask,request,jsonify
from markupsafe import escape
import numpy as np
import joblib
import json
from flask_cors import CORS
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
CORS(app)
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello'
	
@app.route('/predict',methods=['POST'])
def predict():
	try:
		data = request.get_json(force=True)
		features = [np.array(data['data'])]
		prediction = model.predict(features)
		return jsonify({"output":str(prediction[0])})
	except:
		return jsonify({"error":"Data was inconsistent"})

if __name__ == "__main__":
	app.run(debug=True)		
