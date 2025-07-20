from fastapi import FastAPI
import logging
import requests

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logging.info("[API 1] Ready to serve requests")
@app.get("/")
async def api1():
    logging.info("[API 1] Received request from user")
    response = requests.get("http://api2:8002/")
    logging.info("[API 1] Received response from API 2")
    logging.info("[API 1] Sending response to user")
    return response.json()