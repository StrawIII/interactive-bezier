from typing import TYPE_CHECKING

import numpy as np
import pygame as pg

from interactive_bezier.bezier import bezier_point_numpy
from interactive_bezier.models import Layer, MouseButton, Point

if TYPE_CHECKING:
    from config import Config


# hlavní třída GUI aplikace
class App:
    # konstruktor
    def __init__(self, config: "Config"):
        self.config = config

    # vlastní inicializace třídy
    def setup(self):
        if self.config.user_settings.fullscreen:
            self.display_size = (pg.display.Info().current_w, pg.display.Info().current_h)
        else:
            self.display_size = tuple(self.config.user_settings.resolution)

        self.surface = pg.display.set_mode(size=self.display_size)
        self.clock = pg.time.Clock()
        self.surface.fill(color=pg.Color(self.config.user_settings.background_color))
        self.layer = Layer()
        self.performance_mode = False

    # funkce pro vyčištění a vykreslení
    def refresh(self):
        if len(self.layer) <= self.config.user_settings.performance_mode_threshold:
            self.performance_mode = False
        else:
            self.performance_mode = True

        self.surface.fill(color=pg.Color(self.config.user_settings.background_color))

        for p1, p2 in zip(self.layer.points[:-1], self.layer.points[1:]):
            self.draw_line(p1=p1, p2=p2)

        for point in self.layer:
            self.draw_point(point=point)

        for step in np.arange(0, 1, 1 / self.config.user_settings.step_count):
            coor = (round(coor) for coor in bezier_point_numpy(layer=self.layer.as_ndarray, step=step))

            self.draw_point(point=Point(coor=coor))

    # funkce pro vyčištění a promazání dat
    def reset(self):
        self.layer = Layer()
        self.surface.fill(color=pg.Color(self.config.user_settings.background_color))
        self.performance_mode = False

    # funkce pro vykreslení bodu
    def draw_point(self, point: Point):
        pg.draw.circle(
            surface=self.surface,
            color=self.config.user_settings.point.color,
            center=point.coor,
            radius=self.config.user_settings.point.diameter,
        )

    # funkce pro vykreslení čáry
    def draw_line(self, p1: Point, p2: Point):
        pg.draw.aaline(
            surface=self.surface,
            color=self.config.user_settings.line.color,
            start_pos=p1.coor,
            end_pos=p2.coor,
        )

    # funkce hlavní smyčky
    def mainloop(self):
        selected_point = None

        while True:
            # iteruj přes všechny eventy, které se během framu staly
            for event in pg.event.get():
                # pokud je kliknuto na křížek nebo je stisknut ESC ukonči aplikaci
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    return

                # pokud je stisknuto pravé tlačítko myši
                if event.type == pg.MOUSEBUTTONUP and event.button == MouseButton.RIGHT.value:
                    # iteruj přes všechny body ve vrstvě
                    for point in self.layer:
                        # pokud je myš nad již existujícím bodě smaž ho
                        if point.is_over(mouse_coor=pg.mouse.get_pos()):
                            self.layer.remove(point=point)
                            break
                    # vytvoř nový bod
                    else:
                        self.layer.add(point=Point(coor=pg.mouse.get_pos()))

                    self.refresh()

                # pokud je stisknuto levé tlačítko myši
                if event.type == pg.MOUSEBUTTONDOWN and event.button == MouseButton.LEFT.value:
                    mouse_coor = pg.mouse.get_pos()

                    # iteruj přes všechny body ve vrstvě
                    for point in self.layer:
                        # pokud je myš nad nějakým bodem ulož ho jako "selected"
                        if point.is_over(mouse_coor=mouse_coor):
                            selected_point = point

                # pokud je uvolněno levé tlačítko myši a existuje "selected" bod
                if (
                    event.type == pg.MOUSEBUTTONUP
                    and event.button == MouseButton.LEFT.value
                    and selected_point
                    and self.performance_mode
                ):
                    # posuň bod na místo myši
                    selected_point.coor = pg.mouse.get_pos()
                    selected_point = None
                    self.refresh()

                # pokud je myš v pohybu a existuje "selected" bod
                if event.type == pg.MOUSEMOTION and selected_point and not self.performance_mode:
                    selected_point.move(movement=event.rel)
                    self.refresh()

                if event.type == pg.MOUSEBUTTONUP and selected_point:
                    selected_point = None

                # pokud je stisknuto "R" volej funkci reset
                if event.type == pg.KEYDOWN and event.key == pg.K_r:
                    self.reset()

            # updatuj obrazovku
            pg.display.flip()
            # nastav počet snímků za sekundu
            self.clock.tick(self.config.user_settings.framerate)
