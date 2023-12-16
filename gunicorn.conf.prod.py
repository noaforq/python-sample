

worker_class = "uvicorn.workers.UvicornWorker"
# (2023/6/5 workers( ワーカー数 )をCPUに応じた数を設定するとメモリ不足で落ちてしまうためコメントアウト)
# workers = psutil.cpu_count(logical=True) * 2 + 1
workers = 1

# https://github.com/benoitc/gunicorn/pull/862#issuecomment-53175919
# workersをCPUに応じた数に設定できるようになったらコメントアウトを解除
# max_requests = 500
# max_requests_jitter = 200

# https://cloud.google.com/load-balancing/docs/https#timeouts_and_retries
keepalive = 620

timeout = 360
loglevel = "info"
