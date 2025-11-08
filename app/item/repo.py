from .model import ItemResponse as Item

def read_by_id(db: list[Item], id: int):
    return [item for item in db if item.id == id] 

def read_all(db: list[Item], skip: int = 0, limit: int = 0):
    # set skip & limit to return entire db if not valid
    if(skip < 0 or skip >= len(db)):
        skip = 0
        
    if(limit < -1 or limit > len(db)):
        limit = len(db)
        
    return db[skip:limit]

def update_by_id(db: list[Item], new_item: Item):
    for index, item in enumerate(db):
        if item.id == new_item.id:
            db[index] = new_item
            return db[index]

def delete_by_id(db: list[Item], id: int):
    for index, item in enumerate(db):
        if item.id == id:
            del db[index]
            return
        
def create(db: list[Item], new_item: Item):
    # check if new_item.id already exists or not
    if not [item for item in db if item.id == new_item.id]:
        db.append(new_item)
    