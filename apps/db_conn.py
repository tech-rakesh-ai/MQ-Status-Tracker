from fastapi import HTTPException
from pymongo import MongoClient

from apps.config import settings


def init_mongo_db():
    try:
        client = MongoClient(settings.MONGO_DB_HOST, settings.MONGO_DB_PORT)
        return client
    except Exception as e:
        print(f"Error creating MongoDB client: {e}")
        raise HTTPException(status_code=500, detail=str(e))
