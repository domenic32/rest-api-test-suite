# REST API Automated Test Suite

A modular API test automation framework built with **Python**, **pytest**, and **requests**. This repository demonstrates automated testing strategies against RESTful endpoints, including response validation, schema assertions, status code checks, and negative test scenarios.

## Features
- **Status Code & Header Validation:** Ensures endpoints respond with standard HTTP codes and correct content-type headers.
- **JSON Schema Verification:** Validates key structure and data types within JSON payloads.
- **HTTP Method Support:** Automated coverage for `GET` and `POST` endpoints.
- **Negative Testing:** Validates proper error handling (e.g., `404 Not Found`) on bad requests.

## Tech Stack
- **Python 3.10+**
- **pytest** (Test execution framework)
- **requests** (HTTP client library)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/api-test-suite.git](https://github.com/yourusername/api-test-suite.git)
   cd api-test-suite
