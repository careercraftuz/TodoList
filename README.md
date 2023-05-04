# TodoList

## Database Design
Here is a sample schema for our Todo List app's database:

## Api Design

| Method | Path | Description |
| --- | --- | --- |
| GET | /api/tasks/ | Get all todo tasks |
| GET | /api/tasks/<int:id> | Get a todo task by id |
| POST | /api/tasks/<int:id>/delete | Delete a todo task by id |
| POST | /api/tasks/<int:id>/update | Update a todo task by id |
| POST | /api/create-task/ | Create a todo task |

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
