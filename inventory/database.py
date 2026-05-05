import os
from dotenv import load_dotenv
from redis_om import get_redis_connection

# Učitavamo promenljive iz .env fajla
load_dotenv()

# Izvlačimo podatke koristeći os.getenv
redis = get_redis_connection(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True
)