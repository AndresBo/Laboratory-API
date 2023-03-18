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

Additional functionality allows ONLY administrators to create, read, update and delete: tests, analyzers and analysts.

## Database system:
The API will use **PostgreSQL** an open-source relational database. 

Advantages of PostgreSQL include:
- Supports Python
- No license cost
- More SQL-compliant when compared to MySQL
- PostgreSQL is an object-relational database offering more sophisticated data types. MySQL is purely relational database

Disadvantages against MySQL 
- MySQL is not an object-relational database, this makes it less complex and easier to manage

## ORM:
Object Relational Mapping (ORM) will bridge the gap between the relational database and the object oriented program in our application. Instead of using SQL to directly interact with our database, an ORM tool can write simpler queries.

For example:
An SQL query like this one: `'SELECT id, name, email FROM users WHERE id = 3'`, in ORM can look like this: `users.GetById(3)`. 

Advantages of using  ORM include:
- Speeds development 
- Handles logic to interact with database
- Improved security. ORM tools can defend against malicious attacks like SQL Injection Vulnerability.

Disadvantages of an ORM:
- Learning ORM tools
- Slower than SQL
- Complex queries may not be possible with ORM and will need SQL
