from contextlib import nullcontext
from flask import Flask,jsonify

app = Flask(__name__)

data = {
     "kenya_cases": {"id": "5b1abe9a-3b4a-448c-8037-addc1f6e5158", "timestamp":'2023-03-25 15:14:46.598683', "file_content_type": 'application/pdf', 'source_file':nullcontext, 
'document_id': '116c8171-06f0-2333-4d49-0a66cf5bc112'},
    "uganda_cases": {"id": "5b1abe9a-3b4a-448c-8037-addc1tryyryt", "timestamp":'2023-03-25 15:14:46.598679', "file_content_type": 'text/html', 'source_file':nullcontext, 
'document_id': '116c8171-5678-2333-4d49-0a66cf5bc112'},
    "tanzania_cases": {"id": "5b1abe9a-3b4a-448c-8040-addc1f6e5158", "timestamp":'2023-03-25 15:14:46.598680', "file_content_type": 'application/pdf', 'source_file':nullcontext, 
'document_id': '116c8171-06f0-2333-4d49-0a66cf5bc112'}
}
# endpoint for the flask app
@app.route('/scrape/<action>/<target>')

# function scrape takes in two params
def scrape(action, target):
    if action in data and target in data[action]:
        return jsonify(data[action][target]), 200
    else:
        return jsonify({"error": "Invalid action or target parameter"}), 400

if __name__ == '__main__':
    app.run()
