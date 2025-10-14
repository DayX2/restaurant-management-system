from flask import Flask, jsonify

app = Flask(__name__)

# Menü verileri
MENU_ITEMS = [
    {"id": 1, "name": "Adana Kebab", "price": 41, "category": "kebab"},
    {"id": 2, "name": "Döner Kebab", "price": 35, "category": "kebab"},
    {"id": 3, "name": "Mercimek Çorbası", "price": 15, "category": "soup"},
    {"id": 4, "name": "Mantı", "price": 25, "category": "pasta"},
    {"id": 5, "name": "Haydari", "price": 10, "category": "appetizer"},
]

@app.route('/')
def home():
    return jsonify({
        "message": "🎮 Restaurant Management API",
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


@app.route('/api/menu')
def get_menu():
    return jsonify({
        "total": len(MENU_ITEMS),
        "items": MENU_ITEMS
    })


@app.route('/api/menu/<int:item_id>')
def get_menu_item(item_id):
    item = next((item for item in MENU_ITEMS if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404


if __name__ == '__main__':
    print("🚀 Starting Restaurant API...")
    print("📍 Visit: http://localhost:5000")
    app.run(debug=True, port=5000)