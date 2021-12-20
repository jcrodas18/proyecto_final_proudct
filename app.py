from flask import Flask, jsonify, request
import pandas as pd

import config2 as cfg
import pipeline_predict as pp


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"   

@app.route("/predecirsalescustomer", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    dataframe = pd.json_normalize(json_data)
    data = dataframe

    #cambiar nombre X1stFlrSF y X2ndFlrSF
    data = data[cfg.FEATURES]
    resultado = pp.predict(data)
    print(resultado)
    return jsonify({"Prediccion": resultado})




