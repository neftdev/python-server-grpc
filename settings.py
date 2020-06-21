import os
from dotenv import load_dotenv

load_dotenv()

MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = int(os.environ.get("MONGO_PORT"))
MONGO_DB = os.environ.get("MONGO_DB")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT"))
REDIS_DB = int(os.environ.get("REDIS_DB"))
