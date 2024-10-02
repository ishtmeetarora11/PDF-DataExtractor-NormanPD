from pypdf import PdfReader
from io import BytesIO
import re

def extractIncidents(incident_data):
    file_object = BytesIO(incident_data)
    reader = PdfReader(file_object)
    incident_records = []
    for page in reader.pages:
        text = page.extract_text(extraction_mode="layout")
        for line in text.split('\n'):
            line = line.strip()
            
            if line.startswith('Date / Time') or line.startswith('NORMAN POLICE DEPARTMENT') or line.startswith('Daily Incident Summary'):
                continue
            if re.match(r'^\d{1,2}/\d{1,2}/\d{4}', line):
                parts = re.split(r'\s{2,}', line)
                if len(parts) >= 5:  
                    incident = {
                        'Date_Time': parts[0],
                        'Incident Number': parts[1],
                        'Location': parts[2],
                        'Nature': parts[3],
                        'ORI': parts[4]
                    }
                    incident_records.append(incident)
    return incident_records
        