from flask import Flask, render_template, request, jsonify
from datetime import datetime
import socket

app = Flask(__name__)
orders = {}
order_counter = 1000

@app.route('/')
def index():
    return render_template('order.html')

@app.route('/place-order', methods=['POST'])
def place_order():
    global order_counter
    order_counter += 1
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

@app.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')

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
