from typing import Optional

from pydantic import Field

from src.database.schemas.base_schema import BaseSchema


class WorldSchema(BaseSchema):
    name: Optional[str] = None


class RequestWorld(BaseSchema):
    parameter: WorldSchema = Field(...)
