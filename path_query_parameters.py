from fastapi import FastAPI

app = FastAPI()

# A small database of user details
user_details = [
    {
        "Name": "Angel",
        "Age": 24,
        "Phone": 2349044932417,
        "City": "Lagos"
    },
    {
        "Name": "Caleb",
        "Age": 19,
        "Phone": 2348143268535,
        "City": "Owerri"
    },
    {
        "Name": "Thomas",
        "Age": 27,
        "Phone": 2348073451986,
        "City": "Abuja"
    },
    {
        "Name": "Joseph",
        "Age": 29,
        "Phone": 2347018356285,
        "City": "Port Hacourt"
    }
]

# Endpoint using path parameter
@app.get("/objects/{no}")
async def read_object_path(no: int):
    return {"User Details": user_details[no]}

# Endpoint using query parameter
@app.get("/objects/")
async def read_object_query(no: int):
    return {"User Details": user_details[no]}




# http://127.0.0.1:8000/objects/?no=0