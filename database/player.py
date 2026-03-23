import json
import os
from datetime import datetime

DB_FILE = "database/users.json"

def load_db():
    if os.path.exists(DB_FILE) and os.path.getsize(DB_FILE) > 0:
        with open(DB_FILE) as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)

def register(username, password):
    db = load_db()
    if username in db:
        return None, "❌ Username already exists!"
    db[username] = {
        "password": password,
        "balance": 1000,
        "wins": 0,
        "losses": 0,
        "joined": datetime.now().strftime("%Y-%m-%d")
    }
    save_db(db)
    return db[username], "✅ Account created!"

def login(username, password):
    db = load_db()
    if username not in db:
        return None, "❌ Username not found!"
    if db[username]["password"] != password:
        return None, "❌ Wrong password!"
    return db[username], "✅ Login successful!"

def save_player(username, data):
    db = load_db()
    db[username] = data
    save_db(db)

def get_leaderboard():
    db = load_db()
    players = [(u, d["balance"], d["wins"]) for u, d in db.items()]
    players.sort(key=lambda x: x[1], reverse=True)
    return players[:10]