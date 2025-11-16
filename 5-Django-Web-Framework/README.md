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

  - Overview of Django, where it’s used, and how projects/apps fit together. Environment setup (VS Code, Python). Create a Django project and app using `django-admin` and `manage.py`. Understand the MVT pattern, DRY principles, and Django’s project structure.
  - After completing this module, you will be able to:
    - Differentiate between an app and project structure
    - Use basic commands with `django-admin` and `manage.py`
    - Create an app inside an existing project using the correct structure
    - Use the MVT framework to ensure reusability of code
    - Apply DRY principles to organize your code

- **Module 2: Views** (`Module_2/`)

  - Build views that process HTTP requests and return responses. Work with request/response objects, HTTP methods (GET, PUT, POST, DELETE), regex URL patterns and URL routing. Handle errors at HTTP, view logic, and view levels. Explore and reuse class‑based views.
  - After completing this module, you will be able to:
    - Create views and view logic that process basic HTTP requests
    - Use the request and response objects for common operations
    - Differentiate parameters and how they map to HTTP methods
    - Use regular expressions to create URL patterns and map URLs to views
    - Handle errors at the HTTP, view logic, and view levels
    - Use class‑based views and reuse them across a project

- **Module 3: Models** (`Module_3/`)

  - Work with the Django ORM: create models, run and apply migrations, and query data using the QuerySet API. Use the Django admin to manage users, groups, and permissions. Create forms and bind data with the Form API. Set up a MySQL database for your app.
  - After completing this module, you will be able to:
    - Create models and apply migrations using best practices
    - Use the QuerySet API to interact with the database
    - Create forms and bind data using the Form API
    - Manage users, groups, and permissions in the Django admin
    - Configure a MySQL database for your Django app

- **Module 4: Templates** (`Module_4/`)

  - Create templates and use the Django Template Language (DTL) to generate HTML. Work with template inheritance, includes, and static files. Integrate third‑party libraries. Intro to debugging and testing in Django.
  - After completing this module, you will be able to:
    - Create templates and use the template language to create markup
    - Use templating to generate HTML and build reusable layouts
    - Work effectively with templates and supporting assets

- **Module 5: Graded Assessment** (`Module_5/`)
  - Build a small Django site (e.g., Little Lemon prototype), then complete the final graded assessment and reflect on the course.
  - After completing this module, you will be able to:
    - Synthesize your Django skills to create a functional website
    - Reflect on learning and plan next steps

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
