# Project Support

### Introduction

Todo List is an open source project that enable users manage users tasks and also keep track of their progress.

### Project Support Features

* Private (authenticated) users can access all tasks on the platform.
* Private (authenticated) users can view details of a single task.
* Private (authenticated) users can create a task on the platform.
* Private (authenticated) users can delete a task on the platform.
* Private (authenticated) users can update a task on the platform.

### Installation Guide

* Clone this repository [here](https://github.com/careercraftuz/TodoList.git).
* The develop branch (`dev`) is the most stable branch at any given time, ensure you're working from it.
* Run pip install to install all dependencies.
* migrate the database using `python manage.py migrate` command.

### Usage

* Run the application using `python manage.py runserver` command.
* Access the endpoints specified below on your browser or postman.

### Available types

* you can find the available types [here](types.md).

### API Endpoints

user authentication endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /api/login/ | Login a user |
| POST | /api/logout/ | Logout a user |
| POST | /api/register/ | Register a user |

todo task endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /api/tasks/ | Get all todo tasks |
| GET | /api/tasks/<int:id> | Get a todo task by id |
| POST | /api/tasks/<int:id>/delete | Delete a todo task by id |
| POST | /api/tasks/<int:id>/update | Update a todo task by id |
| POST | /api/create-task/ | Create a todo task |

### API Documentation

* you can find the API documentation [here](api-docs.md).

### Technologies Used

* [Django](https://docs.djangoproject.com/) This is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Django Rest Framework](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [Sqlite](https://www.sqlite.org/index.html) SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
* [Python](https://www.python.org/) Python is an interpreted, high-level, general-purpose programming language.
* [Postman](https://www.postman.com/) Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster.

### Current Comtributors

<a href="https://github.com/carecraftuz/TodoList/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=carecraftuz/TodoList"/>
</a>
