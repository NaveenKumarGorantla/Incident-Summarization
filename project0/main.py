import argparse
import PyPDF2
import tempfile
import sqlite3
import urllib.request
def main(url):


        # Download data
    incident_data = fetchincidents(url)
              # Extract data
    incidents = extractincidents(incident_data)
                    
     # Create new database
    print("Hello")
    db = createdb()
                            
     #Insert data
    populatedb(db, incidents)
                                    
    # Print incident counts
    status(db)

def fetchincidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return data

def extractincidents(data):
    # Write the pdf data to a temp file
    fp = tempfile.TemporaryFile()
    fp.write(data)
    # Set the curser of the file back to the begining
    fp.seek(0)
    # Read the PDF
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    total_pages=pdfReader.getNumPages()
    incidents=[]
    # Get the first page
    for i in range(0,total_pages):
        if(i==0):
            page1 = pdfReader.getPage(i).extractText()
            page1=page1.replace(" \n"," ")
            incident = page1.split('\n')
            incident=incident[5:]
            incident=incident[:-3]
            incidents.extend(incident)
        elif(i==total_pages-1):
            pagelast=pdfReader.getPage(i).extractText()
            pagelast=pagelast.replace(" \n"," ")
            incidents_lastpage=pagelast.split('\n')
            incidents_lastpage=incidents_lastpage[:-2]
            incidents.extend(incidents_lastpage)
        else:
            page=pdfReader.getPage(i).extractText()
            page=page.replace(" \n"," ")
            incident=page.split('\n')
            incident=incident[:-1]
            incidents.extend(incident)
              
    #print(incidents)
    return incidents    

def createdb():
    db='normanpd.db'
    #conn = None
    conn = sqlite3.connect('normanpd.db')
    #conn.isolation_level = None
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS incidents (
                   incident_time TEXT,
                    incident_number TEXT,
                   incident_location TEXT,
                  nature TEXT,
                  incident_ori TEXT ) ''')
    
    conn.commit()
    conn.close()
    return db

def  populatedb(db,incidents):
    incident_data=incidents
    db = 'normanpd.db'
    list_rows = list()
    z=0
    while( z<len(incident_data)):
         list1= list(incident_data[z:z+5])
         list_rows.append(list(incident_data[z:z+5]))
         z+=5
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    #print(list_rows)
    for i in list_rows:
        cur.execute("INSERT into incidents VALUES (?,?,?,?,?)" , (i))
    #sqlquery = 'INSERT into incidents VALUES (?,?,?,?,?)'
    #cur.executemany(sqlquery,list_rows)
    con.commit()
    con.close()

def status(db):
    db= 'normanpd.db'
    con = sqlite3.connect('normanpd.db')
    cur = con.cursor()
    rows =  cur.execute("SELECT nature,COUNT(nature) FROM incidents GROUP BY nature ORDER BY nature")
    for row in rows:
        print(row)


if (__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
            help="Incident summary url.")
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
