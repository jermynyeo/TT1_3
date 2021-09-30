const express = require("express");
const app = express();
const cors = require("cors");
const PORT = process.env.PORT || 5000;
const path = require("path");

//middleware

app.use(express.json());
app.use(cors());

//routes
app.use("/auth", require("./routes/jwtAuth"));

//app.use("/dashboard", require("./routes/dashboard"));

if (process.env.NODE_ENV === "production") {
  app.use(express.static(path.join(__dirname, "client/build")));
}

app.listen(PORT, () => {
  console.log("server is running on port 5000");
});

// app.get("*", (req, res) => {
//   res.sendFile(path.join(__dirname, "client/build/index.html"));
// });
