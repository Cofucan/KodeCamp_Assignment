from fastapi import FastAPI, Form, UploadFile
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.post("/upload_file/")
async def new_upload_file(file: Optional[UploadFile] = None):
    if not file:
        # return {"error" : ValueError("no file")}      # Tried to raise an exception here but it dosen't print any error message
        return {"status" : "no file uploaded"}
    else:
        return {"filename" : file.filename, "filetype" : file.content_type}









