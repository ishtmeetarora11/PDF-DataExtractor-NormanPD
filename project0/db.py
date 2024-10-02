import sqlite3
import os
def createdb():
    if os.path.exists("./resources/normanpd.db"):
        os.remove("./resources/normanpd.db")
    connection = sqlite3.connect("./resources/normanpd.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT
);""")

    connection.commit()
    return connection

def populatedb(conn, incidents):
    curr = conn.cursor()
    data_to_insert = [(incident['Date_Time'], incident['Incident Number'], incident['Location'], incident['Nature'], incident['ORI'])
                  for incident in incidents]

    curr.executemany("""
                INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori)
                VALUES (?, ?, ?, ?, ?);
                 """,data_to_insert)

def status(conn):
    curr = conn.cursor()
    data =  curr.execute("""
                SELECT nature, COUNT(*)
                FROM incidents
                GROUP BY nature
                ORDER BY COUNT(*) DESC, nature ASC;
                """)
    for (nature, count) in data:
        print(f"{nature}|{count}")       

