# Instructions

The Instructor should Run this Flask server before PF-4-3: End of Module Assessment begins.
 * Click the Run button, and ensure the Flask server remains running throughout the Assessment.

They should then share the URL for the Replit with learners.
 * The URL should look similar to this: `https://pf-4-3-end-of-module-assessment-server.<team-name>.repl.co`
   * You should be able to find this URL in the "Webview" tab in the upper-right pane.
   * You can also find the Webview icon in the Tools menu in the bottom-left.

# Troubleshooting

## Working Examples

The instructor can use these examples for troubleshooting the Flask server.

### POST
```
import requests
import json

url = 'https://pf-4-3-end-of-module-assessment-server.<team-name>.repl.co/send_cheep'
data = {'message': 'test cheep'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response)
```

### GET

```
import requests

url = "https://pf-4-3-end-of-module-assessment-server.<team-name>.repl.co/get_cheeps"

response = requests.get(url)

response_json = response.json()
print(response_json)
```