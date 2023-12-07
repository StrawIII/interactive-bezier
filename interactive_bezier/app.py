from typing import TYPE_CHECKING

import pygame as pg

from interactive_bezier.bezier import bezier_point
from interactive_bezier.models import Layer, MouseButton, Point

if TYPE_CHECKING:
    from config import Config


class App:
    def __init__(self, config: "Config"):
        self.config = config

    def setup(self):
        if self.config.user_settings.fullscreen:
            self.display_size = (pg.display.Info().current_w, pg.display.Info().current_h)
        else:
            self.display_size = tuple(self.config.user_settings.resolution)

        self.surface = pg.display.set_mode(size=self.display_size)
        self.clock = pg.time.Clock()
        self.surface.fill(color=pg.Color(self.config.user_settings.background_color))
        self.layer = Layer()

    def refresh(self):
        step_count = 10_000

        self.surface.fill(color=pg.Color(self.config.user_settings.background_color))

        for p1, p2 in zip(self.layer.points[:-1], self.layer.points[1:]):
            self.draw_line(p1=p1, p2=p2)

        for point in self.layer:
            self.draw_point(point=point)

        for step in range(0, step_count, 1):
            self.draw_point(point=bezier_point(layer=self.layer, step=(step / step_count)))

    def reset(self):
        self.layer = Layer()
        self.surface.fill(color=pg.Color(self.config.user_settings.background_color))

    def draw_point(self, point: Point):
        pg.draw.circle(
            surface=self.surface,
            color=self.config.user_settings.point.color,
            center=point.coor,
            radius=self.config.user_settings.point.diameter,
        )

    def draw_line(self, p1: Point, p2: Point):
        pg.draw.aaline(
            surface=self.surface,
            color=self.config.user_settings.line.color,
            start_pos=p1.coor,
            end_pos=p2.coor,
        )

    def mainloop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    return

                if event.type == pg.MOUSEBUTTONUP and event.button == MouseButton.RIGHT.value:
                    self.layer.add(point=Point(coor=pg.mouse.get_pos()))
                    self.refresh()

                if event.type == pg.MOUSEBUTTONDOWN and event.button == MouseButton.LEFT.value:
                    # TODO finish moving point
                    mouse_coor = pg.mouse.get_pos()

                    for point in self.layer:
                        if point.is_clicked(mouse_coor=mouse_coor):
                            point.move(coor=mouse_coor)
                            self.refresh()

                if event.type == pg.KEYDOWN and event.key == pg.K_r:
                    self.reset()

            pg.display.flip()
            self.clock.tick(self.config.user_settings.framerate)
