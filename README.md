# Hey there! Glad you're here

Welcome to the unofficial Python library for [Abstract API](https://www.abstractapi.com/). This library allows Python developers to use Abstract APIs with Python code. The library currently supports the following APIs by Abstract:

- Exchange Rates API
- IP Geolocation API
- Value added Tax (VAT) API

The name of this library is `abstract-python`

## Key features
The `abstract-python` library is capable of the following:
1. It allows you to send requests to Abstract APIs using Python code. 
2. It performs type validation on each request parameters before requests are sent to the API server. This helps you to manage API credits.
3. It provides an helper variable that allows you to access the list of supported countries for the VAT API. A feature Abstract API doesn't provide
4. It provides an helper variable that allows you to access the list of supported currencies for the Exchange Rates API. A feature Abstract API doesn't provide.


## How it works?
This library wraps the Abstract APIs and their endpoints using a Python class. Each API has a designated Python class which helps to ensure modularity in the project.
The API endpoints are represented with methods within their Parent class. 


## Project structure
- The library utilities are in the `src` folder. 
- The `abstract.py` file contains the code for the library. This is where you can make code-contributions to the library. 
- The `docs` folder contains the library's documentation files. This is where you can make writing-contributions to the library.
The documentation is built with [Mintlify](https://mintlify.com).   

## Getting started
Visit the [documentation](https://rilwanorganization.mintlify.app/introduction) to learn how to use the library in your project.

