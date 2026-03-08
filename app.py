import os
import logging
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from menu import menu

app = Flask(__name__)

# Store orders in memory (for testing)
orders = {}
order_counter = 1000

@app.route('/')
def index():
    return render_template('order.html', menu=menu)

@app.route('/place-order', methods=['POST'])
def place_order():
    global order_counter
    order_counter += 1
    
    order_data = request.json
    order_id = order_counter
    
    # Add timestamp and status
    order_data['timestamp'] = datetime.now().isoformat()
    order_data['order_id'] = order_id
    order_data['status'] = 'received'
    
    # Store order
    orders[order_id] = order_data
    
    print(f"✅ Order #{order_id} placed: {order_data}")  # For debugging
    
    return jsonify({
        'success': True,
        'order_id': order_id,
        'message': 'Order received!'
    })

@app.route('/kitchen-orders')
def kitchen_orders():
    # Return only pending orders
    pending = {}
    for order_id, order in orders.items():
        if order['status'] in ['received', 'preparing']:
            pending[order_id] = order
    return jsonify(pending)

@app.route('/update-status/<int:order_id>', methods=['POST'])
def update_status(order_id):
    status = request.json.get('status')
    if order_id in orders:
        orders[order_id]['status'] = status
        print(f"✅ Order #{order_id} status updated to: {status}")
    return jsonify({'success': True})

@app.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')

if __name__ == '__main__':
    print("🚀 Starting restaurant order system...")
    
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    PORT = 8080
    
    print("=" * 50)
    print("✅ SERVER RUNNING!")
    print("=" * 50)
    print(f"📱 On THIS computer: http://127.0.0.1:{PORT}")
    print(f"📱 On YOUR PHONE: http://{local_ip}:{PORT}")
    print("=" * 50)
    print("⚠️  Make sure phone is on same WiFi")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=PORT)