const pool = require('../config/db');

module.exports = {
  async getAll(req, res) {
    const { rows } = await pool.query('SELECT * FROM tasks');
    return res.json(rows);
  },

  async create(req, res) {
    const { title, description } = req.body;
    if (!title) return res.status(400).json({ error: 'Título é obrigatório' });
    
    const { rows } = await pool.query(
      'INSERT INTO tasks (title, description) VALUES ($1, $2) RETURNING *',
      [title, description]
    );
    return res.status(201).json(rows[0]);
  },

  async update(req, res) {
    const { id } = req.params;
    const { title, description, done } = req.body;
    
    const { rows } = await pool.query(
      'UPDATE tasks SET title = $1, description = $2, done = $3 WHERE id = $4 RETURNING *',
      [title, description, done, id]
    );
    
    if (rows.length === 0) return res.status(404).json({ error: 'Tarefa não encontrada' });
    return res.json(rows[0]);
  },

  async delete(req, res) {
    const { id } = req.params;
    const { rowCount } = await pool.query('DELETE FROM tasks WHERE id = $1', [id]);
    
    if (rowCount === 0) return res.status(404).json({ error: 'Tarefa não encontrada' });
    return res.status(204).send();
  }
};