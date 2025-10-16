import sqlite3

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

users = [
    ('admin', 'admin@restoran.com', 'hashed_password_123', 'admin'),
    ('umut_gungor', 'umut@example.com', 'rastgele_password_123', 'customer'),
    ('dogukan_staff', 'dogukan@restaurant.com', 'rastgele_password_456', 'staff')
]

cursor.executemany('''
    INSERT INTO users (username, email, password_hash, role)
    VALUES(?, ?, ?, ?)
''', users)

menu_items = [
    ("Adana Kebab", "Acılı kebap, lavaş ile servis", 45.00, "kebab", None, 1),
    ("Döner", "Tavuk döner porsiyon", 30.00, "kebab", None, 1),
    ("Mercimek Çorbası", "Klasik çorba", 15.00, "soup", None, 1)
]

cursor.executemany('''
    INSERT INTO menu_items (name, description, price, category, image_url, available)
    VALUES (?, ?, ?, ?, ?, ?)
''', menu_items)

conn.commit()

print("✅ Test data added successfully!")
print(f"   Users: {len(users)}")
print(f"   Menu items: {len(menu_items)}")

conn.close()