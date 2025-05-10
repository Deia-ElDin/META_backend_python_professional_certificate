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

### Example Structure
```
Meta_Back-End_Developer_Professional_Certificate/
├── Makefile                # Professional certificate-level Makefile
├── common.mk               # Shared variables and rules
├── README.md               # This file
├── 2_Programming_in_Python/
│   ├── Makefile            # Course-level Makefile
│   ├── README.md           # Course-level README
│   └── Module_1/
│       ├── Makefile        # Module-level Makefile
│       └── ...
└── ... (other courses)
```

## Top-Level Makefile Usage
- `make` or `make all` — Build the Docker image, clean and run the container, and show info
- `make info` — Show available top-level commands
- `make clean` — Remove the container
- `make fclean` — Remove the container and image
- `make re` — Remove everything and start fresh
- `make git MSG="your message"` — Commit professional certificate-level changes

## Development Environment
- Uses Docker for a consistent, isolated environment
- All course and module directories are mounted into the container for real-time development

## Contributing
Feel free to submit issues and enhancement requests! 