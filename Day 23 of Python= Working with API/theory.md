🔹 What is an API?

An API (Application Programming Interface) allows different software applications to communicate with each other.
👉 Example:

When you check weather in an app, it gets data from a weather API.

🔹 What is REST API?

A REST API uses HTTP methods:

GET → Fetch data
POST → Send data
PUT → Update data
DELETE → Remove data

🔹  Types of APIs

1. Web APIs

Used over the internet using HTTP protocol.
👉 Most commonly used in Python.

2. Library APIs

Functions provided by libraries (like Python’s built-in modules).

3. Operating System APIs

Allow interaction with OS (file handling, memory, etc.)

🔹  What is an Endpoint?

An endpoint is a specific URL where an API can be accessed.

👉 Example:

https://jsonplaceholder.typicode.com/posts
posts → endpoint
It returns list of posts

🔹  API Request and Response

✔ Request:
Sent by client (your Python program)

✔ Response:
Returned by server (data + status code)

🔹  Python Library for APIs → requests

The requests library is used to send HTTP requests easily.

✔ Features:

Simple syntax
Supports all HTTP methods
Handles JSON easily

🔹  Working of API in Python

Steps:

Import requests
Define API URL
Send request
Receive response
Convert to JSON
Extract required data

🔹 Headers and Parameters
✔ Headers

Provide additional information (like authentication)

✔ Parameters

Used to send extra data in URL

👉 Example:

?city=Delhi&units=metric

🔹  Authentication in APIs

Some APIs require authentication to access data.

Types:

API Key
Token
OAuth

👉 Example:

api_key=12345

🔹  Error Handling in APIs

Errors may occur due to:

Wrong URL
No internet
Server issue

👉 Python handles using:

try-except
response.status_code

🔹  Advantages of APIs

Fast data exchange
Easy integration
Automation
Real-time data access

🔹  Limitations of APIs

Dependency on server
Security risks
Rate limits
Requires internet

