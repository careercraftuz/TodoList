# TodoList

## Database Design
Here is a sample schema for our Todo List app's database:

### Task model
| Field name | Description |
|-------------|--|
| id           | SERIAL PRIMARY KEY |
| title        | VARCHAR(100) |
| description  | TEXT |
| completed    | BOOLEAN DEFAULT FALSE |
| user_id      | INTEGER REFERENCES users(id) |
| created_at   | TIMESTAMP DEFAULT NOW() |
| updated_at   | TIMESTAMP DEFAULT NOW() |

## Api Design
| HTTP Method | Endpoint | Description | Request Body | Response Body |
| --- | --- | --- | --- | --- |
| GET | /tasks | Get a list of all tasks | None | List of task objects |
| GET | /tasks/:id | Get a task by ID | None | Task object |
| POST | /tasks | Create a new task | `{'title': str, 'description': str}` | Task object |
| PUT | /tasks/:id | Update a task | `{'title': str, 'description': str, 'completed': bool}` | Task object |
| DELETE | /tasks/:id | Delete a task | None | None |

**Request Body:**

- `POST /tasks`: 

```python
{
    'title': 'string',
    'description': 'string'
}
```

- `PUT /tasks/:id`: 

```python
{
    'title': 'string',
    'description': 'string',
    'completed': True/False
}
```

- `GET /tasks`: 

```python
[
    {
        'id': int,
        'title': 'string',
        'description': 'string',
        'completed': True/False,
        'created_at': 'datetime',
        'updated_at': 'datetime'
    },
    ...
]
```

- `GET /tasks/:id, POST /tasks, PUT /tasks/:id`: 

```python
{
    'id': int,
    'title': 'string',
    'description': 'string',
    'completed': True/False,
    'created_at': 'datetime',
    'updated_at': 'datetime'
}
```