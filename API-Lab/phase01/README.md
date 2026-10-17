# Phase 01: API & Client-Server Fundamentals

## Overview
Phase 01 introduces foundational web API concepts, exploring how clients (such as web browsers or Python applications) communicate with remote backend servers over HTTP.

## Key Exercises
- **Task 01**: Browser exploration of JSONPlaceholder endpoints (`/posts/1`, `/posts/2`, `/posts/3`).
- **Task 02**: Client-Server architecture and request-response lifecycle mapping.
- **Task 03**: Distinguishing collection resources (`/posts`) from individual member resources (`/posts/1`).

## Architecture Flow
```
[Client / Web Browser] 
       │ 
       ▼ (1) HTTP GET https://jsonplaceholder.typicode.com/posts/1
[API Interface / Gateway]
       │
       ▼ (2) Forward / Route Request
[Backend Server & Database] (Queries record with ID 1)
       │
       ▼ (3) Return record
[API Layer] (Formats HTTP 200 OK + JSON Payload)
       │
       ▼ (4) Response Packet
[Client / Web Browser] (Parses and renders JSON)
```
