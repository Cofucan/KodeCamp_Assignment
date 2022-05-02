from uuid import UUID
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

app = FastAPI()

db = {}

class User(BaseModel):
    id = UUID
    first_name: str = Field(..., max_length=50, min_length=3)
    middle_name: Optional[str] = Field(None, max_length=50, min_length=3)
    surname: str = Field(..., max_length=50, min_length=3)
    phone: str = Field(..., max_length=13, regex="\d{10}")      # To make sure that the phone number entered is between 10 to 13 digits
    email: EmailStr
    password: str = Field(..., max_length=20, min_length=8)
    birth_year: Optional[str] = Field(None, max_length=4, regex="\d{4}")     # Regular expression to make sure that the year is 4 digits
    birth_month: int = Field(..., le=12) 
    birth_date: int = Field(..., le=31)
    gender: str = Field(..., max_length=15, min_length=3)

@app.post("/signup/")
async def create_account(sign_up: User):
    """Create user account."""
    if sign_up.email in db.keys():
        raise HTTPException(status_code=404, detail="Sorry, this email already exists in our database")
    db[sign_up.email] = sign_up
    return sign_up

@app.get("/acounts/")
async def get_all_accounts():
    """Show all accounts in database."""
    return db