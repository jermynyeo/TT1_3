const Pool = require("pg").Pool;
require("dotenv").config();

// const devConfig = {
//   user: process.env.PG_USER,
//   password: process.env.PG_PASSWORD,
//   host: process.env.PG_HOST,
//   port: process.env.PG_PORT,
//   database: process.env.PG_DATABASE,
// };

const devConfig = {
  user: "postgres",
  password: "password",
  host: "localhost",
  port: 5432,
  database: "ecommerce",
};

// const proConfig = {
//   connectionString: process.env.DATABASE_URL,
// };

// const pool = new Pool(
//   process.env.NODE_ENV === "production" ? proConfig : devConfig
// );

const pool = new Pool(devConfig);
module.exports = pool;
