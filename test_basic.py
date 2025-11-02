import os
import sqlite3
from app import init_db, DB_PATH, hash_password

def test_hash_password():
    assert hash_password("password") == hash_password("password")

def test_db_init():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    assert c.fetchone() is not None
    conn.close()
