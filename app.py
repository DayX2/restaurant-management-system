from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "🎮 Restaurant Management API - CDPR Journey",
        "status": "running",
        "day": 1,
        "date": "October 6, 2025"
    })

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": "0.1.0"
    })

if __name__ == '__main__':
    print("🚀 Starting Restaurant API...")
    print("📍 Visit: http://localhost:5000")
    app.run(debug=True, port=5000)