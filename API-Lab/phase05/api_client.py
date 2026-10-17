"""
Phase 05: Errors, Timeouts & Rate Limits
Tasks 19-23: Status code validation (404, multi-status), request timeouts,
fault-tolerant error handling, and rate-limiting inspection.
"""
import requests

def task19_handle_404():
    print("=== Task 19: Handle 404 Error ===")
    url = "https://jsonplaceholder.typicode.com/posts/999999"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print("Request failed.")
            print(f"Status Code: {response.status_code}")
            print("Resource not found.")
        elif response.status_code == 200:
            print("Resource found:", response.json())
        else:
            print(f"Unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
    print()

def task20_handle_multiple_errors():
    print("=== Task 20: Handle Multiple HTTP Status Codes ===")
    def evaluate_status(status_code):
        if status_code in (200, 201):
            return f"[{status_code} Success] Operation completed successfully."
        elif status_code == 400:
            return f"[{status_code} Bad Request] Malformed request syntax or parameters."
        elif status_code == 401:
            return f"[{status_code} Unauthorized] Missing or invalid credentials."
        elif status_code == 404:
            return f"[{status_code} Not Found] The requested resource does not exist."
        elif status_code == 429:
            return f"[{status_code} Too Many Requests] Rate limit exceeded. Back off and retry."
        elif status_code == 500:
            return f"[{status_code} Internal Server Error] The backend server failed."
        else:
            return f"[{status_code}] Status code received."

    for code in [200, 400, 401, 404, 429, 500]:
        print(evaluate_status(code))
    print()

def task21_add_timeout():
    print("=== Task 21: Add Request Timeout ===")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url, timeout=5.0)
        print(f"Success! Status Code: {response.status_code}")
    except requests.exceptions.Timeout:
        print("Error: The request timed out before receiving a server response.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    print()

def task22_safe_api_client():
    print("=== Task 22: Comprehensive Failure Handling ===")
    def safe_request(url, timeout=5.0):
        try:
            res = requests.get(url, timeout=timeout)
            if res.status_code == 200:
                return {"type": "SUCCESS", "status": res.status_code, "data": res.json()}
            else:
                return {"type": "API_ERROR", "status": res.status_code, "msg": f"HTTP {res.status_code}"}
        except requests.exceptions.Timeout:
            return {"type": "TIMEOUT", "msg": "Connection timed out."}
        except requests.exceptions.ConnectionError:
            return {"type": "NETWORK_FAILURE", "msg": "Network failure: Connection refused or DNS error."}
        except requests.exceptions.RequestException as e:
            return {"type": "GENERAL_ERROR", "msg": str(e)}

    print("Testing safe call to valid endpoint:")
    print(safe_request("https://jsonplaceholder.typicode.com/posts/1"))
    print()

if __name__ == "__main__":
    task19_handle_404()
    task20_handle_multiple_errors()
    task21_add_timeout()
    task22_safe_api_client()
