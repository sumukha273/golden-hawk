from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)

# Define the /status/v2/info endpoint
@app.route('/status/v2/info', methods=['GET'])
def status_info():
    # Return a JSON response
    return jsonify({"info": "Everything looks good"})

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
