from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

app = FastAPI()


class User(BaseModel):
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
    return sign_up

