import queue
import threading
import time
import requests
import os
import logging

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "http://localhost:8001/webhook/score-event/")
event_queue = queue.Queue()
logger = logging.getLogger(__name__)

def send_event(event):
    retries = 3
    for attempt in range(retries):
        try:
            r = requests.post(WEBHOOK_URL, json=event, timeout=5)
            if r.status_code == 200:
                logger.info("[Webhook] Entregue com sucesso.")
                return "delivered"
            else:
                logger.warning("[Webhook] Erro HTTP %s. Tentando novamente...", r.status_code)
        except Exception as e:
            logger.error("[Webhook] Falha no envio: %s", e)
        time.sleep(2)
    logger.error("[Webhook] Todas as tentativas falharam.")
    return "failed"

def worker():
    while True:
        event = event_queue.get()
        if event is None:
            break
        send_event(event)
        event_queue.task_done()

# Iniciar thread da fila
thread = threading.Thread(target=worker, daemon=True)
thread.start()

def enqueue_event(event):
    event_queue.put(event)
