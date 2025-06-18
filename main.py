from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []
menu = [
    {"id": 1, "item": "Pizza", "price": 250},
    {"id": 2, "item": "Burger", "price": 150},
    {"id": 3, "item": "Pasta", "price": 200}
]

@app.route('/')
def home():
    return "Welcome to the Food Order API<br>This is a JSON-based API to manage food orders.<br>Try endpoints like /orders, /menu using Postman or Curl."

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.json
    if not data or 'item_id' not in data:
        return jsonify({'error': 'Invalid order data'}), 400
    item = next((m for m in menu if m["id"] == data["item_id"]), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    order = {
        "order_id": len(orders) + 1,
        "item": item["item"],
        "price": item["price"]
    }
    orders.append(order)
    return jsonify(order), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)