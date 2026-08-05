from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "env-resource-privileged-template sample app",
        "environment": os.environ.get("ENVIRONMENT", "unknown")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)