# Phase 06: From API Integration to Agent Tools

## Task 24: API Tool Specification

- **Tool Name**: `get_post_by_id`
- **Description**: Retrieves full details (userId, id, title, body) of an individual blog post by ID from the JSONPlaceholder REST API.
- **HTTP Method**: `GET`
- **Endpoint**: `https://jsonplaceholder.typicode.com/posts/{post_id}`
- **Required Inputs**: `post_id` (integer)
- **Optional Inputs**: None
- **Expected Output**: JSON object containing `userId` (int), `id` (int), `title` (str), and `body` (str).
- **Possible Errors**: `404 Not Found`, `429 Rate Limit Exceeded`, `500 Server Error`, `Timeout`.
- **Authentication Required**: No (Public REST endpoint).

---

## Task 25: Agent Tool Interface (JSON Schema / Tool Definition)

```json
{
  "tool_name": "get_post",
  "purpose": "Retrieve a specific blog post by its unique ID for reasoning, inspection, or summarization.",
  "parameters": {
    "type": "object",
    "properties": {
      "post_id": {
        "type": "integer",
        "description": "The unique numerical identifier of the post to retrieve (e.g. 1)."
      }
    },
    "required": [
      "post_id"
    ]
  },
  "output_schema": {
    "type": "object",
    "properties": {
      "id": {
        "type": "integer"
      },
      "userId": {
        "type": "integer"
      },
      "title": {
        "type": "string"
      },
      "body": {
        "type": "string"
      }
    }
  },
  "possible_errors": [
    "404 Not Found: Post ID does not exist",
    "429 Too Many Requests: Rate limit exceeded",
    "500 Internal Server Error: Remote backend failure",
    "Timeout: Network connection timed out"
  ]
}
```
