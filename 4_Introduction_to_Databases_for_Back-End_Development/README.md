# Introduction to Databases for Back-End Development

This directory contains all materials, code, and modules for the "Introduction to Databases for Back-End Development" course, part of the Meta Back-End Developer Professional Certificate.

## Course Overview
This course covers the fundamentals of databases, including SQL, database design, CRUD operations, and more. You'll learn about database basics, SQL syntax, data manipulation, and proper database design principles. The course provides hands-on experience with creating, managing, and querying databases using SQL.

## Modules
- **Module 1: Introduction to Databases** (`Module_1/`)  
  Receive an introduction to databases, database engineering careers, and essential database concepts. Learn about SQL basics and explore how databases work and their structure.  
  After completing this module, you will be able to:
  - Explain what a database is and what it's used for
  - Explain how data is related in a database and how tables organize data
  - Differentiate between types of databases and keys
  - Apply SQL syntax to create SQL commands
  - Identify potential career paths in database engineering
  - Apply best practices for successful course completion

- **Module 2: Create, Read, Update and Delete (CRUD) Operations** (`Module_2/`)  
  Master SQL data types and fundamental CRUD operations. Learn how to work with different types of data and manipulate database content through hands-on exercises.  
  After completing this module, you will be able to:
  - Differentiate between SQL data types
  - Work with numeric data, string data, and default values
  - Create and read records and tables in an existing database
  - Update and delete records in an existing database
  - Create databases and tables using SQL statements
  - Populate tables with data using SQL statements

- **Module 3: SQL Operators and sorting and filtering data** (`Module_3/`)  
  Explore SQL operators and learn advanced techniques for data manipulation. Master various clauses for sorting and filtering data through practical demonstrations and exercises.  
  After completing this module, you will be able to:
  - Explain how SQL operators are used within a database
  - Use SQL arithmetic and comparison operators
  - Sort and filter data in an existing database
  - Work with ORDER BY, WHERE, and SELECT DISTINCT clauses
  - Apply different clauses to manipulate database data
  - Execute practical database operations using various clauses

- **Module 4: Database design** (`Module_4/`)  
  Learn the principles of database design, including schema creation, table relationships, and normalization concepts.  
  After completing this module, you will be able to:
  - Describe how tables are structured in a database
  - Differentiate between types of database schema
  - Define different types of keys in a database
  - Maintain data integrity and relationships through the use of keys
  - Define relationships between entities in a database
  - Understand database normalization and normal forms

- **Module 5: Graded Assessment** (`Module_5/`)  
  Review and demonstrate your mastery of database concepts through comprehensive assessment.  
  After completing this module, you will be able to:
  - Recap all topics covered in the course
  - Identify your strengths in database management
  - Target areas for further study and improvement
  - Apply your knowledge in practical scenarios

## Getting Started
1. Make sure you have Docker installed.
2. Navigate to this course directory:
   ```sh
   cd 4_Introduction_to_Databases_for_Back-End_Development
   ```
3. Start the course container:
   ```sh
   make all
   ```
4. To work on a specific module, navigate to its directory (e.g., `Module_1/`) and use its Makefile for running scripts and module-level commits.

## Course-Level Makefile Usage
- `make all` — Build, clean, and run the container for this course
- `make info` — Show available course-level commands
- `make clean` — Remove the course container
- `make fclean` — Remove the course container and image
- `make re` — Remove everything and start fresh
- `make git MSG="your message"` — Commit course-level changes

## Module-Level Makefile Usage
- `make info` — Show available module-level commands
- `make run1`, `make run2`, ... — Run specific Python scripts in the module
- `make git MSG="your message"` — Commit module-level changes

## Development Environment
- All code for this course runs inside a dedicated Docker container for consistency and reproducibility.
- The course directory (including all modules) is mounted into the container at `/app` for real-time development.
- Use the course-level Makefile to build, clean, and run the container for this course.
- Before running module-level commands (like `make run1`), ensure the course container is running:
  ```sh
  make all
  ```
- If you see an error about the container not running, run `make all` in the course directory to start it. 

## Contributing
Feel free to submit issues and enhancement requests!