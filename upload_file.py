from fastapi import FastAPI, Form, UploadFile, status, HTTPException
from typing import Optional

app = FastAPI()

@app.post("/upload_file/")
async def new_upload_file(username: str = Form(...), pin: int = Form(..., ge=1000, le=9999), file: Optional[UploadFile] = None):
    if not file:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no file was uploaded")
    return {"username" : username,
            "pin"      : pin,
            "Filename" : file.filename, 
            "filetype" : file.content_type}
