import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());

// Route: forward request to ML API
app.post("/calories", async (req, res) => {
  try {
    const response = await fetch("http://127.0.0.1:8000/predict_calories", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(req.body),
    });

    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: "ML API not reachable" });
  }
});

app.listen(3000, () => console.log("Node backend running on port 3000"));
