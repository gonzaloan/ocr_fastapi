import asyncio
import os
import time
from typing import List

from fastapi import FastAPI, UploadFile, File

import ocr
import utils

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR"}


@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    tasks = []
    for img in Images:
        print("Images Uploaded: ", img.filename)
        temp_file = utils.save_file_to_server(img, path="./", save_as=img.filename)
        tasks.append(asyncio.create_task(ocr.read_image(temp_file)))
    text = await asyncio.gather(*tasks)
    for i in range(len(text)):
        response[Images[i].filename] = text[i]
    response["Time taken"] = round((time.time() - s), 2)
    return response
