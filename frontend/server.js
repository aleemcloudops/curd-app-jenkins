const express = require('express');
const path = require('path');
const axios = require('axios');
const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

// API proxy to backend
const API = 'http://localhost:5000';

app.get('/api/notes', async (req, res) => {
  const response = await axios.get(`${API}/notes`);
  res.json(response.data);
});

app.post('/api/notes', async (req, res) => {
  const response = await axios.post(`${API}/notes`, req.body);
  res.json(response.data);
});

app.put('/api/notes/:id', async (req, res) => {
  const response = await axios.put(`${API}/notes/${req.params.id}`, req.body);
  res.json(response.data);
});

app.delete('/api/notes/:id', async (req, res) => {
  const response = await axios.delete(`${API}/notes/${req.params.id}`);
  res.json(response.data);
});

app.listen(PORT, () => {
  console.log(`Frontend running on http://localhost:${PORT}`);
});
