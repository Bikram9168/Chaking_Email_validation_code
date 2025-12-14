# Email Validation Program in Python

This project is a simple email validation program written in Python.  
It checks whether the entered email address follows basic email format rules.

## Features
- Checks minimum length of email
- Ensures email starts with an alphabet
- Verifies presence of exactly one `@` symbol
- Validates domain extension like `.com`, `.in`, etc.
- Detects invalid characters and spaces
- Identifies uppercase letters in email
- Displays appropriate error messages for invalid emails

## Validation Rules Used
- Email length must be at least 6 characters
- First character must be an alphabet
- Email must contain exactly one `@`
- Domain must end with `.com`, `.in`, or similar
- No spaces are allowed
- Only alphabets, digits, `_`, `.`, and `@` are permitted

## Concepts Used
- Conditional statements (`if`, `elif`, `else`)
- Loops (`for`)
- String methods (`isalpha()`, `isdigit()`, `isspace()`, `upper()`)
- Counters and flags
- User input handling

## How to Run the Program
1. Make sure Python is installed
2. Clone the repository or download the file
3. Run the program using:

```bash
python email_validation.py
