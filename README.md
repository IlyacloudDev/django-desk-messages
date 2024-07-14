# Django Desk Messages

[Read in Russian](README_ru.md)

---

Desk Messages is an internet resource for an MMORPG fan server.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running](#running)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Project Description

This project is a message management system (such as user inquiries or technical requests) within a Django web application. It includes functionality for creating, viewing, updating, and deleting messages in a support system.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/IlyacloudDev/django-desk-messages.git
    ```
   
2. Navigate into the project directory:
    ```sh
    cd django-desk-messages
    ```
   
3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
   
4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Apply database migrations:
    ```sh
    python manage.py migrate
    ```
   
2. Create a superuser to access the Django admin panel:
    ```sh
    python manage.py createsuperuser
    ```
   Follow the prompts to create an administrator account.

## Running

Start the Django development server with the following command:
```sh
python manage.py runserver
```
The project will be available at http://localhost:8000/


## Usage
1. Navigate to the main application page:
- http://localhost:8000/


2. Register or log in using administrator credentials.


3. Create, view, update, and delete messages through the web application interface.


4. Use the Django admin interface to manage users and messages:
- http://localhost:8000/admin/


## Dependencies
 requirements.txt:
   ```python
    amqp==5.2.0

    asgiref==3.8.1

    async-timeout==4.0.3

    billiard==4.2.0

    celery==5.4.0

    click==8.1.7

    click-didyoumean==0.3.1

    click-plugins==1.1.1

    click-repl==0.3.0

    colorama==0.4.6

    Django==5.0.6

    django-allauth==0.63.1

    django-ckeditor==6.7.1

    django-filter==24.2

    django-js-asset==2.2.0

    kombu==5.3.7

    prompt-toolkit==3.0.43

    python-dateutil==2.9.0.post0

    redis==5.0.4

    six==1.16.0

    sqlparse==0.5.0

    typing_extensions==4.11.0

    tzdata==2024.1

    vine==5.1.0

    wcwidth==0.2.13
   ```


---
# Happy Using!
