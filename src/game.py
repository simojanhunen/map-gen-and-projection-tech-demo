"""
Game entry point
"""

import pygame as pg
import sys

from typing import Type

from settings import *
from map import *
from player import *
from raycasting import *


class Game:
    def __init__(self) -> None:
        pg.init()
        self.window = pg.display
        self.display = self.window.set_mode(DISPLAY_RESOLUTION)
        self.clock = pg.time.Clock()
        self.dt: int = 1  # deltatime
        self.two_dimentional: bool = True
        self.new_game()

    def new_game(self):
        self.player = Player(self)
        self.raycasting = RayCasting(self)
        self.map = Map(self)

        self.initialize()

    def game_loop(self):
        while True:
            self.event_loop()
            self.update()
            self.draw()

    def initialize(self):
        self.player.initialize()

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.window.flip()
        self.dt = self.clock.tick(FRAMES_PER_SECOND)
        self.window.set_caption(f"{GAME_TITLE} - {self.clock.get_fps() :.1f}")

    def draw(self):
        self.display.fill("white")

        if self.two_dimentional:
            self.map.draw()
            self.player.draw()
        else:
            self.raycasting.draw()

    def event_loop(self):
        # Process key presses
        for event in pg.event.get():

            # Q or ESC quits game
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()

            # SPACE generates new layout
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.new_game()

            # ENTER changes perspective from 2D to 2.5D and vice versa
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                self.two_dimentional = not self.two_dimentional


if __name__ == "__main__":
    game = Game()
    game.game_loop()
