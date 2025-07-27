'''Purpose: to create the db and log the messages'''

import sqlite3

def init_db():
    conn = sqlite3.connect("calls.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS call_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        caller_number TEXT,
        direction TEXT,
        timestamp TEXT,
        transcript TEXT,
        intent TEXT
    )''')
    conn.commit()
    conn.close()

def log_call(caller_number, direction, timestamp, transcript, intent):
    conn = sqlite3.connect("calls.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO call_logs (caller_number, direction, timestamp, transcript, intent) VALUES (?, ?, ?, ?, ?)",
        (caller_number, direction, timestamp, transcript, intent),
    )
    conn.commit()
    conn.close()

