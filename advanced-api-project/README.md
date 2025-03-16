# Advanced API Project

Welcome to the **Advanced API Project**! This project is built using Django and Django REST Framework to create a powerful API that can be used for various applications.

## Table of Contents

- [Advanced API Project](#advanced-api-project)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)

## Getting Started

Follow the steps below to set up your development environment and get started with the project.

### Prerequisites

Make sure you have Python and pip installed on your machine.

## Installation

1. **Activate your Virtual Environment**  

Create and activate your virtual environment to keep your project dependencies isolated:
   
```python -m venv djenv``` used to create the virtual environment named djenv

On Windows use `djenv\Scripts\activate` to activate the virtual environment

2. **Install Required Packages**

Install Django and Django REST Framework by running:

```pip install django djangorestframework```

3. **Create the Django Project**
   
Start a new Django project:

```django-admin startproject advanced_api_project .```

4. **Navigate to the Project Directory**
   
Change into the project directory:

```cd advanced_api_project```

5. **Create a Django App**
   
Create a new Django app named api:

```django-admin startapp api```

# Project Structure

Here’s a brief overview of the project structure:

```
advanced_api_project/
│
├── api/                     # Your API application
│   ├── migrations/          # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── advanced_api_project/    # Main project directory
│   ├── __init__.py
|   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py                # Project management script
└── README.md
```
