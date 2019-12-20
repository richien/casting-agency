# API Reference Document

## Introduction

The Casting Agency application models a company that is responsible for creating movies and managing and assigning actors to those movies.
This API document details the available endpoints for performing these actions. The API was developed following REST principles.

## Getting Started
- Base url: This API is not currently hosted but can be accessed in a local environment on the following url. `--TODO-- Use the Heroku url`
```
-TODO-- Use the Heroku url
http://localhost:5000/api/v1 
```
- The API in its current version uses Auth0 mechanisms for authentication and authorization. A JWT token should be passed in the request headers using `Authorization Bearer token`. The payload of the JWT token should contain permissions.
- The API uses the  **Auth0 Role Based Access Control** mechanisms for implementing authorization for each endpoint. The following  permissions are currently accepted;
    - `get:actors`
    - `post:actors`
    - `patch:actors`
    - `delete:actors`
    - `get:movies`
    - `post:movies`   
    - `patch:movies`
    - `delete:movies`

- Roles and their corresponding permissions are listed below:
  - **Casting Assistant**: 
    - `get:actors`
    - `get:movies`
  - **Casting Director**: 
    All the permissions of the Casting Assistant as well as;
    - `post:actors`
    - `patch:actors`
    - `patch:movies`
    - `delete:actors`
  - **Executive Producer**: 
    All the permisions of the Casting Director as well as;
    - `post:movies`
    - `delete:movies`

 ## Error Handling
 Errors are returned as JSON objects in the following format:
 ```
 {
    "success": False,
    "error": 404,
    "message": "resource not found"
 }
 ```
 The API will return the following error types when requests fail:
 - 400: bad request
 - 404: resource not found
 - 422: unable to process request 
 - 405: method not allowed
 - 500: internal server error
 - Error codes 401 and 403 are returned for authentication and authorization errors respectively.

## Resource endpoint library

```
GET /actors
```

- General
    - Returns a list of actor objects, the total number of actors in the database and a success value of true.
    - Results are paginated in groups of 10 by default. Include a **page** request argument to choose
        a page number, starting from 1. If no argument is supplied the default page is page 1.
    - You can also optionally specify a **limit** request argument to change the number or returned actors
    in the pagination group.

- Request Arguments: 
    - `page` integer [optional - defaults to 1]
    - `limit` integer [optional - defaults to 10]
- Required Permissions:
    - `get:actors` 

- Sample: ``` curl http://localhost:5000/api/v1/actors?page=1 -H 'Authorization: Bearer token-goes-here'``` `TODO Use the heroku url`
```
{
    "actors": [
        {
            "age": 24,
            "created-at": "2019-12-20T09:24:08.377268",
            "gender": "female",
            "id": 7,
            "name": "Jane Vanfon",
            "updated-at": "2019-12-20T13:13:50.581077"
        },
        {
            "age": 29,
            "created-at": "2019-12-20T09:31:48.060282",
            "gender": "male",
            "id": 9,
            "name": "Peter Stranse",
            "updated-at": "2019-12-20T09:46:39.789014"
        }
    ],
    "success": true,
    "total-actors": 2

```

- Response Codes
  - success: 200
  - error: 404
- If there are no actors in the database for the requested page, a `404` error response
  will be returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
GET /actors/<int:id>
```

- General
    - Returns an actor object with the given ID and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `get:actors`

- Sample: ``` curl http://localhost:5000/api/v1/actors/9 -H "Authorization: Bearer token-goes-here"``` `TODO Use the heroku url`
```
{
    "actor": {
        "age": 29,
        "created-at": "2019-12-20T09:31:48.060282",
        "gender": "male",
        "id": 9,
        "name": "Peter Stranse",
        "updated-at": "2019-12-20T09:46:39.789014"
    },
    "success": true
}
```

- Response Codes
  - success: 200
  - error: 404
- If an actor with the supplied ID does not exist in the database, a `404` error response
  will be returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.
  
```
POST /actors
```

- General
    - Takes a json object containing an actor's name, dob(date of birth - ISO format) and gender in the request body.
    - Returns an actor object and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `post:actors`

- Sample: ```curl -X POST http://localhost:5000/api/v1/actors -H "content-type:application/json" -H "Authorization: Bearer token-goes-here" -d '{"name": "Jane Vanfon", "gender": "female", "dob": "1995-12-14"}'``` `TODO Use the heroku url`
```
{
    "actor": {
        "age": 24,
        "created-at": "2019-12-20T12:22:11.290889",
        "gender": "female",
        "id": 10,
        "name": "Jane Vanfon",
        "updated-at": "2019-12-20T12:22:11.290916"
    },
    "success": true
}
```

- Response Codes
  - success: 201
  - error: 400
- If there are validation errors in the request, a 400 error response is returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
PATCH /actors/<int:id>
```

- General
    - Updates the supplied fields for the actor object with the given ID.
    - Takes a json object containing any of the fields; name, dob(date of birth - ISO format) and gender in the request body.
    - Returns an actor object and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `patch:actors`

- Sample: ```curl -X PATCH http://localhost:5000/api/v1/actors/10 -H "content-type:application/json" -H "Authorization: Bearer token-goes-here" -d '{"name": "Jane Vanfon Matthews"}'``` `TODO Use the heroku url`
```
{
    "actor": {
        "age": 24,
        "created-at": "2019-12-20T12:22:11.290889",
        "gender": "female",
        "id": 10,
        "name": "Jane Vanfon Matthews",
        "updated-at": "2019-12-20T12:27:40.436492"
    },
    "success": true
}
```

- Response Codes
  - success: 200
  - error: 400, 422
- If there are validation errors in the request, a 400 error response is returned.
- If an actor with the supplied ID doesn't exist in the database, a 422 error response is returned.
 Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
DELETE /actors/<int:id>
```

- General
    - Deletes the actor object with the given ID.
    - Returns the ID of the deleted actor object and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `delete:actors`

- Sample: ```curl -X DELETE http://localhost:5000/api/v1/actors/2 -H "Authorization: Bearer token-goes-here"``` `TODO Use the heroku url`
```
{
  "deleted": 2,
  "success": true
}
```

- Response Codes
  - success: 200
  - error: 422
- If an actor with the supplied ID doesn't exist in the database, a 422 error response is returned.
 Checkout the section on [error handling](#error-handling) above for the structure of the error response.


```
GET /actors/<int:id>/movies
```

- General
    - Retrieve an actor's movies.
    - Returns a list of movie objects, the total number of movies in the database and a success value of true, for the
      actor with the given ID.

- Request Arguments: 
    - None

- Required Permissions:
    - `get:movies`

- Sample: ```curl http://localhost:5000/api/v1/actors/9/movies -H "Authorization: Bearer token-goes-here"``` `TODO Use the heroku url`
```
{
    "movies": [
        {
            "created-at": "2019-12-20T12:37:16.868226",
            "id": 12,
            "release-date": "2020-03-01T00:00:00",
            "title": "Elevated",
            "updated-at": "2019-12-20T12:41:22.670044"
        }
    ],
    "success": true,
    "total-movies": 1
}
```

- Response Codes
  - success: 200
  - error: 404
- If there is no actor in the database with the given actor ID, a `404` error response will be returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
GET /movies
```

- General
    - Returns a list of movie objects, the total number of movies in the database and a success value of true.
    - Results are paginated in groups of 10 by default. Include a **page** request argument to choose
        a page number, starting from 1. If no argument is supplied the default page is page 1.
    - You can also optionally specify a **limit** request argument to change the number or returned movies
    in the pagination group.
    - The release date is returned in ISO format.

- Request Arguments: 
    - `page` integer [optional - defaults to 1]
    - `limit` integer [optional - defaults to 10]

- Required Permissions:
    - `get:movies`


- Sample: ``` curl http://localhost:5000/api/v1/movies?page=1 -H "Authorization: Bearer token-goes-here"``` `TODO Use the heroku url`
```
{
    "movies": [
        {
            "created-at": "2019-12-20T12:35:59.496877",
            "id": 11,
            "release-date": "2020-10-10T15:00:00",
            "title": "A Sudden Rise",
            "updated-at": "2019-12-20T12:35:59.496899"
        },
        {
            "created-at": "2019-12-20T12:37:16.868226",
            "id": 12,
            "release-date": "2020-03-23T16:30:00",
            "title": "Distinct Roads",
            "updated-at": "2019-12-20T12:37:16.868620"
        }
    ],
    "success": true,
    "total-movies": 2

```

- Response Codes
  - success: 200
  - error: 404
- If there are no movies in the database for the requested page, a `404` error response
  will be returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
GET /movies/<int:id>
```

- General
    - Retrieves a movie by the movie ID.
    - Returns a movie object with the given ID and a success value of true.
    - The release date is returned in ISO format

- Request Arguments: 
    - None

- Required Permissions:
    - `get:movies`


- Sample: ``` curl http://localhost:5000/api/v1/movies/12 -H "Authorization: Bearer token-goes-here"``` `TODO Use the heroku url`
```
{
    "movie": {
        "created-at": "2019-12-20T12:37:16.868226",
        "id": 12,
        "release-date": "2020-03-23T16:30:00",
        "title": "Distinct Roads",
        "updated-at": "2019-12-20T12:37:16.868620"
    },
    "success": true
}
```

- Response Codes
  - success: 200
  - error: 404
- If a movie with the supplied ID does not exist in the database, a `404` error response
  will be returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
POST /movies
```

- General
    - Adds a movie.
    - Takes a json object containing a movie's title, release-date (in ISO format) in the request body.
    - Returns a movie object and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `post:movies`


- Sample: ```curl -X POST http://localhost:5000/api/v1/movies -H "content-type:application/json" -H "Authorization: Bearer token-goes-here" -d '{"title": "A Sudden Rise", "release-date": "2020-10-10T15:00:00"}'``` `TODO Use the heroku url`
```
{
    "movie": {
        "created-at": "2019-12-20T12:35:59.496877",
        "id": 11,
        "release-date": "2020-10-10T15:00:00",
        "title": "A Sudden Rise",
        "updated-at": "2019-12-20T12:35:59.496899"
    },
    "success": true
}
```

- Response Codes
  - success: 201
  - error: 400
- If there are validation errors in the request, a 400 error response is returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
PATCH /movies/<int:id>
```

- General
    - Updates the supplied fields for the movie object with the given ID.
    - Takes a json object containing any of the fields; title, release-date (in ISO format) in the request body.
    - Returns a movie object and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `patch:movies`


- Sample: ```curl -X PATCH http://localhost:5000/api/v1/movies/12 -H "content-type:application/json" -H "Authorization: Bearer token-goes-here" -d '{"title": "Elevated", "release-date": "2020-03-01"}'``` `TODO Use the heroku url`
```
{
    "movie": {
        "created-at": "2019-12-20T12:37:16.868226",
        "id": 12,
        "release-date": "2020-03-01T00:00:00",
        "title": "Elevated",
        "updated-at": "2019-12-20T12:41:22.670044"
    },
    "success": true
}
```

- Response Codes
  - success: 200
  - error: 400, 422
- If there are validation errors in the request, a 400 error response is returned.
- If a movie with the supplied ID doesn't exist in the database, a 422 error response is returned.
 Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
DELETE /movies/<int:id>
```

- General
    - Deletes the movie object with the given ID.
    - Returns the ID of the deleted movie object and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `delete:movies`


- Sample: ```curl -X DELETE http://localhost:5000/api/v1/movies/9 -H "Authorization: Bearer token-goes-here"``` `TODO Use the heroku url`
```
{
  "deleted": 9,
  "success": true
}
```

- Response Codes
  - success: 200
  - error: 422
- If a movie with the supplied ID doesn't exist in the database, a 422 error response is returned.
 Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
GET /movies/<int:id>/actors
```

- General
    - Returns a list of actor objects, the total number of actors in the database and a success value of true, for the movie with the given ID.

- Request Arguments: 
    - None

- Required Permissions:
    - `get:actors`


- Sample: ```curl http://localhost:5000/api/v1/movies/3/actors -H "Authorization: Bearer token-goes-here"``` `TODO Use the heroku url`
```
{
    "actors": [
        {
            "age": 31,
            "created-at": "2019-12-20T09:24:08.377268",
            "gender": "female",
            "id": 7,
            "name": "Jane Vanfon",
            "updated-at": "2019-12-20T09:24:08.377322"
        },
        {
            "age": 29,
            "created-at": "2019-12-20T09:31:48.060282",
            "gender": "male",
            "id": 9,
            "name": "Peter Stranse",
            "updated-at": "2019-12-20T09:46:39.789014"
        }
    ],
    "success": true,
    "total-actors": 2
}
```

- Response Codes
  - success: 200
  - error: 404
- If there is no movie in the database with the given movie ID, a `404` error response will be returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.

```
POST /movies/<int:id>/actors
```

- General
    - Adds an actor to a movie.
    - Takes a json object containing an actor's ID in the request body.
    - Returns an actor object and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `post:actors`


- Sample: ```curl -X POST http://localhost:5000/api/v1/movies/3/actors -H "content-type:application/json" -H "Authorization: Bearer token-goes-here" -d '{"actor-id": 9}'``` `TODO Use the heroku url`
```
{
    "actor": {
        "age": 29,
        "created-at": "2019-12-20T09:31:48.060282",
        "gender": "male",
        "id": 9,
        "name": "Peter Stranse",
        "updated-at": "2019-12-20T09:46:39.789014"
    },
    "success": true
}
```

- Response Codes
  - success: 201
  - error: 400, 404, 422
- If there are validation errors in the request, a 400 error response is returned.
- If a movie with the given movie ID does not exist, a 404 error response is returned.
- If an actor with the given actor ID does not exist or is already assigned to the movie, a 422 error response is returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.


```
DELETE /movies/<int:id>/actors
```

- General
    - Removes the actor from a movie.
    - Takes a json object containing an actor's ID in the request body.
    - Returns the ID of the removed actor object and a success value of true.

- Request Arguments: 
    - None

- Required Permissions:
    - `delete:actors`


- Sample: ```curl -X DELETE http://localhost:5000/api/v1/movies/3/actors -H "content-type:application/json" -H "Authorization: Bearer token-goes-here" -d '{"actor-id": 4}'``` `TODO Use the heroku url`
```
{
  "deleted": 4,
  "success": true
}
```

- Response Codes
  - success: 200
  - error: 422
- If there are validation errors in the request, a 400 error response is returned.
- If a movie with the given movie ID does not exist, a 404 error response is returned.
- If an actor with the given actor ID does not exist or is not yet assigned to the movie, a 422 error response is returned.
 Checkout the section on [error handling](#error-handling) above for the structure of the error response.