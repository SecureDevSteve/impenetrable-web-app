import os

api_key = os.getenv("API_KEY")

def connect_to_database():
    if api_key:
        print("Successfully authenticated!")
    else:
        print("Error: API_KEY not found in environment.")

if __name__ == "__main__":
    connect_to_database()