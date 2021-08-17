import sqlite3


def db_connect():
    db_name = "confrence.sqlite"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn

with db_connect() as db:
    cur = db.cursor()
    cur.execute("CREAT")