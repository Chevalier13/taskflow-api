# TaskFlow API 🚀

API desenvolvida para a avaliação P2 da disciplina de Lab. Programação Back-End (Engenharia de Software).

## 🛠️ Tecnologias Utilizadas
* Node.js & Express
* PostgreSQL 16
* Jest & Supertest (Testes Unitários/Integração)
* Docker & Docker Compose

## 📌 Rotas da API (CRUD)
* `GET /tasks` - Lista todas as tarefas
* `GET /tasks/:id` - Busca uma tarefa específica
* `POST /tasks` - Cria uma nova tarefa (Body: `{ "title": "Estudar para P2", "description": "Focar em Docker" }`)
* `PUT /tasks/:id` - Atualiza uma tarefa existente
* `DELETE /tasks/:id` - Remove uma tarefa

## 🐳 Como Executar o Projeto (Via Docker Compose)

Conforme as diretrizes da Aula 11, você não precisa ter Node.js ou Postgres instalados localmente. Basta ter o **Docker Desktop** configurado.

1. Baixe apenas o arquivo `docker-compose.yml` deste repositório em uma pasta local.
2. Abra o terminal nesta pasta.
3. Execute o comando:
```bash
docker compose up -d