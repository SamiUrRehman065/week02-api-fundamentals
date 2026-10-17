# Phase 02: HTTP Requests, Responses & REST

## 1. URL Analysis (`https://api.example.com/students/101`)

| Component | Value | Description |
| :--- | :--- | :--- |
| **Protocol** | `https` | Hypertext Transfer Protocol Secure (TLS encrypted communication) |
| **Host / Domain** | `api.example.com` | Target server domain address hosting the API service |
| **Path** | `/students/101` | Hierarchical route specifying the resource location |
| **Resource** | `students` | The primary entity collection (noun) |
| **Resource Identifier** | `101` | Unique primary key identifying the specific student record |

---

## 2. REST API Operations

| Operation | HTTP Method | Endpoint | Idempotent? | Safe? |
| :--- | :--- | :--- | :--- | :--- |
| Retrieve all students | `GET` | `/students` | Yes | Yes |
| Create a student | `POST` | `/students` | No | No |
| Retrieve student 101 | `GET` | `/students/101` | Yes | Yes |
| Update student 101 | `PUT` | `/students/101` | Yes | No |
| Delete student 101 | `DELETE` | `/students/101` | Yes | No |

---

## 3. HTTP Methods Semantic Rationale
REST standardizes uniform interfaces where nouns represent resources and HTTP verbs dictate actions:
- `GET`: Safe, read-only retrieval without mutating server state.
- `POST`: Submits data to create new subordinate resources; server assigns an ID.
- `PUT`: Completely updates or replaces the identified target resource.
- `DELETE`: Permanently destroys the identified resource from storage.
