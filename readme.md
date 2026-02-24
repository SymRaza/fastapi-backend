# Todo API

A simple and elegant RESTful API built with FastAPI for managing todo items. This application allows users to create, retrieve, and delete tasks with built-in validation.

## Features

- **Create Items**: Add new todo items with text and completion status
- **Read Items**: Retrieve all items or fetch a specific item by ID
- **Delete Items**: Remove completed or unwanted items
- **Validation**: Automatic validation to prevent duplicate items and empty text
- **FastAPI**: Modern, fast web framework with automatic API documentation
- **Error Handling**: Comprehensive HTTP error responses for invalid operations

## Project Structure

```
.
├── main.py           # Main FastAPI application with all endpoints
├── db.py             # Database module (ready for expansion)
├── requirements.txt  # Python dependencies
└── readme.md         # Project documentation
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or download the project to your local machine

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-restart when code changes are detected.

The API will be available at: `http://localhost:8000`

### Interactive API Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## API Endpoints

### 1. Hello Endpoint
```
GET /
```
Returns a greeting message.

**Query Parameters:**
- `name` (string): The name to greet

**Example:**
```bash
curl "http://localhost:8000/?name=John"
```

**Response:**
```json
"Hello John"
```

---

### 2. Create Item
```
POST /items
```
Creates a new todo item.

**Request Body:**
```json
{
  "text": "Buy groceries",
  "is_done": false
}
```

**Response:**
```json
[
  {
    "text": "Buy groceries",
    "is_done": false
  }
]
```

**Errors:**
- `400`: Item with the same text already exists
- Text validation: Text cannot be empty

---

### 3. Get All Items
```
GET /items
```
Retrieves all todo items.

**Response:**
```json
[
  {
    "text": "Buy groceries",
    "is_done": false
  },
  {
    "text": "Complete project",
    "is_done": true
  }
]
```

---

### 4. Get Item by ID
```
GET /items/{item_id}
```
Retrieves a specific item by its index.

**Path Parameters:**
- `item_id` (integer): The index of the item in the list

**Response:**
```json
{
  "text": "Buy groceries",
  "is_done": false
}
```

**Errors:**
- `404`: Item not found

---

### 5. Delete Item
```
DELETE /items/{item_id}
```
Deletes a specific item by its index.

**Path Parameters:**
- `item_id` (integer): The index of the item to delete

**Response:**
```json
{
  "message": "Item deleted successfully"
}
```

**Errors:**
- `404`: Item not found

## Item Model

The `Item` model has the following structure:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `text` | string | Required | The todo item description (cannot be empty) |
| `is_done` | boolean | `false` | Whether the item is completed |

## Dependencies

- **FastAPI**: Modern web framework for building APIs with Python
- **Uvicorn**: ASGI web server for running the application

See [requirements.txt](requirements.txt) for exact versions.

## Example Usage

### Using cURL

```bash
# Get greeting
curl "http://localhost:8000/?name=World"

# Create a new item
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"text": "Learn FastAPI", "is_done": false}'

# Get all items
curl "http://localhost:8000/items"

# Get specific item (ID 0)
curl "http://localhost:8000/items/0"

# Delete item (ID 0)
curl -X DELETE "http://localhost:8000/items/0"
```

### Using Python Requests

```python
import requests

BASE_URL = "http://localhost:8000"

# Create item
response = requests.post(f"{BASE_URL}/items", 
    json={"text": "Learn FastAPI", "is_done": False})
print(response.json())

# Get all items
response = requests.get(f"{BASE_URL}/items")
print(response.json())

# Delete item
response = requests.delete(f"{BASE_URL}/items/0")
print(response.json())
```

## Future Enhancements

- Integrate with a real database (SQLAlchemy, PostgreSQL, etc.)
- Add user authentication
- Implement item update/edit functionality
- Add pagination for large datasets
- Deploy to cloud services (AWS, Azure, Heroku)
- Add unit tests

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, please create an issue or contact the project maintainer.
