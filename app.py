from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# --- MySQL Configuration ---
# Your MySQL root user and password
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sk%40080022@localhost/mini_blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# --- Blog Post Model ---
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

# --- Create tables (run once) ---
with app.app_context():
    db.create_all()

# --- API Routes ---
@app.route("/api/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"id": p.id, "title": p.title, "content": p.content} for p in posts])

@app.route("/api/posts", methods=["POST"])
def add_post():
    data = request.get_json()
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Invalid data"}), 400
    new_post = Post(title=data["title"], content=data["content"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post added successfully"}), 201

# --- Run Server ---
if __name__ == "__main__":
    app.run(debug=True)
