# Google Analytics Embedded Dashboard

To Run:
1. Clone the repository:
```bash
git clone https://github.com/dariusstrasel/Google_Analytics_Embedded_Dashboard.git
```
2. Setup flask:
```bash
export flask_app=app.py
```
3. Run flask:
```bash
flask run
```

4. Visit localhost:5000 (default settings)

# Configuration Concerns:
- AWS S3: S3 object named "google-dashboard-service-key" with a file named "key.json" File should be OAuth credentials for a service account generated from the Google API Console.
- AWS CLI
- Heroku (optional) 

# How it works:
1. Client connects to Flask web server (GET Request).
2. Flask opens connection to S3 (using AWS Access Key and AWS Secret Access Key, pulled from host OS enviornment variables); reads Google Service Account JSON key to memory.
3. Sends JSON key to Google Analytics Oauth Callback, which returns an authenticated oauth access token.
4. Flask renders a Jinja template, embedding the access token as a Javascript constant, and serves HTML to client.
5. Upon painting to client, HTML authenticates to the Google Analytics API using embedded access token.
6. Upon success, template generates JavaScript components using Google Analytics Embedded Dashboard API.
7. ???
8. Profit!
