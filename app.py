from flask import Flask, request, render_template, jsonify
from utils import get_car_price

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_price', methods = ['POST'])
def get_car_predicted_price():
    data = request.form

    pred_price = get_car_price(data)
    print("Predicted price is:", pred_price )

    return jsonify({"Predicted car price": pred_price})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
