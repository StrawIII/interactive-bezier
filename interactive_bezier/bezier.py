from typing import List

import numpy as np

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


def bezier_point_numpy(layer: np.ndarray, step: float) -> np.ndarray:
    layer_lenght = len(layer)

    if layer_lenght == 1:
        return layer[0]

    next_layer = np.empty(shape=(layer_lenght - 1, 2), dtype=np.float32)

    for i in np.arange(layer_lenght - 1):
        next_layer[i][0] = layer[i][0] + (layer[i + 1][0] - layer[i][0]) * step
        next_layer[i][1] = layer[i][1] + (layer[i + 1][1] - layer[i][1]) * step

    return bezier_point_numpy(layer=next_layer, step=step)
