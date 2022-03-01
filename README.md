# cs5293sp21-project0

## Name - NAVEEN KUMAR GORANTLA
## Email - Naveen.Kumar.Gorantla-1@ou.edu

## PROJECT SUMMARY: 
To Build a function to collect only incidents data from the regular reports of incidents. The data is hosted on the website of Oklahoma Police Department,
Norman in the form of PDF. In this project we use PyPDF2 Library to extract data from the PDF and python functions to do the following.
                                                                                                                                                                              
1. Download the data from one incident pdf;
2. Extract the fields:
   Date / Time
   Incident Number
   Location
   Nature
   Incident ORI (originating agency identifier)

3. Create a SQLite database to store the data;
4. Insert the data into the database;
5. Print each nature and the number of times it appears

Assumptions: Assuming the the data format in the PDF Report from oklahoma Police Department does not change.

## Running the program- 
Code for the above functionality is available in this Github Repository.

### Command line to Run - pipenv run python project0/main.py --incidents "url"

### - [Sample < url>](https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-03_daily_incident_summary.pdf)

## Required Python Packages to Install
1. PyPDF2   - pipenv install PyPDF2
2. Sqlite   - pipenv install PyPDF2
3. Urllib   - pipenv install PyPDF2
4. Tempfile - pipenv install PyPDF2
5. Argparse - pipenv install PyPDF2

### List of Python Functions used - fetchincidents, extractincidents, createdb, populatedb, status

### fetchincidents- 
This python function takes the url string as an argument and fetch data from the website using urllib.request library to grab one incident pdf data.
The function returns the object data.

### extractincidents-
This python function takes the object data returned from fetchincidents function as an argument. Inside the function we write down the pdf data to 
a temporary file which is created using tempfile library. We set the cursor to the beginning of temporary file and read the pdf using pdf file reader with the help of 
PyPDF2 Library. In order to extract the data from each page we take a count of  total number of pages from the pdf reader and extract text from each page.
We write a condition after extracting text from each page depending on the position of the page. First page and last page has different set of conditions while pages
in between has different. This is done to extract relevant data and exclude data which are not relevant. Each page data extracted is added to a common array named incidents.
This function returns the array of incidents.

### createdb -
we create a database named normanpd.db using sqlite library. After creating the database we create and insert the table named incidents with relevant schema
into the database. This function returns the db file name created.

### populatedb - 
This function takes the db filename and the incidents data array returned from extractincidents function as an argument.
We group and separate every five records into a list from the start of the array and Append each group list into a separate list named list_rows. Connecting to
normanpd.db database created, We iterate over the the list_rows and insert the values from each item list into the table incidents created in the database.

### status- 
This function displays the nature of incidents and count of nature of incidents by running the sqlquery using sqlite connection to database. 
 

    







