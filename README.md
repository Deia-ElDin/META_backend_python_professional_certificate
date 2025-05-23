# Meta Back-End Developer Professional Certificate

This repository contains all coursework, code, and resources for the Meta Back-End Developer Professional Certificate.

## Certificate Overview
- **Provider:** Meta (Taught by Meta Staff)
- **Level:** Beginner (no prior experience required)
- **Courses:** 9-course series
- **Duration:** 3–6 months

## What You'll Learn
- Python programming, Linux commands, Git, SQL, version control, cloud hosting, APIs, JSON, XML, and more
- Build a portfolio and prepare for technical interviews
- Apply in-demand programming skills to solve real-world problems

## Certificate Structure
Each course in the certificate has its own directory. Each course directory may contain multiple modules, each with its own Makefile for running code and managing module-level commits.

## Courses Included
1. **Introduction to Back-End Development** (19 hours)
    - **Certificate:** [View Certificate](https://coursera.org/share/ca09885a491a1fbb5d2c0cbb2b3c9df6)
    - **Completed on:** May 7, 2025
    - **Grade:** 96.40%
    - **What You'll Learn:**
        - Distinguish between front-end, back-end, and full-stack developers
        - The benefits of working with UI frameworks
        - Create and style a webpage with HTML and CSS
2. **Programming in Python** (45 hours)
    - **Certificate:** [View Certificate](https://coursera.org/share/eb9fac32b66e4b34796d1bff38589b83)
    - **Completed on:** May 22, 2025
    - **Grade:** 99.37%
    - **What You'll Learn:**
        - Foundational programming skills with basic Python Syntax
        - How to use objects, classes and methods
3. **Version Control** (18 hours)
    - **Certificate:** [View Certificate](https://coursera.org/verify/YC08OTGEN44M)
    - **Completed on:** May 23, 2025
    - **Grade:** 100%
    - **What You'll Learn:**
        - Implement Version Control systems
        - Navigate and configure using the command line
        - Use a GitHub repository and create GitHub repositories
        - Manage code revisions
4. **Introduction to Databases for Back-End Development** (27 hours)
5. **Django Web Framework** (45 hours)
6. **APIs** (21 hours)
7. **The Full Stack** (25 hours)
8. **Back-End Developer Capstone** (20 hours)
9. **Coding Interview Preparation** (12 hours)

    


### Example Structure
```
Meta_Back-End_Developer_Professional_Certificate/
├── Makefile # Top-level Makefile (controls all courses)
├── README.md # This file
├── 2_Programming_in_Python/
│ ├── Makefile # Course-level Makefile (builds/starts course container)
│ ├── README.md # Course-level README
│ ├── project.mk # Course-level variables and Docker config
│ └── Module_1/
│   ├── Makefile # Module-level Makefile (runs scripts, module commits)
│ └── ...
└── ... (other courses)
```

## Top-Level Makefile Usage
- `make` or `make all` — Build and start containers for all courses (as they are added)
- `make info` — Show available top-level commands
- `make clean` — Remove all course containers
- `make fclean` — Remove all course containers and images
- `make re` — Remove everything and start fresh
- `make git MSG="your message"` — Commit professional certificate-level changes

## Development Environment
- Uses Docker for a consistent, isolated environment.
- **Each course directory contains its own Makefile to build and run a dedicated Docker container for that course.**
- When you run `make all` at the top level, it will build and start containers for all courses (as they are added).
- Each course's code and modules are mounted into its container for real-time development.
- To work within a course, first ensure its container is running (see below), then use the module-level Makefile commands as needed.

### Running Containers
- **To start all course containers:**  
  From the repository root, run:
  ```sh
  make all
  ```
- **To start a single course container:**  
  From the course directory (e.g., `2_Programming_in_Python`), run:
  ```sh
  make all
  ```
- **To check running containers:**  
  ```sh
  docker ps
  ```
- **To stop and remove all containers and images:**  
  ```sh
  make fclean
  ```

## Contributing
Feel free to submit issues and enhancement requests! 