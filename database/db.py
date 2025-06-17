import sqlite3

def add_book(title, author):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()
    print('The book has been added to the library.')

add_book('Z mgły', 'Brandon')