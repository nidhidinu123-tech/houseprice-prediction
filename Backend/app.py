
from flask import Flask, request, jsonify
import numpy as np
import joblib

# Create Flask application
app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("house price.pkl")
scaler = joblib.load("scaler.pkl")


# Home route
@app.route("/")
def home():
    return "House Price Prediction API is running!"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Get input features
        features = [
            float(data["income"]),
            float(data["age"]),
            float(data["rooms"]),
            float(data["bedrooms"]),
            float(data["population"])
        ]

        # Convert to NumPy array
        input_data = np.array(features).reshape(1, -1)

        # Scale input
        input_scaled = scaler.transform(input_data)

        # Predict house price
        prediction = model.predict(input_scaled)

        # Return result
        return jsonify({
            "predicted_price": float(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)