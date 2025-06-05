import logging
from app.database import events
from app.event_queue import enqueue_event

logger = logging.getLogger(__name__)

async def save_score_event(score_data):
    """Persist score event to MongoDB and enqueue for webhook."""
    try:
        result = await events.insert_one(score_data)
        logger.info("[MONGO] SALVO COM ID: %s", result.inserted_id)
    except Exception as e:
        logger.error("[MONGO] ERRO AO INSERIR: %s", e)

    try:
        enqueue_event(score_data)
        logger.info("[QUEUE] Evento enfileirado com sucesso.")
        return "queued"
    except Exception as e:
        logger.error("[QUEUE] Falha ao enfileirar evento: %s", e)
        return "enqueue_failed"
