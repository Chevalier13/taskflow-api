FROM python:3.11-slim

# Evita que o Python escreva arquivos .pyc e bufeie os logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Copia e instala os requerimentos padrão
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instala a versão pré-compilada do driver do Postgres (não precisa de gcc/libpq-dev)
RUN pip install --no-cache-dir psycopg2-binary

# Copia o restante do código do projeto
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]