## API Documentation Details

### GET /api/tasks/

Use this to get all todo tasks. Returns a list of [Task](types.md#task) object.

### GET /api/tasks/<int:id>

Use this to get a todo task by id. Returns a [Task](types.md#task) object.

#### Request

resquest url params:

| Attribute | Type | Description |
| --- | --- | --- |
| id | int | task id |

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

update a todo task by id. Returns an updated [Task](types.md#task) object.

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

| Attribute | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | no | task name |
| description | string | no | task description |
| status | bool | no | task status |

### POST /api/create-task/

create a todo task. Returns a [Task](types.md#task) object.

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

| Attribute | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | yes | task name |
| description | string | yes | task description |
| status | bool | yes | task status |

#### Response

```json
{
    "result": "created"
}
```
