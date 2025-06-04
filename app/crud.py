from app.database import events
from app.event_queue import enqueue_event

def save_score_event(score_data):
    try:
        events.insert_one(score_data)
    except Exception:
        pass  # log

    try:
        enqueue_event(score_data)
        return "queued"
    except Exception:
        return "enqueue_failed"
