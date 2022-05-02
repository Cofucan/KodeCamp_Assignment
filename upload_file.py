from http.client import HTTPException
from fastapi import FastAPI, Form, UploadFile, status
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()


@app.post("/upload_file/")
async def new_upload_file(username: str = Form(...), pin: int = Form(..., ge=1000, le=9999), file: Optional[UploadFile] = None):
    if not file:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no file was uploaded")
        raise HTTPException(status_code=404, detail="no file was uploaded")
        
        # return JSONResponse(
        #         status_code=status.HTTP_404_NOT_FOUND,
        #         content={"message": "no file uploaded"}
        #     )
        # note = JSONResponse(
        #         status_code=status.HTTP_404_NOT_FOUND,
        #         content={"message": "no file uploaded"}
        #     )

        # return {"username" : username,
        #         "pin"      : pin,
        #         "file"     : note.body,
        #         "error"    : note.status_code}
  
    return {"username" : username,
            "pin"      : pin,
            "Filename" : file.filename, 
            "filetype" : file.content_type}

