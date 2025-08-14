import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  // Fetch posts from backend
  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/posts")
      .then((res) => setPosts(res.data))
      .catch((err) => console.log(err));
  }, []);

  // Add new post
  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://127.0.0.1:5000/api/posts", { title, content })
      .then((res) => {
        setPosts([...posts, { title, content, id: posts.length + 1 }]);
        setTitle("");
        setContent("");
      })
      .catch((err) => console.log(err));
  };

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "0 auto" }}>
      <h1>Mini Blog</h1>

      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          style={{ width: "100%", marginBottom: "10px", padding: "8px" }}
        />
        <textarea
          placeholder="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
          style={{ width: "100%", marginBottom: "10px", padding: "8px" }}
        />
        <button type="submit" style={{ padding: "10px 20px" }}>Add Post</button>
      </form>

      <div>
        {posts.map((post) => (
          <div key={post.id} style={{ border: "1px solid #ccc", padding: "10px", marginBottom: "10px" }}>
            <h3>{post.title}</h3>
            <p>{post.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
