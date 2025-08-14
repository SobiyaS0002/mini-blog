from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/api/posts", methods=["GET"])
def get_posts():
    # Temporary dummy data (we'll connect to MySQL later)
    posts = [
        {"id": 1, "title": "My first blog", "content": "This is my first post!"},
        {"id": 2, "title": "Another day", "content": "Learning Flask + React is fun!"}
    ]
    return jsonify(posts)

if __name__ == "__main__":
    app.run(debug=True)
