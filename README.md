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
This API will use **SQLAlchemy ORM**.

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

## ERD:
![trace_elements](https://user-images.githubusercontent.com/85352176/226087292-a4bbba8c-b124-47f1-a3a9-435b11383406.png)

## Models:
Laboratory-API has five models: Analyst, Analyzer, Request, Test and Request_test.

The following list shows the Name of the **Model** and its attributes with **(fk)** added for foreign keys:
- **Analyst** (*id*, email, password, admin)
- **Analyzer**(*id*, name, brand, model, year)
- **Test**(*id*, name)
- **Request**(*id*, date, status, analyst_email **(fk)**, analyzer_email **(fk)**)
- **Request_test**(*id*, request_id **(fk)**, test_name **(fk)**)

### Relationships:
- One Analyst can have many Requests - One Request can have only one Analyst. This is a one-to-many relationship.
- One Analyzer can have many Requests assigned - One Request can be assigned to only one Analyzer. A one-to-many relationship.
- One Test can be on many Requests - One Request can have many Tests. This is a many-to-many relationship that is handled by the Request_test Model.

## Endpoints:

### Requests:

These collection of endpoints are the core of our API. It allows an authenticated user to create a new request, delete a request by entering the id, update a request using the id and adding tests to a existing request using the id of the request. 

- GET localhost:5000/requests/
- POST localhost:5000/requests/
- DELETE localhost:5000/requests/id/
- PUT localhost:5000/requests/id/
- POST localhost:5000/requests/addtest/id/

### User Authentication:

These endpoints allow an existing user to login using their email and password. Also allow an admin to create new users.

- GET localhost:5000/analysts/
- POST localhost:5000/analysts/login
- POST localhost:5000/analysts/register

### Tests:

These endpoints provide available tests information and allow an admin user to create and delete tests.

- GET localhost:5000/tests/
- POST localhost:5000/tests/
- DELETE localhost:5000/tests/name/

### Analyzer:

These endpoints provide analyzer information and allow and admin to create and delete analyzers. 
- GET localhost:5000/analysers/
- POST localhost:5000/analysers/
- DELETE localhosts:5000/analysers/name/
