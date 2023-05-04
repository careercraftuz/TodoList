# Project Support

### Introduction

Todo List is an open source project that enable users manage users tasks and also keep track of their progress.

### Project Support Features

* Public (non-authenticated) users can access all tasks on the platform.
* Public (non-authenticated) users can view details of a single task.
* Public (non-authenticated) users can create a task on the platform.
* Public (non-authenticated) users can delete a task on the platform.
* Public (non-authenticated) users can update a task on the platform.

### Installation Guide

* Clone this repository [here](https://github.com/careercraftuz/TodoList.git).
* The develop branch (`dev`) is the most stable branch at any given time, ensure you're working from it.
* Run pip install to install all dependencies.
* migrate the database using `python manage.py migrate` command.

### Usage

* Run the application using `python manage.py runserver` command.
* Access the endpoints specified below on your browser or postman.

### API Endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /api/tasks/ | Get all todo tasks |
| GET | /api/tasks/<int:id> | Get a todo task by id |
| POST | /api/tasks/<int:id>/delete | Delete a todo task by id |
| POST | /api/tasks/<int:id>/update | Update a todo task by id |
| POST | /api/create-task/ | Create a todo task |

### Technologies Used

* [Django](https://docs.djangoproject.com/) This is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Django Rest Framework](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [Sqlite](https://www.sqlite.org/index.html) SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
* [Python](https://www.python.org/) Python is an interpreted, high-level, general-purpose programming language.
* [Postman](https://www.postman.com/) Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster.

### Author

* **[Career Craft Contributors](https://github.com/careercraftuz/TodoList/graphs/contributors)**

## API Documentation Details

### GET /api/tasks/

get all todo tasks

#### Response

```json
{
    "result": [
        {
            "id": 1,
            "name": "task 01",
            "description": "task description",
            "status": false,
            "created": "2023-05-04T05:07:40.069249Z",
            "updated": "2023-05-04T05:07:40.069285Z"
        }
    ]
}
```

response attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| id | int | task id |
| name | string | task name |
| description | string | task description |
| status | bool | task status |
| created | datetime | task created time |
| updated | datetime | task updated time |

### GET /api/tasks/<int:id>

get a todo task by id

#### Response

```json
{
    "id": 1,
    "name": "task 01",
    "description": "task description",
    "status": false,
    "created": "2023-05-04T05:07:40.069249Z",
    "updated": "2023-05-04T05:07:40.069285Z"
}
```

response attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| id | int | task id |
| name | string | task name |
| description | string | task description |
| status | bool | task status |
| created | datetime | task created time |
| updated | datetime | task updated time |

### POST /api/tasks/<int:id>/delete

delete a todo task by id

#### Request

resquest url params:

| Attribute | Type | Description |
| --- | --- | --- |
| id | int | task id |

#### Response

```json
{
    "result": "Task deleted"
}
```

### POST /api/tasks/<int:id>/update

update a todo task by id

#### Request

resquest url params:

| Attribute | Type | Description |
| --- | --- | --- |
| id | int | task id |

request body:

```json
{
    "name": "task 01",
    "description": "task description",
    "status": false
}
```

request body attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| name | string | task name |
| description | string | task description |
| status | bool | task status |

#### Response

```json
{
    "result": {
        "id": 1,
        "name": "task 01",
        "description": "task description",
        "status": false,
        "created": "2023-05-04T05:07:40.069249Z",
        "updated": "2023-05-04T05:07:40.069285Z"
    }
}
```

response attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| id | int | task id |
| name | string | task name |
| description | string | task description |
| status | bool | task status |
| created | datetime | task created time |
| updated | datetime | task updated time |

### POST /api/create-task/

create a todo task

#### Request

request body:

```json
{
    "name": "task 01",
    "description": "task description",
    "status": false
}
```

request body attributes:

| Attribute | Type | Description |
| --- | --- | --- |
| name | string | task name |
| description | string | task description |
| status | bool | task status |

#### Response

```json
{
    "result": "created"
}
```