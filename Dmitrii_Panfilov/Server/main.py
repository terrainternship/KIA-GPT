from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request
from fastapi.responses import StreamingResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Optional
from pydantic import BaseModel
import cv2
import numpy as np
from PIL import Image
import glob
import os
# import torch
# torch.cuda.is_available = lambda : False  # принудительно использовать только CPU для PyTorch

default_kbl_path = './kblist/'  # Путь по умолчанию, где хранятся файлы Базы Знаний

app = FastAPI(title="KIA GPT System API", version="0.1.0", debug=True)  # Инициализация FastAPI

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_latest_kblist(path):  # Функция для выбора самой последней Базы Знаний в формате MarkDown (*.md)
    list_of_files = glob.glob(f'{path}*.md')
    if not list_of_files:
        return None  # Ни одного файла БЗ не найдено
    latest_kblist = max(list_of_files, key=os.path.getctime)  # Выбираем самый свежий файл БЗ
    print(f'♻️  Last KB List: {latest_kblist}')
    return latest_kblist


# Добавление статических файлов
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    kblist_files = list_kblist()  # это словарь
    print(f"\n🛒 Список Доступных Баз Знаний: {kblist_files['KB List']}")
    return templates.TemplateResponse("index.html", {"request": request, "kblist": kblist_files['KB List']})


@app.get('/info')
def read_root():
    return {'Project 2023': '🤖 KIA GPT System - "Создание нейро-консультанта для ответов на вопросы клиентов" [г. Москва, 2023 г.]'}


@app.get('/kblist')
def list_models():
    kblist_dir = "kblist"
    kblist = []

    for filename in os.listdir(kblist_dir):
        if filename.endswith(".h5") or filename.endswith(".md"):  # Расширения файлов БЗ
            kblist.append(filename)
    #return JSONResponse(content={"KB List": kblist})
    return {"KB List": kblist}


@app.post('/predict')
async def predict():
  pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
