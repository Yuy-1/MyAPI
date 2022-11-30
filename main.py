from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/post")
def get_post():
    return {'data': 'This is your posts'}


@app.post("/createposts")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return{"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

