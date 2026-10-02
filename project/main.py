from sqlalchemy import select
from urllib import request
from fastapi import FastAPI
import uvicorn
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models import Item
from db import Session, ItemsORM



app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



@app.get("/", tags=["abdullik"])
def read_index():
    return templates.TemplateResponse({"request": request}, "index.html")

@app.post("/items", tags=["items"])
def create_item(item: Item):
    with Session() as session:
        item_orm = ItemsORM(creator=item.creator, model=item.model, price=item.price, category=item.category)
        session.add(item_orm)
        session.commit()
        return "W"



@app.get("/items/{id_item}", tags=["items"])
def get_item(id_item: int):
    with Session() as session:
        result = session.execute(select(ItemsORM).where(ItemsORM.id == id_item))
        data = result.scalars().all()
        session.commit()
        print(data[0].id)
    return "WWW.abdullik.com", data



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)