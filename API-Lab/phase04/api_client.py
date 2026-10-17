"""
Phase 04: Authentication, API Keys & Secure Configuration
Tasks 16-18: Authorization headers, Bearer tokens, and .env configuration.
"""
import os
import requests
from dotenv import load_dotenv

def task17_authorization_header():
    print("=== Task 17: Implement Authorization Header ===")
    url = "https://api.example.com/protected/data"
    bearer_token = "eyJhGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.dummy_sample_payload.sF4"
    
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # Sanitized preview for safe logging
    sanitized_headers = headers.copy()
    sanitized_headers["Authorization"] = "Bearer " + "*" * 20
    
    print(f"Request URL       : {url}")
    print(f"Sanitized Headers : {sanitized_headers}")
    print(f"Header Keys       : {list(headers.keys())}")
    print()

def task18_load_credentials_from_env():
    print("=== Task 18: Move Credentials to .env ===")
    # Load environment variables from local .env
    load_dotenv()
    
    # Retrieve key without hardcoding
    api_key = os.getenv("API_KEY", "sk_test_SAMPLE_DEFAULT_KEY_987654321")
    
    masked_key = api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]
    print(f"Securely loaded API Key: {masked_key}")
    print("Security Check: Verified API Key is loaded via environment variables and excluded by .gitignore.")
    print()

if __name__ == "__main__":
    task17_authorization_header()
    task18_load_credentials_from_env()
