#!/bin/bash

# Defina suas variáveis
PROJECT_ID="foundlab-core-460315"
SERVICE_NAME="foundlab-api"
REGION="us-central1"
IMAGE="gcr.io/$PROJECT_ID/$SERVICE_NAME"

# Build da imagem com Cloud Build
gcloud builds submit --tag $IMAGE

# Deploy para o Cloud Run
gcloud run deploy $SERVICE_NAME \
  --image $IMAGE \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars API_KEY=testkey
