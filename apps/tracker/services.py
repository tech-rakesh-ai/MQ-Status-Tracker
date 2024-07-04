from fastapi import HTTPException
from datetime import datetime
from apps.config import settings
from apps.db_conn import init_mongo_db


async def status_count(start, end):
    try:
        start_time = datetime.fromisoformat(start)
        end_time = datetime.fromisoformat(end)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")

    pipeline = [
        {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]

    client = init_mongo_db()
    db = client[settings.MONGO_DB]
    collection = db[settings.MONGO_COLLECTION]
    result = list(collection.aggregate(pipeline))

    return result
