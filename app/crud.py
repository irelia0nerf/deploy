from app.database import events
from app.event_queue import enqueue_event

def save_score_event(score_data):
    try:
        result = events.insert_one(score_data)
        print(f"[MONGO] SALVO COM ID: {result.inserted_id}")
    except Exception as e:
        print(f"[MONGO] ERRO AO INSERIR: {e}")

    try:
        enqueue_event(score_data)
        print("[QUEUE] Evento enfileirado com sucesso.")
        return "queued"
    except Exception as e:
        print(f"[QUEUE] Falha ao enfileirar evento: {e}")
        return "enqueue_failed"
