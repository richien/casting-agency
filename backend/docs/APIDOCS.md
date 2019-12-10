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
    - Returns a list of actor objects.
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
  will be returned. Checkout the section on [error handling](#error-handling) above for the structure of the response.
  


