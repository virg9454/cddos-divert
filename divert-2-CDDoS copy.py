

import http.client, os, json
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv('API_KEY')
account_id = os.getenv('ACCOUNT_ID')

#test variables
print("--"*44)
if api_key:
    print(f"API Key: {api_key[:6]}\n\n")
else:
    print("API Key not found in environment variables.\n\n")
if account_id:
    print(f"API Key: {account_id[:6]}\n\n")
else:
    print("Account ID not found in environment variables.\n\n")
print("--"*44)
api_url= "api.radwarecloud.app"
# Replace asset_endpoint with your own endpoint
asset_endpoint = "69d3c9496bdd502e2f6c2ce7"



conn = http.client.HTTPSConnection(api_url)
payload = json.dumps({
  "assets": [
    {
      "_id": {
        "_oid": asset_endpoint
      },
      "type": "server"
    }
  ],
  "additional_email_text": "Test from Virg"
})
headers = {
  'x-api-key': api_key,
  'Content-Type': 'application/json'
}
conn.request("POST", f"//api/assets/activate/?isDivert=true&type=account&id={account_id}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
