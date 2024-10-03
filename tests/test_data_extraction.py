import pytest
from io import BytesIO
from pypdf import PdfReader
from project0 import extractincidents 
import urllib.request 


@pytest.fixture
def sample_pdf_data():
    return b"""
    NORMAN POLICE DEPARTMENT Daily Incident Summary (Public)
    Date / Time    Incident Number    Location    Nature    Incident ORI
    8/1/2024 0:04    2024-00055419    1345 W LINDSEY ST    Traffic Stop    OK0140200
    8/1/2024 0:18    2024-00055420    1820 BEVERLY HILLS ST    Suspicious    OK0140200
    """

def test_extract_incidents(sample_pdf_data):
    headers ={}
    url =("https://www.normanok.gov/sites/default/files/documents/2024-08/2024-08-01_daily_incident_summary.pdf")
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    info = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()

    result = extractincidents.extractIncidents(info)
    
    assert result[0]['Date_Time'] == '8/1/2024 0:04'

    assert result[1]['Date_Time'] == '8/1/2024 0:18'

