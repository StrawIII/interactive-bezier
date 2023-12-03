from enum import Enum
from typing import TYPE_CHECKING, List, Tuple

import pygame
from pydantic import BaseModel, model_validator

if TYPE_CHECKING:
    from interactive_bezier.interactive_bezier import App


class Color(Enum):
    RED = (255, 0 ,0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (102, 0, 204)
    

class Shape(BaseModel):
    size: int  # pixels
    color: Color
    app: "App"
    
   


class Point(Shape):
    px_coor: Tuple[int, int]
    cart_coor: Tuple[float, float]

    @model_validator(mode="before")
    def px_to_cart(cls, values):
        ...
    
    @model_validator(mode="before")    
    def cart_to_px(csl, values):
        ...

    def draw(self):
        self.app.pygame.draw.circle(self.app.surface, color="white", center=self.px_coor, radius=5)

    
class Line(Shape):
    p1: Point
    p2: Point


class Layer(BaseModel):
    level: int
    points: List[Point]
