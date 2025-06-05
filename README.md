===================================================
           FOUNDLAB API — GUIA DE USO RÁPIDO
===================================================

1. PRÉ-REQUISITOS

-----------------

- Conta Google Cloud
- Conta MongoDB Atlas
- Docker instalado (para build local)
- Google Cloud SDK instalado e autenticado

2. COMO RODAR O PROJETO LOCALMENTE

----------------------------------
a) Clone o repositório:
   git clone <https://github.com/Zanecruise/deploy_modulos_found>

b) Crie o arquivo `.env` na raiz do projeto com:
   API_KEY=SuperSenhaUltraSecreta_2024!
    MONGODB_URI="mongodb+srv://usuario:senha123@cluster0.exemplo.mongodb.net/banco_ficticio?retryWrites=true&w=majority&appName=Cluster0"
    (Substitua `usuario`, `senha123`, `cluster0.exemplo.mongodb.net` e `banco_ficticio` pelos seus dados reais do MongoDB Atlas)

c) Build & execute usando Docker:
   docker build -t foundlab-api .
   docker run --env-file .env -p 8000:8080 foundlab-api

d) (ou) Rode com Docker Compose (para local):
   docker-compose up --build

e) Acesse:
   <http://localhost:8000/health/>
   Documentação Swagger: <http://localhost:8000/docs>

3. COMO FAZER DEPLOY NO GOOGLE CLOUD RUN

----------------------------------------
a) Faça build e push da imagem Docker:
   docker build -t gcr.io/SEU_PROJECT_ID/foundlab-api .
   docker push gcr.io/SEU_PROJECT_ID/foundlab-api

b) Deploy:
   gcloud run deploy foundlab-api \
     --image gcr.io/SEU_PROJECT_ID/foundlab-api \
     --platform managed \
     --region southamerica-east1 \
     --allow-unauthenticated \
     --set-env-vars API_KEY=SuperSenhaUltraSecreta_2024!,MONGODB_URI="mongodb+srv://Zane:root@cluster0.kvya5a3.mongodb.net/foundlab?retryWrites=true&w=majority&appName=Cluster0"

c) Use a URL fornecida ao final do deploy para testar as rotas.

4. ROTAS DISPONÍVEIS E TESTES

-----------------------------

-------------------------------------

a) Healthcheck
-------------------------------------

GET /health/
Exemplo:
curl <https://foundlab-api-xxxxxx.run.app/health/>

-------------------------------------

b) Score — calcula e salva score
-------------------------------------

POST /score/
Headers:
  Content-Type: application/json
  x-api-key: SuperSenhaUltraSecreta_2024!

Body exemplo:
{
  "wallet_address": "0xteste123",
  "tx_count": 10,
  "balance": 100.0,
  "risk_inputs": ["input1", "input2"]
}

Exemplo CURL:
curl -X POST <https://foundlab-api-xxxxxx.run.app/score/> \
  -H "Content-Type: application/json" \
  -H "x-api-key: SuperSenhaUltraSecreta_2024!" \
  -d '{
        "wallet_address": "0xteste123",
        "tx_count": 10,
        "balance": 100.0,
        "risk_inputs": ["input1", "input2"]
      }'

-------------------------------------

c) Flags — consultar flags ativas
-------------------------------------

GET /flags/
Headers:
  x-api-key: SuperSenhaUltraSecreta_2024!

Exemplo CURL:
curl -X GET <https://foundlab-api-xxxxxx.run.app/flags/> \
  -H "x-api-key: SuperSenhaUltraSecreta_2024!"

-------------------------------------

d) Flags — adicionar/remover flag
-------------------------------------

POST /flags/
Headers:
  Content-Type: application/json
  x-api-key: SuperSenhaUltraSecreta_2024!

Body exemplo para adicionar:
{
  "flag": "nova_flag",
  "action": "add"
}

Body exemplo para remover:
{
  "flag": "nova_flag",
  "action": "remove"
}

Exemplo CURL (remover):
curl -X POST <https://foundlab-api-xxxxxx.run.app/flags/> \
  -H "Content-Type: application/json" \
  -H "x-api-key: SuperSenhaUltraSecreta_2024!" \
  -d '{"flag":"nova_flag","action":"remove"}'

-------------------------------------

e) Documentação Swagger (interativo)
-------------------------------------

GET /docs
Exemplo:
<https://foundlab-api-xxxxxx.run.app/docs>

-------------------------------------------------

5. TECNOLOGIAS UTILIZADAS

-------------------------------------------------

- **FastAPI**: Framework Python para APIs web.
- **Uvicorn**: ASGI server para rodar o FastAPI.
- **Docker**: Containerização da aplicação.
- **Google Cloud Run**: Deploy escalável sem servidor.
- **MongoDB Atlas**: Banco de dados MongoDB gerenciado em nuvem.
- **PyMongo**: Driver Python para MongoDB.
- **Python-dotenv**: Carregamento de variáveis de ambiente.
- **Pydantic**: Validação e parsing de dados.
- **Requests**: Para integração assíncrona e webhooks (eventos).

-------------------------------------------------

6. OBSERVAÇÕES IMPORTANTES

-------------------------------------------------

- A API utiliza autenticação por API_KEY para rotas protegidas.
- Os dados do endpoint `/score/` são persistidos na collection `score_events` no banco MongoDB Atlas.
- O endpoint `/health/` é público e serve para monitoramento.
- Sempre manter as dependências atualizadas no requirements.txt.

===================================================
