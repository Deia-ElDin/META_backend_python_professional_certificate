# Programming in Python

This repository contains the course materials and exercises for the Programming in Python course. The course is structured into 5 modules, each focusing on different aspects of Python programming.

## Course Structure

### Module 1: Python Fundamentals
- Basic Python syntax and data types
- String manipulation and type casting
- User input handling
- Operators and expressions
- Control flow statements (if-else, match)
- Loops and nested loops

### Module 2: Coming Soon
- To be added

### Module 3: Coming Soon
- To be added

### Module 4: Coming Soon
- To be added

### Module 5: Coming Soon
- To be added

## Getting Started

1. Make sure you have Docker installed on your system
2. Clone this repository
3. Navigate to the course directory (`2_Programming_in_Python`)
4. Run `make all` in the root directory to build and start the container
5. Navigate to the specific module directory (e.g., `Module_1`)
6. Use `make info` to see available commands for that module
7. Use the module-specific commands (e.g., `make run1` for Module_1/python_syntax.py)

## Available Commands

### Course-level commands (in root directory)
- `make all` - Build and start the container (MUST be run first)
- `make info` - Display available commands
- `make clean` - Remove the container
- `make fclean` - Remove the container and image
- `make re` - Remove everything and start fresh
- `make git MSG="your message"` - Commit course-level changes

### Module-level commands (in Module_1 directory)
- `make run1` through `make run11` - Run specific Python scripts
- `make git MSG="your message"` - Commit module-level changes

## Development Environment

The course uses Docker to provide a consistent development environment. The container includes:
- Python 3.x
- All necessary dependencies
- Mounted volume for real-time code changes

## Contributing

Feel free to submit issues and enhancement requests!
