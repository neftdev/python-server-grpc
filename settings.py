import os
from dotenv import load_dotenv

load_dotenv()

MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = int(os.environ.get("MONGO_PORT"))
MONGO_DB = os.environ.get("MONGO_DB")
