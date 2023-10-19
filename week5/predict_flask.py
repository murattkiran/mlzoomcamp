import pickle
from flask import Flask
from flask import request
from flask import jsonify

def load(filename):
    with open(filename, "rb") as f_in:
        return  pickle.load(f_in)

dv = load("dv.bin")
model = load("model1.bin")

app = Flask("credit_approve")

@app.route("/predict_flask", methods=["POST"])
def predict():
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    approve = y_pred >= 0.5

    result = {
        "approve_probability": y_pred,
        "approve": bool(approve)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)

