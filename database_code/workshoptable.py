# Author: Bradley Hartlove
# Assn Name: Flask Tables
# Date: April 23, 2021
# Description: This python file will create a table called "workshops" within the database
# and fill the table with each workshops name, session number, room number, start time, and end time

import sqlite3
import os

# Read through file and fill dictionary
workshopData = []
file = open("workshops.csv")
for line in file:
    line = line.strip()
    dataSplit = line.split(",")
    name = dataSplit[0]
    sessionNumber = dataSplit[1]
    roomNum = dataSplit[2]
    startTime = dataSplit[3]
    endTime = dataSplit[4]
    newDictionary = {'Name': name,
                     'Session Number': sessionNumber,
                     'Room Number': roomNum,
                     'Start Time': startTime,
                     'End Time': endTime}
    workshopData.append(newDictionary)

# Goes up one directory to access conference database
os.chdir("..")


# Connect to the database
def db_connect():
    db_name = "conference.sqlite"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row

    return conn


# Creates table nominees in database
db = db_connect()
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS workshops(
                id INTEGER PRIMARY KEY,
                name TEXT not null ,
                sessionNum TEXT not null ,
                roomNum TEXT not null ,
                startTime TEXT NOT NULL,
                endTime TEXT NOT NULL,
                UNIQUE (name, sessionNum, roomNum)
                );""")

db.commit()

# Keeps from adding duplicates to table
cur.execute("""CREATE INDEX IF NOT EXISTS idx_name
ON workshops (name);""")
cur.execute("""CREATE INDEX IF NOT EXISTS idx_sessionNum
ON workshops (sessionNum);""")
cur.execute("""CREATE INDEX IF NOT EXISTS idx_roomNum
ON workshops (roomNum);""")
db.commit()

# Iterate through list of dictionaries
for dictionary in workshopData:
    cur.execute("""INSERT OR IGNORE INTO workshops (name, sessionNum, roomNum, startTime, endTime) 
        VALUES(?,?,?,?,?);""", [dictionary['Name'], dictionary['Session Number'], dictionary['Room Number'],
                                dictionary['Start Time'], dictionary['End Time']])
    db.commit()

# Close out cursor and db
cur.close()
db.close()
