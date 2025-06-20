import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "enter-secret-key")
    MONGO_URI = os.environ.get("MONGO_URI", "enter-mongo-uri")
