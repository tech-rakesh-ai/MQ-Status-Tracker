from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "MQ-Status- Tracker"
    PROJECT_DESCRIPTION: str = "Simple MQ Status Tracker."
    MONGO_DB_HOST: str = "localhost"
    MONGO_DB_PORT: int = 27017
    MONGO_DB: str = "mqtt_db"
    MONGO_COLLECTION: str = "msg"
    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_QUEUE_NAME: str = "mqtt_queue"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
