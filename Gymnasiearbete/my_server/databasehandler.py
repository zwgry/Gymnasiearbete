import sqlite3

def create_connection(db_file = 'db_test.db'):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn
