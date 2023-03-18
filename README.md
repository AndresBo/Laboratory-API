# Laboratory-API
API webserver project: build a web server for a Laboratory that helps keep track of day-to-day operations.

## Why?
Laboratories report patient data (results and patient details) but often cannot track day-to-day operation data like:
- Who was the analyst who prepared a run (batch of tests)
- What analyzer was used to run a test/request

Often day-to-day data is tracked using paper or at best a spreadsheet. This takes a lot of time and effort and is unreliable. My aim is to build and API that can track this data.

## Functionality:
Core functionality would allow an analyst to:
1. Create a request
2. Read a request
3. Update a request: add tests to request, update request status.
4. Delete a request

Additional functionality allows ONLY administrators to create, read, update and delete: tests, analysers and analysts.

## Database system:
The API will use **PostgreSQL** an open-source relational database. 

Advantages of PostgreSQL include:
- Supports Python
- No licence cost
- More SQL-compliant when compared to MySQL
- PostgreSQL is an object-relational database offering more sophisticated data types. MySQL is purely relational database

Disadvantages against MySQL 
- MySQL is not an object-relational database, this makes it less complex and easier to manage

## ORM:
Object Relational Mapping (ORM)
