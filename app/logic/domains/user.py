from datetime import datetime

from pydantic import BaseModel, UUID4


class User(BaseModel):
    uuid: UUID4
    visited_at: datetime
