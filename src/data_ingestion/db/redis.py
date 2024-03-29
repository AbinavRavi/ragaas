from redis import Redis
import os
from dotenv import load_dotenv


class RedisOps:
    def __init__(self, host, port, password):
        load_dotenv()
        self.host = os.getenv("REDIS_HOST")
        self.port = os.getenv("REDIS_PORT")
        self.password = os.getenv("REDIS_PASSWORD")
        self.redis = Redis(host=host, port=port, password=password)

    def set(self, key, value):
        self.redis.set(key, value)

    def get(self, key):
        return self.redis.get(key)

    def delete(self, key):
        self.redis.delete(key)

    def close(self):
        self.redis.close()
