import queue
import threading
import time
import requests
import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "http://localhost:8001/webhook/score-event/")
event_queue = queue.Queue()

def send_event(event):
    retries = 3
    for attempt in range(retries):
        try:
            r = requests.post(WEBHOOK_URL, json=event, timeout=5)
            if r.status_code == 200:
                print(f"[Webhook] Entregue com sucesso.")
                return "delivered"
            else:
                print(f"[Webhook] Erro HTTP {r.status_code}. Tentando novamente...")
        except Exception as e:
            print(f"[Webhook] Falha no envio: {e}")
        time.sleep(2)
    print("[Webhook] Todas as tentativas falharam.")
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
