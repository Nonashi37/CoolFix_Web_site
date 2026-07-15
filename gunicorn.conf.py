bind = "0.0.0.0:8000"

# Формула: (2 × ядра CPU) + 1. Проверь свои ядра: nproc
workers = 3

worker_class = "sync"
timeout = 120
keepalive = 5

max_requests = 1000
max_requests_jitter = 100

accesslog = "-"
errorlog = "-"
capture_output = True
loglevel = "info"