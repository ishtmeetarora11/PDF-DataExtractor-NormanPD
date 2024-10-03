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

incident_data = fetchIncidents(url): Fetches incident data from the provided URL.

incidents = extractIncidents(incident_data): Extracts and processes incidents from the fetched data.

db = createdb(): Initializes the database.

populatedb(db, incidents):Inserts the extracted incidents into the initialized database.

status(db):Checks or reports the status of the database.

### fetchincidents.py


### extractincidents.py


### db.py


## Bugs and Assumptions


### Assumptions


## Test Cases


### test_db.py


### test_extractincidents.py


### test_incident.py


