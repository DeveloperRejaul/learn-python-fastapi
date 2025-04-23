from fastapi import FastAPI

app = FastAPI(version="0.1.0", title="My API", description="This is my API", docs_url="/docs" )

list = ["item1", "item2", "item3"]


@app.get("/")
async def root():
    list.append("item")
    return {"message":list}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}
