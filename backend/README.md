# Casting Agency Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PostgreSQL

Instructions to install PostgreSQL on your platform can be found in the official [PostgreSQL tutorial](http://www.postgresqltutorial.com/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the PostgreSQL database.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup
From within the PostgreSQL shell, run the following commands to create the following databases
`-TODO- Running migrations? OR Restore Database from agency.sql file?`
```bash
CREATE DATABASE agency
```
Create another database that will be used for running tests.
```bash
CREATE DATABASE agency_test
```
Ensure that the user has all privileges access to both databases. If you need additional information on setting up the PostgreSQL databases, checkout the [PostgreSQL tutorial](http://www.postgresqltutorial.com/).

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server:

- Create a `.env` file in the root of the `backend` directory. 
- Copy the contents of `.env.example` into the `.env` file and edit with the database information from the previous section.
- Run the command `source .env` to load the environment variables
- Run the tests `pytest`. If the tests all pass, then the setup was successfull.
- To run the application on `http://localhost:5000`, execute:

```bash
flask run
```

## Testing
To run the tests with coverage, run this command from within the `backend` folder.
```
pytest --cov
```
## API Documentation.
The documentation for the Casting Agency API are available at in the [docs/APIDOCS.md](docs/APIDOCS.md) file.
