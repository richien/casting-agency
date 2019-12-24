[![CircleCI](https://circleci.com/gh/richien/casting-agency.svg?style=svg)](https://circleci.com/gh/richien/casting-agency) [![Coverage Status](https://coveralls.io/repos/github/richien/casting-agency/badge.svg?branch=master)](https://coveralls.io/github/richien/casting-agency?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/66834a00f8fa71d4ab4a/maintainability)](https://codeclimate.com/github/richien/casting-agency/maintainability)
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

#### Third Party Dependencies

##### Auth0

[Auth0](https://auth0.com/) is an identity management platform. The API uses Auth0 to manage authentication and authorization using JSON Web Tokens(JWT) that include Role Based Access Control(RBAC) permission claims.

- Setup Auth0
    - Create an Auth0 account if you dont't have one.
    - Select a unique tenant domain
    - Create a new single page web application
    - Create a new API
        - in API Settings:
            - Enable RBAC
            - Enable Add Permissions in the Access Token
    - Create new API permissions as listed in the `Getting Started` section of the [docs/APIDOCS.md](docs/APIDOCS.md) file.
    - Create new roles as described in the `Getting Started` section of the [docs/APIDOCS.md](docs/APIDOCS.md) file.
- Additional Auth0 setup is required for running the tests locally.
    - From your Auth0 account, create a new machine-machine application called **Executive Producer**.
    - Authorize the machine to use the API you created earlier, giving it all the permissions for the Executive Producer role. The `client ID` and `client Secret` for this machine will need to be added to a `.env` file as decribed in the [Running the server](#running-the-server) section of this document.
    - Repeat the above instructions to create two other machine-machine applications called **Casting Director** and **Casting Assistant**.
    - NOTE: The machine to machine applications are required for the automation of the RBAC test cases. These tests were implemented with the python unittest library. 
##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the PostgreSQL database.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

- [Auth0](https://auth0.com/) is an identity management platform we'll use for authentication and authorization on the backend.

## Database Setup
With Postgres running, create two databases.
- From the `backend` folder, in terminal run:
```bash
createdb agency
```
Create another database that will be used for running tests.
```bash
createdb agency_test
```
Ensure that the user has all privileges access to both databases. If you need additional information on setting up the PostgreSQL databases, checkout the [PostgreSQL tutorial](http://www.postgresqltutorial.com/).

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server:

- Create a `.env` file in the root of the `backend` directory. 
- Copy the contents of `.env.example` into the `.env` file.
- Edit with the database information from the previous section.
- Add the Auth0 machine to machine applications' `Client ID` and `Client Secret`.
- Run the command `source .env` to load the environment variables.
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
