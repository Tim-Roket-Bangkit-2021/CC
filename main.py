from flask import Flask, request, render_template, url_for
import os
import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    data = {"status": 200, "data": "Hello world"}
    prediksi = {
        "010621": 1,
        "020621": 2,
        "030621": 3,
        "040621": 4,
        "050621": 5,
        "060621": 6,
        "070621": 7,
        "080621": 8,
        "090621": 9,
        "100621": 10,
        "110621": 11,
        "120621": 12,
        "130621": 13,
        "140621": 14,
        "150621": 15,
        "160621": 16,
        "170621": 17,
        "180621": 18,
        "190621": 19,
        "200621": 20,
        "210621": 21,
        "220621": 22,
        "230621": 23,
        "240621": 24,
        "250621": 25,
        "260621": 26,
        "270621": 27,
        "280621": 28,
        "290621": 29,
        "300621": 30,
        "predictedapril": "https://storage.googleapis.com/kancatani/predictedApril.png",
        "predictedmay": "https://storage.googleapis.com/kancatani/PredictedMay.png"
    }
    data["val_prediksi_juni"] = prediksi
    return json.dumps(data)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))