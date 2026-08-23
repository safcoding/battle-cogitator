from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.core import helpers
import backend.core.unit_datasheet as unit_datasheet

app = FastAPI()

available_units = {
    "astartes_unit": unit_datasheet.astartes_unit,
    "ts_cult_unit": unit_datasheet.ts_cult_unit
}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get("/units/{unit_id}/weapons")
def get_unit_weapons(unit_id):
    if unit_id in available_units:
        selected_unit = available_units[unit_id]
        weapon_grp = helpers.get_weapons(selected_unit)
        return weapon_grp
    else:
        raise HTTPException(status_code=404, detail="Unit not found") 



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id }