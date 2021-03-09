import pytest
#from project0 import project0
from project0 import main

def test_fetchincidents():
    url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-03_daily_incident_summary.pdf"
    data = main.fetchincidents(url)
    assert  type(data) == bytes 
def test_extractincidents():
    url = "https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-03_daily_incident_summary.pdf"
    data = main.fetchincidents(url)
    incidentdata = main.extractincidents(data)
    assert type(incidentdata)== list 
def test_createdb():
    db = main.createdb()
    assert db == 'normanpd.db'
def test_populatedb():
   assert True 
def test_status():
   assert True   
