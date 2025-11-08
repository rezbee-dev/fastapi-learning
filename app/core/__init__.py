from typing import Annotated
from fastapi import Depends
from app.core.db import load_json_db

Database = Annotated[list, Depends(load_json_db)]
