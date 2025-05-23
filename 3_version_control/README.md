# Version Control 

This directory contains all materials, code, and modules for the "Version Control" course, part of the Meta Back-End Developer Professional Certificate.

## Course Overview
This course introduces the fundamentals of version control, a system for tracking and managing changes to code and files. Topics include the purpose and importance of version control in software development, an overview of both centralized and distributed systems, and practical skills using Git and GitHub.

Key concepts covered include creating and cloning repositories, tracking changes, and using essential Git commands such as add, commit, push, pull, branching, and merging. The course also addresses conflict resolution and the use of command-line tools for version control tasks.

## Modules
- **Module 1: Software Collaboration** (`Module_1/`)  
  Learn about using version control to organize large software projects, explore different version control systems, and understand effective software development workflows.  
  After completing this module, you will be able to:
  - Describe how modern software teams collaborate and work on the same codebase.
  - Understand the importance of proper workflows in version control.
  - Explain the concepts of Continuous Integration (CI), Continuous Delivery, and Continuous Deployment.
  - Differentiate between staging and production environments.

- **Module 2: Command Line** (`Module_2/`)
  Introduction to using the command line in Linux, including common commands for navigating, creating, renaming, and deleting files. Learn to use piping and redirection to automate workflows.  
  After completing this module, you will be able to:
  - Describe what the command line is and how it is used.
  - Traverse your hard drive via the command line.
  - Create, rename, and delete files and folders using Unix commands.
  - Use pipes and redirection.

- **Module 3: Git** (`Module_3/`)
  Develop a strong conceptual understanding of Git, including installing Git, creating repositories, making commits, and working with remote repositories.  
  After completing this module, you will be able to:
  - Outline Git principles.
  - Use a GitHub repository.
  - Describe the steps in a standard GitHub workflow.
  - Create branches and merge sources.
  - Explain how code moves from local development to version control and production.

- **Module 4: Graded Assessment** (`Module_4/`) (coming soon)  
  Apply the skills learned throughout the course in a graded project on GitHub. Reflect on course content and the learning path ahead.  
  After completing this module, you will be able to:
  - Recap all topics covered in the course.
  - Apply your skills in a graded project.

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