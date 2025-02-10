from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

data_file = "payment_data.txt"

@app.route('/submit', methods=['POST'])
def submit_data():
    """Handles submission of payment data."""
    data = request.get_json()
    card_number = data.get('cardNumber')
    expiry_date = data.get('expiryDate')
    cvv = data.get('cvv')

    if card_number and expiry_date and cvv:
        with open(data_file, 'a') as file:
            file.write(f"Card Number: {card_number}, Expiry Date: {expiry_date}, CVV: {cvv}\n")
        return jsonify({"message": "Data saved successfully"}), 200
    else:
        return jsonify({"message": "Invalid data"}), 400

@app.route('/verify', methods=['GET'])
def verify():
    """Verifies that the server is running."""
    return jsonify({"message": "Server is running!"}), 200

if __name__ == '__main__':
    if not os.path.exists(data_file):
        with open(data_file, 'w') as f:
            pass
    app.run(debug=True, host="0.0.0.0", port=8000)