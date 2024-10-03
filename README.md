# cis6930fa24-project0

Name: Ishtmeet Singh Arora

## Project Description
This project extracts incident data from the Norman Police Department's daily reports (in PDF format) and processing it for database storage and analysis. The project involves fetching the incident data from a given URL, extracting relevant information such as Date, Time, Incident Number, Location, Nature, and ORI, and then storing the data in an SQLite database. Finally, the data is queried and displayed, summarizing the count of each incident type.

## How to install

```
pipenv install -e .
```

## How to run
Run the following command on terminal
``` bash
pipenv run python project0/main.py --incidents <pdf_url>
```

Example :
``` bash
pipenv run python project0/main.py --incidents "https://www.normanok.gov/sites/default/files/documents/2024-08/2024-08-01_daily_incident_summary.pdf"
```

## Running Test Cases
```bash
pipenv run pytest
```

## Project Demo




## Functions

#### main.py 

The main(url) function runs everything together:

1. **`incident_data = fetchIncidents(url)`**:
   - Fetches incident data from the provided URL.

2. **`incidents = extractIncidents(incident_data)`**:
   - Extracts and processes incidents from the fetched data.

3. **`db = createdb()`**:
   - Initializes the database.

4. **`populatedb(db, incidents)`**:
   - Inserts the extracted incidents into the initialized database.

5. **`status(db)`**:
   - Checks or reports the status of the database.

### fetchincidents.py

```
def fetchIncidents(url, headers={}):

    This function fetches an incident PDF file from a given URL using Python’s urllib.request library. It sends an HTTP request to the specified URL, optionally including additional headers, and returns the content of the PDF as a BytesIO object.

    Args:
        url (str): The URL from which the incident PDF is to be downloaded.
        headers (dict, optional): A dictionary of optional HTTP headers to be included in the request. If no headers are provided, an empty dictionary is used by default.
        
    Returns:
        BytesIO: A BytesIO object containing the binary content of the incident PDF file. Using this later to read and process the PDF data in memory.

```

### extractincidents.py

```
def extractIncidents(incident_data):

    This function processes binary incident data from a PDF and extracts relevant incident records. It uses the PyPDF library to read the PDF and regular expressions to parse the data into structured information.

    Args:
        incident_data (bytes): Binary data of the PDF file that contains incident information, fetched from the URL.
        
    Returns:
        list: list of dictionaries, where each dictionary represents an individual incident. Each dictionary contains the following keys:
        'Date_Time': The date and time of the incident.
        'Incident Number': A unique identifier for the incident.
        'Location': The location where the incident occurred.
        'Nature': The nature or type of the incident.
        'ORI': The originating agency identifier.

```
### db.py

```
def createdb():

    This function is responsible for creating a fresh SQLite database and initializing a table for storing incident records. If the database already exists, it deletes it before creating a new one.
        
    connection: An SQLite database connection object that can be used for further database operations.

    An SQL command is executed to create a table named incidents. The table contains the following fields:

    incident_time (TEXT): The date and time of the incident.
    incident_number (TEXT): The incident’s unique identifier.
    incident_location (TEXT): The location of the incident.
    nature (TEXT): The type or nature of the incident.
    incident_ori (TEXT): The originating agency identifier.

```
```
def populatedb(conn, incidents):

    This function populates the database with incident records. It inserts data into the incidents table using a list of dictionaries, each representing an incident.

    Args:
        conn (sqlite3.Connection): The database connection object created by createdb().

        incidents (list): A list of dictionaries, where each dictionary represents an incident with fields like 'Date_Time', 'Incident Number', 'Location', 'Nature', and 'ORI'.
        
    Inserting data:
        The incidents list is transformed into a list of tuples, each containing values in the following order: Date_Time, Incident Number, Location, Nature, and ORI.

        The executemany method is used to insert multiple rows into the incidents table. Each tuple is inserted into the table using placeholders (?, ?, ?, ?, ?), corresponding to the five columns.

```
```
def extractIncidents(incident_data):

    This function processes binary incident data from a PDF and extracts relevant incident records. It uses the PyPDF library to read the PDF and regular expressions to parse the data into structured information.

    Args:
        incident_data (bytes): Binary data of the PDF file that contains incident information, fetched from the URL.
        
    Returns:
        list: list of dictionaries, where each dictionary represents an individual incident. Each dictionary contains the following keys:
        'Date_Time': The date and time of the incident.
        'Incident Number': A unique identifier for the incident.
        'Location': The location where the incident occurred.
        'Nature': The nature or type of the incident.
        'ORI': The originating agency identifier.

```

## Bugs and Assumptions

### Assumptions




## Test Cases


### test_db.py


### test_extractincidents.py


### test_incident.py


