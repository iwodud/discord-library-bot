import sqlite3


def connect_with_db(func):
    def wrapper(*args):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        result = func(cursor, *args)
        conn.commit()
        conn.close()
        return result
    return wrapper


@connect_with_db
def add_book(cursor, title, author):
    '''Adds book into the "books" table'''
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    print('The book has been added to the library.')


@connect_with_db
def get_all_books(cursor):
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()


def format_books(books):
    if not books:
        return "Brak książek."
    return "\n".join(f"{b[0]}. {b[1]} — {b[2]}" for b in books)

if __name__ == "__main__":
    books = get_all_books()
    print(format_books(books))
