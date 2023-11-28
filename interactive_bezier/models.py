from pydantic import BaseModel
from typing import List
from enum import StrEnum

class Color(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    PURPLE = "purple"

class Shape(BaseModel):
    size: float #  pixels -> int?
    color: Color
    
    def draw(self):
        pass


class Point(Shape):
    x: float #  pixels?
    y: float #  pixels?
    
    def px_to_cart(self):
        pass
    
    def cart_to_px(self):
        pass

    
class Line(Shape):
    p1: Point
    p2: Point


class Layer(BaseModel):
    points: List[Point]