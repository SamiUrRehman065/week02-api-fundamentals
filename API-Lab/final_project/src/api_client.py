"""
Final Integration Project - REST API Client
Demonstrates complete REST API interaction, environment variable configuration,
status code checking, error handling, request timeouts, and agent tool compatibility.
"""
import os
import sys
import requests
from dotenv import load_dotenv

# Load configuration from environment / .env file
load_dotenv()

BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
API_KEY = os.getenv("API_KEY", "")
TIMEOUT = int(os.getenv("API_TIMEOUT", "10"))

def get_headers():
    """Build request headers including authentication if configured."""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    return headers

def fetch_post(post_id: int):
    """
    Agent Tool Equivalent: get_post(post_id)
    Retrieves post entity with robust error handling and status code validation.
    """
    url = f"{BASE_URL}/posts/{post_id}"
    print(f"\n[REQUEST] GET {url} (Timeout: {TIMEOUT}s)...")
    
    try:
        response = requests.get(url, headers=get_headers(), timeout=TIMEOUT)
        
        if response.status_code == 200:
            data = response.json()
            print("[SUCCESS 200] Post successfully retrieved:")
            print(f"  Post ID : {data.get('id')}")
            print(f"  User ID : {data.get('userId')}")
            print(f"  Title   : {data.get('title')}")
            print(f"  Body    : {data.get('body')[:60]}...")
            return data
        elif response.status_code == 404:
            print(f"[ERROR 404] Resource not found: Post ID {post_id} does not exist.")
            return None
        elif response.status_code == 401:
            print("[ERROR 401] Unauthorized: Missing or invalid API key.")
            return None
        elif response.status_code == 429:
            print("[ERROR 429] Rate limit exceeded. Please back off before retrying.")
            return None
        else:
            print(f"[ERROR {response.status_code}] Server responded with status {response.status_code}")
            return None
            
    except requests.exceptions.Timeout:
        print("[TIMEOUT] Connection timed out while waiting for server response.")
        return None
    except requests.exceptions.ConnectionError:
        print("[NETWORK ERROR] Failed to connect to server. Check DNS and internet connection.")
        return None
    except requests.exceptions.RequestException as err:
        print(f"[GENERAL ERROR] Unexpected request error: {err}")
        return None

def main():
    print("=" * 55)
    print(" WEEK 02 FINAL INTEGRATION PROJECT: REST API CLIENT ")
    print("=" * 55)
    
    # 1. Successful API call
    print("\n--- Test 1: Fetch Valid Post (ID: 1) ---")
    fetch_post(1)
    
    # 2. 404 Error handling
    print("\n--- Test 2: Fetch Non-existent Post (ID: 999999) ---")
    fetch_post(999999)
    
    print("\n[COMPLETE] All client operations executed gracefully.")

if __name__ == "__main__":
    main()
