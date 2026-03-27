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