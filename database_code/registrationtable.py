# Author: Bradley Hartlove
# Assn Name: Flask Tables
# Date: April 23, 2021
# Description: This python file will create a table called "registrants" within the database
# and fill the table with registrant data using a registrant object defined below

import sqlite3
import os
from os import path


# Create registrant class
class registrant:
    def __init__(self, date, title, first_name, last_name, address_one, address_two, city,
                 state, zipcode, telephone, email, website, position, company, meals,
                 billing_firstname, billing_lastname, card_type, card_number, card_csv,
                 exp_year, exp_month, session_one, session_two, session_three):
        self.date = date
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.address_one = address_one
        self.address_two = address_two
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.telephone = telephone
        self.email = email
        self.website = website
        self.position = position
        self.company = company
        self.meals = meals
        self.billing_firstname = billing_firstname
        self.billing_lastname = billing_lastname
        self.card_type = card_type
        self.card_number = card_number
        self.card_csv = card_csv
        self.exp_year = exp_year
        self.exp_month = exp_month
        self.session_one = session_one
        self.session_two = session_two
        self.session_three = session_three


# List of registrant objects
registrantList = []

# Open file and read data into list of registrant objects
if path.exists("registrant_data.csv"):
    file = open('registrant_data.csv')
else:
    file = open('database_code/registrant_data.csv')
for line in file:
    line = line.strip()  # Remove newline character
    data_split = line.split(",")
    newRegistrant = registrant(data_split[0], data_split[1], data_split[2], data_split[3], data_split[4], data_split[5],
                               data_split[6], data_split[7], data_split[8], data_split[9], data_split[10],
                               data_split[11], data_split[12], data_split[13], data_split[14], data_split[15],
                               data_split[16], data_split[17], data_split[18], data_split[19], data_split[20],
                               data_split[21], data_split[22], data_split[23], data_split[24]
                               )
    registrantList.append(newRegistrant)


# Connect to the database
def db_connect():
    if path.exists('conference.sqlite'):
        db_name = "conference.sqlite"
    else:
        db_name = "../conference.sqlite"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row

    return conn


# Creates table nominees in database
db = db_connect()
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS registrants(
                id INTEGER PRIMARY KEY,
                date TEXT not null ,
                title TEXT not null ,
                first_name TEXT not null ,
                last_name TEXT NOT NULL,
                address_one TEXT NOT NULL,
                address_two TEXT NOT NULL,
                city TEXT not null ,
                state TEXT not null ,
                zipcode INTEGER not null ,
                telephone TEXT NOT NULL,
                email TEXT NOT NULL,
                website TEXT not null ,
                position TEXT not null ,
                company TEXT not null ,
                meals TEXT NOT NULL,
                billing_firstname TEXT NOT NULL,
                billing_lastname TEXT not null,
                card_type TEXT NOT NULL,
                card_number INTEGER NOT NULL,
                card_csv INTEGER not null ,
                exp_year INTEGER not null ,
                exp_month INTEGER not null ,
                session_one TEXT NOT NULL,
                session_two TEXT NOT NULL,
                session_three TEXT not null,
                UNIQUE (first_name, last_name, address_one, address_two)
                );""")

db.commit()

# Keeps from adding duplicates to table
cur.execute("""CREATE INDEX IF NOT EXISTS idx_first_name
ON registrants (first_name);""")
cur.execute("""CREATE INDEX IF NOT EXISTS idx_last_name
ON registrants (last_name);""")
cur.execute("""CREATE INDEX IF NOT EXISTS idx_address_one
ON registrants (address_one);""")
cur.execute("""CREATE INDEX IF NOT EXISTS idx_address_two
ON registrants (address_two);""")
db.commit()

# Iterate through list of registrants and insert into sqlite table
for reg in registrantList:
    cur.execute("""INSERT OR IGNORE INTO registrants (date, title, first_name, last_name, address_one,
    address_two, city, state, zipcode, telephone, email, website, position, company, meals,
     billing_firstname, billing_lastname, card_type, card_number, card_csv, exp_year, exp_month,
     session_one, session_two, session_three)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",
                [reg.date, reg.title,
                 reg.first_name, reg.last_name,
                 reg.address_one,
                 reg.address_two, reg.city, reg.state,
                 reg.zipcode, reg.telephone, reg.email,
                 reg.website,
                 reg.position, reg.company, reg.meals,
                 reg.billing_firstname, reg.billing_lastname,
                 reg.card_type, reg.card_number,
                 reg.card_csv, reg.exp_year, reg.exp_month,
                 reg.session_one, reg.session_two,
                 reg.session_three])
    db.commit()

# Close cursor and database connection
cur.close()
db.close()
