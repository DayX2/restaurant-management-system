# restaurant-management-system
Full-stack restaurant management app
**Part of my 10 months development journey**

- **Backend:** Python 3.13, Flask
- **Database:** SQLite (dev) → PostgreSQL (prod)
- **Frontend:** React (coming soon)

## Features (Planned)
- [ ] User authentication
- [ ] Menu management (CRUD)
- [ ] Order system
- [ ] Payment simulation
- [ ] Admin panel
- [ ] Real-time notifications

## Progress

> Building a production-ready restaurant management application

## Tech Stack
- **Backend:** Python 3.13, Flask, SQLite
- **Frontend:** React (planned)
- **Database:** SQLite → PostgreSQL (production)

## Features
- [x] Menu management API
- [x] Database integration
- [ ] User authentication
- [ ] Order system
- [ ] Admin dashboard

## Database Schema
- users
- menu_items
- orders
- order_items

[See full schema](schema.sql)

## API Endpoints

### Menu
```
GET  /api/menu        - Get all menu items
GET  /api/menu/:id    - Get single item
```

## Setup

\`\`\`bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install flask

# Initialize database
python init_db.py
python seed_data.py

# Run server
python app.py
\`\`\`

## Progress

**Day 1:** Flask setup, first API  
**Day 2:** Database schema, Menu API  
**Day 3:** C programming basics

---
