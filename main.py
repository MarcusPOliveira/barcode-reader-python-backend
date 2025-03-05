import os
from ctypes import cdll
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import cv2
from pyzbar.pyzbar import decode
import numpy as np
from typing import List

# Força o carregamento do libzbar.so
try:
    libzbar_path = "/usr/local/lib/libzbar.so"
    cdll.LoadLibrary(libzbar_path)
    print(f"✅ Biblioteca ZBar carregada com sucesso de {libzbar_path}")
except OSError:
    print(f"❌ Erro ao carregar a biblioteca ZBar em {libzbar_path}")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.post("/api/read-barcodes")
async def read_barcodes(images: List[UploadFile] = File(...)):
    all_codes = []

    for image in images:
        try:
            contents = await image.read()
            nparr = np.frombuffer(contents, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            barcodes = decode(gray)

            codes = [b.data.decode("utf-8") for b in barcodes]
            all_codes.extend(codes)

        except Exception as e:
            return {"success": False, "error": str(e)}

    return {"success": True, "codes": all_codes}