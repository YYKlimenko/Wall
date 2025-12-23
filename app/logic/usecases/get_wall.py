from typing import Protocol

from pydantic import UUID4
from logic.domains import Wall


class WallRepository(Protocol):
    async def get(self, user_id: UUID4) -> Wall:
        ...


class GetWallUsecase:
    def __init__(self, wall_repository: WallRepository):
        self.wall_repository = wall_repository

    async def __call__(self, user_id: UUID4) -> Wall:
        return await self.wall_repository.get(user_id)
