# FoundLab ScoreLab MVP

Infraestrutura mínima de API para score e flags dinâmicas, dockerizada, pronta para acoplar lógica institucional FoundLab.

## Subir Localmente

```bash
cp .env.example .env
docker-compose up --build
```

API rodando em [http://localhost:8000/docs](http://localhost:8000/docs)

## Testar Endpoints

- **Healthcheck:** `GET /health/`
- **Score:** `POST /score/`
- **Flags:** `GET /flags/` e `POST /flags/`

## Testes

```bash
pip install -r requirements.txt
pytest tests/
```
