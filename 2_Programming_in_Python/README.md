# Programming in Python (Meta Back-End Developer Professional Certificate)

This directory contains all materials, code, and modules for the "Programming in Python" course, part of the Meta Back-End Developer Professional Certificate.

## Course Overview
This course covers the fundamentals of Python programming, including syntax, data types, control flow, user input, and more. It is organized into modules, each focusing on a specific topic or set of skills.

## Modules
- **Module 1: Python Fundamentals**
  - Basic Python syntax and data types
  - String manipulation and type casting
  - User input handling
  - Operators and expressions
  - Control flow statements (if-else, match)
  - Loops and nested loops
- **Module 2:** Coming Soon
- **Module 3:** Coming Soon
- **Module 4:** Coming Soon
- **Module 5:** Coming Soon

## Getting Started
1. Make sure you have Docker installed and the professional certificate container is running (see the top-level README).
2. Navigate to this course directory:
   ```sh
   cd 2_Programming_in_Python
   ```
3. Use the course-level Makefile for course-level git commits and info:
   - `make info` — Show available course-level commands
   - `make git MSG="your message"` — Commit course-level changes
4. To work on a specific module, navigate to its directory and use its Makefile for running scripts and module-level commits.

## Course-Level Makefile Usage
- `make info` — Show available course-level commands
- `make git MSG="your message"` — Commit course-level changes

## Module-Level Makefile Usage
- `make info` — Show available module-level commands
- `make run1`, `make run2`, ... — Run specific Python scripts in the module
- `make git MSG="your message"` — Commit module-level changes

## Development Environment
- All code is run inside the Docker container for consistency and reproducibility.
- The course and its modules are mounted into the container for real-time development.

## Contributing
Feel free to submit issues and enhancement requests!
