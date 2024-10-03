import sqlite3
import os

def createdb():
    # Check if the database file already exists and remove it to start fresh
    if os.path.exists("./resources/normanpd.db"):
        os.remove("./resources/normanpd.db")
    
    # Connect to the SQLite database, creating a new file in the resources folder
    connection = sqlite3.connect("./resources/normanpd.db")
    cursor = connection.cursor()

    # Execute SQL command to create a new table for incidents
    cursor.execute("""
        CREATE TABLE incidents (
            incident_time TEXT,
            incident_number TEXT,
            incident_location TEXT,
            nature TEXT,
            incident_ori TEXT
        );
    """)

    # Commit the changes to the database
    connection.commit()
    
    # Return the connection object for further use
    return connection

def populatedb(conn, incidents):
    # Obtain a cursor object from the database connection
    curr = conn.cursor()
    
    # Prepare data for insertion into the incidents table from the incidents list
    data_to_insert = [
        (
            incident['Date_Time'],
            incident['Incident Number'],
            incident['Location'],
            incident['Nature'],
            incident['ORI']
        ) for incident in incidents
    ]

    # Execute many insert statements to populate the database
    curr.executemany("""
        INSERT INTO incidents (
            incident_time,
            incident_number,
            incident_location,
            nature,
            incident_ori
        ) VALUES (?, ?, ?, ?, ?);
    """, data_to_insert)

def status(conn):
    # Obtain a cursor object from the database connection
    curr = conn.cursor()
    
    # Execute SQL query to count occurrences of each 'nature' in the incidents table
    data = curr.execute("""
        SELECT nature, COUNT(*)
        FROM incidents
        GROUP BY nature
        ORDER BY nature ASC;
    """)
    
    # Iterate through each result and print it formatted as 'nature|count'
    for (nature, count) in data:
        print(f"{nature}|{count}")
