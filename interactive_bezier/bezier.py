from typing import Union

from interactive_bezier.models import Layer, Point


def bezier_point(layer: Layer, step: float) -> Point:
    if len(layer) == 1:
        return layer.points[0]

    next_layer = Layer()

    for p1, p2 in zip(layer.points[:-1], layer.points[1:]):
        next_layer.add(
            Point(
                coor=(
                    round(p1.x + (p2.x - p1.x) * step),
                    round(p1.y + (p2.y - p1.y) * step),
                )
            )
        )

    return bezier_point(layer=next_layer, step=step)
