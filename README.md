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


### db.py


## Bugs and Assumptions


### Assumptions


## Test Cases


### test_db.py


### test_extractincidents.py


### test_incident.py


