from pydantic import BaseModel


class Wall(BaseModel):
    posts: list[Post]
