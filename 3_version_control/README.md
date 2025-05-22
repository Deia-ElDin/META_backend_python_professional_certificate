# Version Control 

This directory contains all materials, code, and modules for the "Version Control" course, part of the Meta Back-End Developer Professional Certificate.

## Course Overview
This course introduces the fundamentals of version control, a system for tracking and managing changes to code and files. Topics include the purpose and importance of version control in software development, an overview of both centralized and distributed systems, and practical skills using Git and GitHub.

Key concepts covered include creating and cloning repositories, tracking changes, and using essential Git commands such as add, commit, push, pull, branching, and merging. The course also addresses conflict resolution and the use of command-line tools for version control tasks.

## Modules
- **Module 1:** (`Module_1/`) (comming soon)
- **Module 2:** (`Module_2/`) (comming soon)
- **Module 3:** (`Module_3/`) (comming soon)
- **Module 4:** (`Module_4/`) (comming soon)

## Getting Started
1. Make sure you have Docker installed.
2. Navigate to this course directory:
   ```sh
   cd 3_version_control
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