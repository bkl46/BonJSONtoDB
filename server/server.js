require('dotenv').config();
const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3000;

// Database connection
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }, // Required for Render-hosted DB
});

// Middleware
app.use(express.json());
app.use(cors());

// Get all entries
app.get('/entries', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM fribley');
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const aa = "INSERT INTO fribley (name, kcal, serving_size, total_fat, sat_fat, trans_fat, cholesterol, sodium, carbs, fiber, sugars, protein, vegetarian, vegan, made_without_gluten_containing_ingredients, balance, halal, farm_to_fork, humane, offered_often, date) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21) ";
// Add an entry
app.post('/entries', async (req, res) => {
  try {
    const { c1, c2, c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20, c21 } = req.body;

    const result = await pool.query(aa,[c1, c2, c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20, c21 ]);
    res.json("hi");
    //res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
