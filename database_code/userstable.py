# Author: Bradley Hartlove
# Assn Name: Flask Tables
# Date: April 23, 2021
# Description: This python file will create a table called "users" within the database
# and fill the table with id, username, first name, and last name

import sqlite3
import os

# Goes up one directory to access conference database
os.chdir("..")


# Function to connect to sqlite database
def db_connect():
    db_name = "conference.sqlite"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row

    return conn


# Creates table nominees in database
db = db_connect()
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT not null ,
                firstname TEXT not null ,
                lastname TEXT not null ,
                password INTEGER,
                UNIQUE (username, firstname, lastname)
                );""")

db.commit()

# Keeps from adding duplicates to table
cur.execute("""CREATE INDEX IF NOT EXISTS idx_username 
ON users (username);""")
cur.execute("""CREATE INDEX IF NOT EXISTS idx_firstname 
ON users (firstname);""")
cur.execute("""CREATE INDEX IF NOT EXISTS idx_lastname 
ON users (lastname);""")
db.commit()

file = open('database_code/users.csv')
for line in file:
    line = line.strip()# Removes new line character
    lineData = line.split(",")
    userName = lineData[0]
    firstName = lineData[1]
    lastName = lineData[2]
    passWord = lineData[3]
    record = [userName, firstName, lastName, passWord]
    cur.execute("""INSERT OR IGNORE INTO users (username, firstname, lastname, password) 
        VALUES(?,?,?,?);""", record)
    db.commit()


# Closes out cursor and database connection
cur.close()
db.close()
