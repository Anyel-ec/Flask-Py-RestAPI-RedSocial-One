import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env

class AppEnvironment:
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")
    API_COMMENT = os.getenv("API_COMMENT", "/comment/")