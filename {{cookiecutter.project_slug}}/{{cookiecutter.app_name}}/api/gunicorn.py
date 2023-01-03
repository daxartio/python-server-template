# https://docs.gunicorn.org/en/stable/settings.html

accesslog = '-'
bind = '0.0.0.0:80'
max_requests = 10000
max_requests_jitter = 100
user = 'root'
workers = 1
threads = 1
keepalive = 70
limit_request_line = 0
limit_request_field_size = 0
timeout = 60
worker_class = 'uvicorn.workers.UvicornH11Worker'
wsgi_app = 'app.api.asgi:app'
