# Module 2: Routing

## Notes

<details><summary>GET requests</summary>

- It is discouraged to send data using [`GET`](https://fastapi.tiangolo.com/tutorial/body/#request-body)
</details>

<details><summary>__init__.py files</summary>

- Adding `__init__.py` files to a directory 
  - turns it into a python module
  - allows for easier importing
  - See [reddit thread](https://www.reddit.com/r/learnpython/comments/q8yjvw/still_confused_about_what_init_should_be_used_for/)
</details>

## Steps

### Create `Item` pydantic models

<details><summary>Create directory for `Item`</summary>

- inside `app` directory, create `item` folder
- add `init.py`
- create `model.py`, and add code:
    ```py
    from datetime import datetime, timezone
    from pydantic import BaseModel, Field
        
    class ItemRequest(BaseModel):
        name: str
        quantity: int
        note: str | None = None
        
    class ItemResponse(ItemRequest):
        id: int
        created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))
        updated_at: datetime | None = None
    ```
</details>

<details><summary>Misc notes</summary>

- Pydantic "validation" refers to instantiating a python model from some input against predefined "model" containing field types/ constraints
- Pydantic raises `ValidationError` if validation fails
    ```py
    try:
        User(**some_json_data)
    except ValidationError as e: # catch the validation error
    ```
- `BaseModel` provides useful fields and methods such as `model_dump` and `model_validate`
- Pydantic model field declaration
  - Optional & default value fields: `city: str | None = "N/A"`, Ex: `age: int | None = Field(default=10)`
  - can use `Field()` to define additional functionalities and constraints 
</details>

### Setup JSON DB

<details><summary>Initialize & load JSON database</summary>

- Create JSON file with 100 `Item` entities in project root (`./db/items.json`)
- Create `core` directory in `app` with `db.py`, with the following code:
    ```py
    import json

    def load_json_db():
        try:
            with open('./db/items.json', 'r') as file:
                data = json.load(file)
            print("JSON database loaded successfully")
            return data
        
        except FileNotFoundError:
            print("File Not found")
        except json.JSONDecodeError:
            print("Malformed JSON, unable to decode")
    ```
</details>

<details><summary>Initialize db before app startup</summary>

- Add the following code to `main.py`
    ```py
    from contextlib import asynccontextmanager

    from fastapi import FastAPI
    from app.core.db import load_json_db as init_db

    @asynccontextmanager
    async def startup(app: FastAPI):
        print("Starting FastAPI backend...")
        db = init_db()
        print("Database loaded")
        yield
        print("...stopping FastAPI backend")
    ```
</details>

<details><summary>Implement DB CRUD operations</summary>

- Add to `repo.py` in `item` directory

    ```python
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
    ```
</details>

<details><summary>Misc Notes</summary>

`TypeAdapter`
- Allows you to validate multiple pydantic models (ex: list), see docs [example](https://docs.pydantic.dev/latest/examples/files/#json-data)
</details>


---

TODO
- export `init_db` from `core` (idea is to swap out implementations of `init_db` with SQL, NoSQL, JSON, etc loading)
- Create core/repository for defining CRUD operations