from time import perf_counter

import numpy as np

from interactive_bezier.bezier import bezier_point, bezier_point_numpy
from interactive_bezier.models import Layer, Point

STEP_COUNT = 1000
points_coor = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 0),
    (4, 7),
]
l1 = Layer(points=[Point(coor=coor) for coor in points_coor])
l2 = np.array(object=points_coor, dtype=np.float32)


def bezier():
    start = perf_counter()

    for step in range(0, STEP_COUNT, 1):
        bezier_point(layer=l1, step=step / STEP_COUNT)

    stop = perf_counter()
    return f"bezier:       {stop - start:.5f} s"


def bezier_numpy():
    start = perf_counter()

    for step in np.arange(0, 1, 1 / STEP_COUNT):
        bezier_point_numpy(layer=l2, step=step)

    stop = perf_counter()
    return f"bezier numpy: {stop - start:.5f} s"


if __name__ == "__main__":
    print(f"step count: {STEP_COUNT}")
    print(bezier())
    print(bezier_numpy())
