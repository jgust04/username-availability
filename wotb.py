import requests
import re

# Your API key (replace with your actual application_id)
APPLICATION_ID = "db26e4b918eeb94c1c31cb818677d188"
API_URL = "https://api.wotblitz.com/wotb/account/list/?application_id=13f443c8d2049f4f05a12d18c311b224"

# Function to check username availability via API
def check_username(username):
    params = {
        "application_id": APPLICATION_ID,
        "search": username,
        "language": "en",
        "r_realm": "na"  # Change to "eu", "ru", etc. for other regions
    }
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if not data.get("data"):  # If "data" is empty, username is available
            print(f"✅ The username '{username}' is AVAILABLE!")
        else:
            print(f"❌ The username '{username}' is TAKEN.")

# Ask user for a username to check
while True:
    username_to_check = input("Enter a username to check availability (Enter 'q' to exit): ").strip()
    if username_to_check == "q":
        break
    else:
        # Must be at least 3 characters long
        if len(username_to_check) < 3:
            print("⚠️ Error: Username must be at least 3 characters long.")

        # Must only contain Latin letters, digits, and underscores
        if not re.match(r'^[A-Za-z0-9_]+$', username_to_check):
            print("⚠️ Error: Username can only contain Latin letters (A-Z, a-z), digits (0-9), and underscores (_).")
        
        else:
            check_username(username_to_check)
