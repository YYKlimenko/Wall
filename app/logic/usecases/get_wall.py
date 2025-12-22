from typing import Protocol


class Commiter(Protocol):
    ...


class WallRepository(Protocol):
    def get(self, user_id: int) -> Wall:
        ...

    def create(self, user_id: int) -> Wall:
        ...


class GetWallUsecase:
    def __init__(self, session: Commiter, wall_repository: WallRepository):
        self.wall_repository = wall_repository

    def execute(self, user_id: int) -> Wall:
        return self.wall_repository.get_wall(user_id)