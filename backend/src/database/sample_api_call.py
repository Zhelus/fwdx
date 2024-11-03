import requests
import base64

# Replace these with your actual MongoDB Atlas API details
api_user = "your_api_user"
api_key = "your_api_key"
project_id = "your_project_id"
base_url = f"https://cloud.mongodb.com/api/atlas/v1.0/groups/{project_id}/clusters"

# Base64 encode the API credentials
credentials = base64.b64encode(f"{api_user}:{api_key}".encode('utf-8')).decode('utf-8')
headers = {
    "Authorization": f"Basic {credentials}",
    "Content-Type": "application/json"
}

# Make a GET request to retrieve cluster information
response = requests.get(base_url, headers=headers)

if response.status_code == 200:
    print("Cluster information:", response.json())
else:
    print("Failed to retrieve data. Status code:", response.status_code, "Response:", response.text)