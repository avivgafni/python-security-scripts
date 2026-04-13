# python-security-scripts
Python projects related to cybersecurity
# Python Security Scripts

A collection of beginner-friendly Python tools focused on fundamental cybersecurity concepts and secure coding practices.
These projects demonstrate practical skills in input validation, data handling, and basic encryption techniques using simple command-line interfaces.

---

## Projects Overview

### Password Strength Checker

A command-line tool that evaluates password strength based on common security standards.

**Key Features**

* Enforces minimum length (12+ characters)
* Checks for:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Provides clear feedback on missing requirements
* Re-prompts user until a strong password is created

**Skills Demonstrated**

* Conditional logic (`if/elif/else`)
* Loops and input validation
* String handling and pattern checking
* Basic security principles (password policies)

**How to Run**

```bash
cd password_checker
python password_checker.py
# or
py password_checker.py
```

---

### Text Security Toolkit

A simple command-line toolkit for encoding and basic encryption operations.

**Key Features**

* Caesar Cipher:

  * Encrypt and decrypt text
  * Preserves letter case
* Base64:

  * Encode and decode text
* Menu-driven interface
* Basic error handling for user input

**Skills Demonstrated**

* Functions and modular design
* Control flow and menu systems
* String manipulation (`ord()`, `chr()`)
* Working with bytes and encoding (Base64)
* Foundational cryptography concepts

**How to Run**

```bash
cd text_security_toolkit
text_security_toolkit.py
# or
py text_security_toolkit.py
```

---

## Technologies Used

* Python 3
* Standard libraries (`string`, `base64`)

---

## Purpose

This repository is part of my transition into cybersecurity, building hands-on skills through practical labs and scripting.
It reflects a focus on secure coding, problem solving, and applying foundational security concepts in real-world scenarios.

---

## Future Improvements

* Add password entropy scoring
* Expand encryption methods (e.g. Vigenère cipher)
* Implement file input/output support
* Improve error handling and input validation
* Optional GUI version for usability

---

Author

Aviv Gafni, PhD

