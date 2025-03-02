import os

CLUSTER_URLS = os.getenv('CLUSTER_URLS', 'http://app:8000/v1/group/').split(",")

CLIENT_TIMEOUT_SEC = os.getenv('CLIENT_TIMEOUT_SEC', 5)
CLIENT_MAX_CONNECTIONS = os.getenv('CLIENT_MAX_CONNECTIONS', None)
CLIENT_KEEPALIVE_CONNECTIONS = os.getenv('CLIENT_KEEPALIVE_CONNECTIONS', 10)
