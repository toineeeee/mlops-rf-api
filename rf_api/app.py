from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd

app = Flask(__name__)
model = mlflow.pyfunc.load_model("model")  # à faire juste après : copier le modèle ici

@app.route("/")
def home():
    return "L'API fonctionne ! 🎉"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

