# Django Web Framework

This directory contains all materials, code, and modules for the "Django Web Framework" course, part of the Meta Back-End Developer Professional Certificate.

## Course Overview

Use the Django web framework to build, secure, and administer a web server. Create, design, and configure a web app using Django in line with best practices. You will work with models, views, templates, URL routing, forms, and basic security.

## What You'll Learn

- Design a Django web application using Python, HTML, and CSS
- Implement the HTTP request–response cycle with views, routes, and templates
- Model application data with Django ORM, run migrations, and query data
- Use the Django Template Language (DTL), template inheritance, and static files
- Create forms and handle user input; apply common security best practices

## Modules

- **Module 1: Introduction to Django** (`Module_1/`)

  - Install and set up Django, create a project and apps, understand settings, URLs, and development server basics

- **Module 2: Views** (`Module_2/`)

  - Request/response lifecycle, URL patterns, function‑based vs class‑based views, basic forms and handlers

- **Module 3: Models** (`Module_3/`)

  - Defining models and relationships, migrations, Django admin, querying with the ORM

- **Module 4: Templates** (`Module_4/`)

  - DTL syntax, context, template inheritance, includes, static files, rendering forms

- **Module 5: Course summary and graded project assessment** (`Module_5/`)
  - Bring the pieces together in a small project; review and assessment

## Getting Started

1. Make sure you have Docker installed.
2. Navigate to this course directory:
   ```sh
   cd 5-Django-Web-Framework
   ```
3. Start the course container:
   ```sh
   make all
   ```
4. Work inside module folders (e.g., `Module_1/`) and use their Makefiles for module‑level tasks.

## Course-Level Makefile Usage

- `make all` — Build, clean, and run the container for this course
- `make info` — Show available course-level commands
- `make clean` — Remove the course container
- `make fclean` — Remove the course container and image
- `make re` — Remove everything and start fresh
- `make git MSG="your message"` — Commit course-level changes

## Module-Level Makefile Usage

- `make info` — Show available module-level commands
- `make run1`, `make run2`, ... — Run module scripts/commands
- `make git MSG="your message"` — Commit module-level changes

## Development Environment

- Code runs inside a dedicated Docker container for consistency.
- The course directory is mounted into the container at `/app` for real-time development.
- Ensure the course container is running before module tasks:
  ```sh
  make all
  ```

## Contributing

Feel free to submit issues and enhancement requests!
