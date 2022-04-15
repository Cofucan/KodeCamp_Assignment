from fastapi import FastAPI, status
from database import Base, engine
from pydantic import BaseModel

# Create Post base model
class PostRequest(BaseModel):
    name = str
    age = int
    message = str
    createDate = str

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()


@app.get("/")
def root():
    return "KodeCamp Intermediate Python Assignment"

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: PostRequest):
    return "create individual post"

@app.get("/posts/{id}")
def read_post(id: int):
    return "read individual post by id {id}"

@app.put("/posts/{id}")
def update_post(id: int):
    return "update individual post by id {id}"

@app.delete("/posts/{id}")
def delete_post(id: int):
    return "delete individual post by id {id}"

@app.get("/posts")
def read_all_posts():
    return "read all posts"