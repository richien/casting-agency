# API Reference Document

## Introduction

The Casting Agency application models a company that is responsible for creating movies and managing and assigning actors to those movies.
This API document details the available endpoints for performing these actions.

## Getting Started
- Base url: This API is not currently hosted but can be accessed in a local environment on the following url. `--TODO-- Use the Heroku url`
```
-TODO-- Use the Heroku url
http://localhost:5000/api/v1 
```
- The API in its current version uses Auth0 authentication mechanisms. `--TODO--`

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

## Resource endpoint library

```
GET /actors
```

- General
    - Returns a list of actor objects, the total number of actors in the database and a success value of true.
    - Results are paginated in groups of 10 by default. Include a **page** request argument to choose
        a page number, starting from 1. If no argument is supplied the default page is page 1.
    - You can also optionally specify a **limit** request argument to change the number or returned questions
    in the pagination group.

- Request Arguments: 
    - `page` integer [optional - defaults to 1]
    - `limit` integer [optional - defaults to 10]

- Sample: ``` curl http://localhost:5000/api/v1/actors?page=1``` `TODO Use the heroku url`
```
{
  "actors": [
    {
      "age": 23,
      "gender": "Male",
      "id": 1,
      "name": "James Henry Jones"
    }
  ],
  "success": true,
  "total_actors": 1
}
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

- Sample: ``` curl http://localhost:5000/api/v1/actors/1``` `TODO Use the heroku url`
```
{
  "actor": {
    "age": 23,
    "gender": "Male",
    "id": 1,
    "name": "James Henry Jones"
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
    - Takes a json object containing an actor's name, age and gender in the request body.
    - Returns an actor object and a success value of true.

- Request Arguments: 
    - None

- Sample: ```curl -X POST http://localhost:5000/api/v1/actors -H "content-type:application/json" -d '{"name": "Jane Vanfon", "gender": "female", "age": 28}'``` `TODO Use the heroku url`
```
{
  "actor": {
    "age": 28,
    "gender": "female",
    "id": 2,
    "name": "Jane Vanfon"
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
    - Takes a json object containing any of the fields; name, age and gender in the request body.
    - Returns an actor object and a success value of true.

- Request Arguments: 
    - None

- Sample: ```curl -X PATCH http://localhost:5000/api/v1/actors/2 -H "content-type:application/json" -d '{"name": "Jane Vanfon Matthews"}'``` `TODO Use the heroku url`
```
{
  "actor": {
    "age": 28,
    "gender": "female",
    "id": 2,
    "name": "Jane Vanfon Matthews"
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

- Sample: ```curl -X DELETE http://localhost:5000/api/v1/actors/2``` `TODO Use the heroku url`
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
GET /movies
```

- General
    - Returns a list of movie objects, the total number of movies in the database and a success value of true.
    - Results are paginated in groups of 10 by default. Include a **page** request argument to choose
        a page number, starting from 1. If no argument is supplied the default page is page 1.
    - You can also optionally specify a **limit** request argument to change the number or returned questions
    in the pagination group.
    - The release date is retuned in ISO format.

- Request Arguments: 
    - `page` integer [optional - defaults to 1]
    - `limit` integer [optional - defaults to 10]

- Sample: ``` curl http://localhost:5000/api/v1/movies?page=1``` `TODO Use the heroku url`
```
{
  "movies": [
    {
      "id": 1,
      "release-date": "2020-12-11T00:00:00",
      "title": "The Hatchet"
    }
  ],
  "success": true,
  "total_movies": 1
}
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
    - Returns an movie object with the given ID and a success value of true.
    - The release date is retuned in ISO format

- Request Arguments: 
    - None

- Sample: ``` curl http://localhost:5000/api/v1/movies/1``` `TODO Use the heroku url`
```
{
  "movie": {
    "id": 1,
    "release-date": "2020-12-11T00:00:00",
    "title": "The Hatchet"
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
    - Takes a json object containing an actor's name, age and gender in the request body.
    - Returns an actor object and a success value of true.

- Request Arguments: 
    - None

- Sample: ```curl -X POST http://localhost:5000/api/v1/movies -H "content-type:application/json" -d '{"title": "A Sudden Rise", "release-date": "2020-10-10T15:00:00"}'``` `TODO Use the heroku url`
```
{
  "movie": {
    "id": 9,
    "release-date": "2020-10-10T15:00:00",
    "title": "A Sudden Rise"
  },
  "success": true
}
```

- Response Codes
  - success: 201
  - error: 400
- If there are validation errors in the request, a 400 error response is returned.
Checkout the section on [error handling](#error-handling) above for the structure of the error response.