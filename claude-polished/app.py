<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import socket

app = Flask(__name__)
=======
import os
import logging
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from menu import menu

app = Flask(__name__)

# Store orders in memory (for testing)
>>>>>>> 02f34dd67143036ee036b17bbafbd36d3a4c8afc
orders = {}
order_counter = 1000

@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('order.html')
=======
    return render_template('order.html', menu=menu)
>>>>>>> 02f34dd67143036ee036b17bbafbd36d3a4c8afc

@app.route('/place-order', methods=['POST'])
def place_order():
    global order_counter
    order_counter += 1
<<<<<<< HEAD
    data = request.json
    data['timestamp'] = datetime.now().strftime('%I:%M %p')
    data['order_id'] = order_counter
    data['status'] = 'received'
    orders[order_counter] = data
    print(f"\n🍽️  NEW ORDER #{order_counter}")
    for item in data.get('items', []):
        print(f"   → {item['item']} | ₹{item['price']}")
    print(f"   TOTAL: ₹{data.get('total', 0)}")
    return jsonify({'success': True, 'order_id': order_counter})
=======
    
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
>>>>>>> 02f34dd67143036ee036b17bbafbd36d3a4c8afc

@app.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')

<<<<<<< HEAD
@app.route('/kitchen-orders')
def kitchen_orders():
    pending = {k: v for k, v in orders.items() if v['status'] in ['received', 'preparing']}
    return jsonify(pending)

@app.route('/update-status/<int:order_id>', methods=['POST'])
def update_status(order_id):
    if order_id in orders:
        orders[order_id]['status'] = request.json.get('status')
    return jsonify({'success': True})

if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except:
        local_ip = '0.0.0.0'
    PORT = 8080
    print("=" * 55)
    print("✅ SERVER RUNNING!")
    print(f"📱 On this computer: http://127.0.0.1:{PORT}")
    print(f"📱 On your phone: http://{local_ip}:{PORT}")
    print("=" * 55)
    app.run(debug=True, host='0.0.0.0', port=PORT)
@app.route('/qr')
def qr_page():
    return render_template('qr.html')
=======
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
>>>>>>> 02f34dd67143036ee036b17bbafbd36d3a4c8afc
