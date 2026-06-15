from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle 

app = Flask(__name__)

model = pickle.load(open('./models/project_cycle_03_model.pkl', 'rb'))
scaler = pickle.load(open('./models/project_cycle_03_scaler.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def predict():

    data = {
    "Temperature": float(request.form["Temperature"]),
    "RH": float(request.form["RH"]),
    "Ws": float(request.form["Ws"]),
    "Rain": float(request.form["Rain"]),
    "FFMC": float(request.form["FFMC"]),
    "DMC": float(request.form["DMC"]),
    "ISI": float(request.form["ISI"]),
    "Classes": int(request.form["Classes"]),
    "Region": int(request.form["Region"])
}

    features = np.array([list(data.values())])

    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)[0]

    return render_template(
        "result.html",
        prediction=round(prediction, 2),
        data=data
    )


if __name__ == '__main__':
    app.run(port=6006)