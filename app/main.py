# -*- coding: utf-8 -*-
# @Author: gary
# @Date:   2023-14-05 

from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List
import numpy as np
import logging
import cv2
import ast
import base64
# import onnxruntime as ort

TITLE = "People tracking"
DESC = """Inferencing for yolov7 model.
    """
VERSION = "0.1.1"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# test endpoint 
@app.get("/test")
async def test():
    return {
        "route": "SUCESS"
    }

# detect route 
@app.post("/inference")
async def detect_inference(
    # track_terms : str = Form(..., title="input people/car"),
    track_terms : str = Form(..., title="Input image base64 string"),
    source : UploadFile = File(...)

):
    return {
        "route": "SUCESS"
    }