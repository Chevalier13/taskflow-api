const { Pool } = require('pg');

const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  user: process.env.DB_USER || 'admin',
  password: process.env.DB_PASSWORD || 'senha_secreta_123',
  database: process.env.DB_NAME || 'taskflow',
  port: 5432,
});


const initDb = async () => {
  await pool.query(`
    CREATE TABLE IF NOT EXISTS tasks (
      id SERIAL PRIMARY KEY,
      title VARCHAR(255) NOT NULL,
      description TEXT,
      done BOOLEAN DEFAULT false
    );
  `);
};

initDb().catch(err => console.error("Erro ao criar tabela:", err));

module.exports = pool;