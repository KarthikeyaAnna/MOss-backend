from flask import Flask
from flask_cors import CORS
from app import app as flask_app

# Create a new Flask app for the serverless function
app = Flask(__name__)
CORS(app)  # Enable CORS if needed

# Define a route that forwards requests to the main Flask app
@app.route('/.netlify/functions/api', methods=['GET', 'POST'])
def api():
    # Use the WSGI interface to handle requests
    return flask_app

# If using a specific serverless platform, you might need to define a handler
# For example, if using AWS Lambda, you would typically use serverless_wsgi
