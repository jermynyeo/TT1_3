const jwt = require("jsonwebtoken");
require("dotenv").config();

module.exports = function (req, res, next) {
  // Get token from header
  const token = req.header("token");

  // Verify token
  try {
    //if not token
    if (!token) {
      return res.status(403).json("Not Authorized");
    }
    //it is going to give use the user id (user:{id: user.id})
    const payload = jwt.verify(token, process.env.jwtSecret);

    req.user = payload.user;
    next();
  } catch (err) {
    res.status(401).json({ msg: "Token is not valid" });
  }
};
