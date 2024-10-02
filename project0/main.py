import argparse
from fetchincidents import fetchIncidents
from extractincidents import extractIncidents
from db import createdb, populatedb, status

def main(url):

    incident_data = fetchIncidents(url)

    incidents = extractIncidents(incident_data)
	
    db = createdb()
	
    populatedb(db, incidents)
	
    status(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)