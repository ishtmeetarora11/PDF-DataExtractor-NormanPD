# test_database.py
import pytest
from unittest.mock import patch
from project0 import db
import sqlite3

@pytest.fixture
def db_connection():
    # Patch the connect method of sqlite3 module to always create an in-memory database during tests
    with patch('sqlite3.connect', return_value=sqlite3.connect(":memory:")):
        conn = db.createdb()  # This will now use the patched sqlite3.connect
        yield conn
        conn.close()

def test_createdb(db_connection):
    cur = db_connection.cursor()
    # Check if the table was created correctly
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='incidents';")
    assert cur.fetchone() is not None

def test_populatedb(db_connection):
    # Sample data to insert
    incidents = [
        {'Date_Time': '2021-01-01 10:00', 'Incident Number': '001', 'Location': 'Someplace', 'Nature': 'Theft', 'ORI': 'ORI1'},
        {'Date_Time': '2021-01-02 11:00', 'Incident Number': '002', 'Location': 'Otherplace', 'Nature': 'Assault', 'ORI': 'ORI2'}
    ]
    db.populatedb(db_connection, incidents)
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM incidents")
    assert cur.fetchone()[0] == 2

def test_status(db_connection):
    # Prepare data
    test_populatedb(db_connection)
    # Use a mock to capture print statements
    with patch('builtins.print') as mocked_print:
        db.status(db_connection)
        mocked_print.assert_any_call('Theft|1')
        mocked_print.assert_any_call('Assault|1')
