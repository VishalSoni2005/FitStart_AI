// node-backend/app.js
const express = require("express");
const axios = require("axios");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

const ML_API_URL = "http://127.0.0.1:8000/predict_calories";

app.get("/health", (req, res) => res.json({ status: "ok" }));

app.post("/calories", async (req, res) => {
  try {
    const data = req.body;
    console.log("DATA from ui : ", data);

    const response = await axios.post(ML_API_URL, req.body, {
      headers: { "Content-Type": "application/json" },
      timeout: 5000,
    });
    res.json(response.data);
  } catch (err) {
    console.error("Error calling ML API:", err.message || err);
    if (err.response) {
      res.status(err.response.status).json(err.response.data);
    } else {
      res.status(502).json({ error: "ML service unavailable" });
    }
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Node backend running on port ${PORT}`));
