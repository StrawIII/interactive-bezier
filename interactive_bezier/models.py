from enum import Enum
from typing import List, Tuple

from pydantic import BaseModel


class MouseButton(Enum):
    LEFT = 1
    RIGHT = 3


class Point(BaseModel):
    coor: Tuple[int, int]

    def __eq__(self, other):
        return self.coor == other

    @property
    def x(self):
        return self.coor[0]

    @property
    def y(self):
        return self.coor[1]

    def move(self, coor: Tuple[int, int]):
        self.coor = coor

    def is_clicked(self, mouse_coor: Tuple[int, int]) -> bool:
        # TODO make this exect (new attribute size is needed)
        if mouse_coor[0] in range(self.coor[0] - 10, self.coor[0] + 10) and mouse_coor[1] in range(
            self.coor[1] - 10, self.coor[1] + 10
        ):
            return True

        return False


class Layer(BaseModel):
    points: List[Point] = []

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return iter(self.points)

    def add(self, point: Point):
        self.points.append(point)

    def remove(self, point: Point):
        self.points.remove(point)
