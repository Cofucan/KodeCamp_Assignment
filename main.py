from fastapi import FastAPI, status

app = FastAPI()

@app.get("/")
def root():
    return "KodeCamp Intermediate Python Assignment"

@app.post("/records", status_code=status.HTTP_201_CREATED)
def create_record():
    return "create individual record"

@app.get("/records/{id}")
def read_record(id: int):
    return "read individual record by id {id}"

@app.put("/records/{id}")
def update_record(id: int):
    return "update individual record by id {id}"

@app.delete("/records/{id}")
def delete_record(id: int):
    return "delete individual record by id {id}"

@app.get("/records")
def read_all_records():
    return "read all records"