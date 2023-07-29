from typing import Optional

from pydantic import BaseModel


class BaseSchema(BaseModel):
    id: Optional[str] = None

    class Config:
        from_attributes = True
