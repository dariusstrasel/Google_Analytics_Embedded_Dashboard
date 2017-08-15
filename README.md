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
