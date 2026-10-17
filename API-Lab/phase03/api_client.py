"""
Phase 03: JSON & Python API Integration
Tasks 11-15: Working with JSON records, JSON arrays, and calling REST APIs.
"""
import requests

def task11_json_student_record():
    print("=== Task 11: Single JSON Student Record ===")
    student = {
        "name": "Ali",
        "marks": 85,
        "program": "BSCS"
    }
    print(f"Student Name   : {student['name']}")
    print(f"Student Marks  : {student['marks']}")
    print(f"Student Program: {student['program']}")
    print()

def task12_json_student_array():
    print("=== Task 12: Work With a JSON Array ===")
    students = [
        {"id": 1, "name": "Ali"},
        {"id": 2, "name": "Sara"},
        {"id": 3, "name": "Usman"}
    ]
    for s in students:
        print(f"Student ID: {s['id']}, Name: {s['name']}")
    print()

def task13_first_api_client():
    print("=== Task 13: Access Single Post (/posts/1) ===")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Post ID: {data['id']}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    print()

def task14_multiple_records():
    print("=== Task 14: Retrieve Multiple API Records (/posts/1, 2, 3) ===")
    base_url = "https://jsonplaceholder.typicode.com/posts"
    for post_id in [1, 2, 3]:
        res = requests.get(f"{base_url}/{post_id}")
        if res.status_code == 200:
            print(f"Post {post_id}: {res.json()['title']}")
    print()

def task15_process_collection():
    print("=== Task 15: Retrieve and Process Collection (/posts) ===")
    url = "https://jsonplaceholder.typicode.com/posts"
    res = requests.get(url)
    if res.status_code == 200:
        posts = res.json()
        print(f"Total posts returned: {len(posts)}")
        print("First 5 post titles:")
        for idx, post in enumerate(posts[:5], start=1):
            print(f"  {idx}. {post['title']}")
    print()

if __name__ == "__main__":
    task11_json_student_record()
    task12_json_student_array()
    task13_first_api_client()
    task14_multiple_records()
    task15_process_collection()
