from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logging.info("[API 2] Ready to serve requests")
@app.get("/")
async def api2():
    logging.info("[API 2] Received request from API 1")
    logging.info("[API 2] Sending response to API 1")
    return {"message": "สวัสดีค่ะ พวกเราทีมวัดไร่ขิง"}