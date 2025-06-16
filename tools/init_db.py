# One-time script to initialize the database structure from database/schema.sql
# Run once at project setup or if you want to reset the database.

import sqlite3
from pathlib import Path

SCHEMA_PATH = Path("tools/schema.sql")
DB_PATH = Path("../library.db") if __name__ == "__main__" else Path("library.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database has been initialized.")

if __name__ == "__main__":
    init_db()
