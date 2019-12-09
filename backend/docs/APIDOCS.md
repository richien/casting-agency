# API Reference Document

## Introduction

The Casting Agency application models a company that is responsible for creating movies and managing and assigning actors to those movies.
This API document details the available endpoints for performing these actions.

## Getting Started
- Base url: This API is not currently hosted but can be accessed in a local environment on the following url. `--TODO-- Use the Heroku url`
```
http://localhost:5000/api/v1 `--TODO-- Use the Heroku url`
```
- The API in its current version does not uses Auth0 authentication mechanisms. `--TODO--`

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

- Request Arguments: 
    - `page` integer [optional - defaults to 1]
    - `limit` integer [optional - defaults to 10]

- Sample: ``` curl http://localhost:5000/api/v1/TODO```
```
{}
```

- Response Codes
  - success: 200
  - error: 404
- If there are no actors in the database for the requested page, a `404` error response
  will be returned. Checkout the section on error handling above for the structure of the response.


