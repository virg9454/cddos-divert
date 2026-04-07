

import http.client
import json

conn = http.client.HTTPSConnection("api.radwarecloud.app")
payload = json.dumps({
  "assets": [
    {
      "_id": {
        "_oid": "69d3c9496bdd502e2f6c2ce7"
      },
      "type": "server"
    }
  ],
  "additional_email_text": "Test from Virg"
})
headers = {
  'x-api-key': 'eyJhbGciOiJIUzM4NCJ9.eyJhY2NvdW50SWQiOnsidmFsdWUiOiI2NDQ1NDkxNzUyZmVkODZjZmVjNTJhMjUifSwicm9sZUlkcyI6WyJyb2xfeFpuQUcxbXJQdkdWZmQ3cSIsInJvbF9oNk1CVmtZR3F5U1czTUIzIiwicm9sX21yMko4V2VjSTJReFNNUmciLCJyb2xfaGtCdE8yUVZFVHdBNlBONSIsInJvbF9UaGNJYTVQQW9vNkxaeUFJIl0sImV4cGlyeVRpbWVzdGFtcCI6MTgzODE3NDQwMCwiaWQiOnsidmFsdWUiOiI2OWQzYzc1NDg4OWFjYjIxN2Y3NjU3ZmUifX0.wud1VLS9GQHjm6Je9L5eAH2C3SGGsvGrLYQLZrB9lBSIRKjO2q6fUtxZYQnTwZcT',
  'Content-Type': 'application/json'
}
conn.request("POST", "//api/assets/deactivate/?isDivert=true&type=account&id=62e1528e6d1ad213fcbc93a6", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))