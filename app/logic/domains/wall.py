from pydantic import BaseModel, UUID4


class Wall(BaseModel):
    posts: list[UUID4]
