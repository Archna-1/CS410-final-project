const express = require("express");
const axios = require("axios");
const cors = require("cors");
const ejs = require("ejs");

const app = express();
const port = 5001; // Set your desired port

app.use(cors()); // Enable CORS middleware

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("index");
});

app.post("/get-remote-text", async (req, res) => {
  const url = req.body.url;

  if (!url) {
    return res.status(400).json({ error: "URL parameter is missing" });
  }

  try {
    const response = await axios.get(url);

    if (response.status === 200) {
      const text = response.data;
      res.json({ text });
      // res.render(index);
    } else {
      res
        .status(response.status)
        .json({ error: `HTTP error! Status: ${response.status}` });
    }
  } catch (error) {
    console.error("Error fetching data:", error.message);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port http://localhost:${port}`);
});
