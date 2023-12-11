from enum import Enum
from typing import List, Tuple

import numpy as np
from pydantic import BaseModel


class MouseButton(Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3
    WHEELUP = 4
    WHEELDONW = 5
    MOUSE_5 = 6
    MOUSE_6 = 7


class Point(BaseModel):
    coor: Tuple[int, int]

    @property
    def x(self):
        return self.coor[0]

    @property
    def y(self):
        return self.coor[1]

    def move(self, movement: Tuple[int, int]):
        self.coor = tuple(x + y for x, y in zip(self.coor, movement))

    def is_over(self, mouse_coor: Tuple[int, int]) -> bool:
        # TODO make this exect (new attribute size is needed)
        return mouse_coor[0] in range(self.coor[0] - 10, self.coor[0] + 10) and mouse_coor[1] in range(
            self.coor[1] - 10, self.coor[1] + 10
        )


class Layer(BaseModel):
    points: List[Point] = []

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return iter(self.points)

    @property
    def as_ndarray(self) -> np.ndarray:
        return np.array(object=[point.coor for point in self.points], dtype=np.float32)

    def add(self, point: Point):
        self.points.append(point)

    def remove(self, point: Point):
        self.points.remove(point)
