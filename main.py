import uvicorn
from apps import create_app
from multiprocessing import Process

from apps.tracker.utils import start_mqtt_consumer

app = create_app()

if __name__ == '__main__':
    consumer_process = Process(target=start_mqtt_consumer)
    consumer_process.start()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
    consumer_process.join()
