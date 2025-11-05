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