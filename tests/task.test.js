const request = require('supertest');
const app = require('../src/app');

describe('Testes da API de Tarefas', () => {
  it('Deve responder com 200 na rota raiz', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.body).toHaveProperty('message');
  });
});