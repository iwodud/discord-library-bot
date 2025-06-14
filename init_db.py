import sqlite3
from pathlib import Path

SCHEMA_PATH = Path("database/schema.sql")
DB_PATH = Path("library.db")

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
