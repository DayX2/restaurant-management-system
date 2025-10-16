from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('restaurant.db')
    conn.row_factory = sqlite3.Row
    return conn


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
    conn = get_db_connection() 
    menu_items = conn.execute("SELECT * FROM menu_items WHERE available = 1").fetchall() 

    items = []
    for item in menu_items: 
        items.append({
            'id': item['id'],
            'name': item['name'],
            'description': item['description'],
            'price': item['price'],
            'category': item['category']
        })

    return jsonify({
        "total": len(items),
        "items": items  
    })


@app.route('/api/menu/<int:item_id>')
def get_menu_item(item_id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM menu_items WHERE id = ?', (item_id,)).fetchone()
    conn.close()

    if item:
        return jsonify({
            'id': item['id'],
            'name': item['name'],
            'description': item['description'],
            'price': item['price'],
            'category': item['category']
        })
    else:
        return jsonify({"error": "Item not found"}), 404


if __name__ == '__main__':
    print("🚀 Starting Restaurant API...")
    print("📍 Visit: http://localhost:5000")
    app.run(debug=True, port=5000)