# gunicorn_config.py

# Número de workers y threads
workers = 5
threads = 2

# Máximo número de conexiones por worker
# worker_connections = 10

# Configuración de tiempo de espera
timeout = 130

# Dirección y puerto de binding
bind = "0.0.0.0:5050"
