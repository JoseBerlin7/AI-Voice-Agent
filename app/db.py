import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/calls.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS call_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            caller TEXT,
            direction TEXT,
            transcript TEXT,
            intent TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_call(caller, direction, transcript, intent):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO call_logs (caller, direction, transcript, intent, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (caller, direction, transcript, intent, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_all_logs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM call_logs ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
