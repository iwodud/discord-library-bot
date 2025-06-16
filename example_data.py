# Optional script to populate the database with example books, users, and loans
# Useful for local development and testing

import sqlite3
from datetime import date, timedelta

def seed_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users (discord_id, username)
        VALUES (?, ?)""", ("123456789", "janek"))

    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Wiedźmin", "Andrzej Sapkowski"))
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Hobbit", "J.R.R. Tolkien"))

    cursor.execute("SELECT id FROM books WHERE title = 'Wiedźmin'")
    wied_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM books WHERE title = 'Hobbit'")
    hobbit_id = cursor.fetchone()[0]

    cursor.execute("INSERT INTO copies (book_id, album_number) VALUES (?, ?)", (wied_id, "W-001"))
    cursor.execute("INSERT INTO copies (book_id, album_number) VALUES (?, ?)", (wied_id, "W-002"))
    cursor.execute("INSERT INTO copies (book_id, album_number) VALUES (?, ?)", (hobbit_id, "H-001"))

    cursor.execute("SELECT id FROM users WHERE discord_id = '123456789'")
    user_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM copies WHERE album_number = 'W-001'")
    copy_id = cursor.fetchone()[0]

    today = date.today()
    due_date = today + timedelta(days=14)
    cursor.execute("""
        INSERT INTO loans (user_id, copy_id, loan_date, due_date, returned)
        VALUES (?, ?, ?, ?, 0)
    """, (user_id, copy_id, today.isoformat(), due_date.isoformat()))

    conn.commit()
    conn.close()
    print("Example data has been added to the database.")

if __name__ == "__main__":
    seed_data()
