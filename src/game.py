"""
Game entry point
"""

import pygame as pg
import sys

from settings import *
from map import *
from player import *


class Game:
    def __init__(self) -> None:
        pg.init()
        self.window = pg.display
        self.display = self.window.set_mode(DISPLAY_RESOLUTION)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.player = Player(self)
        self.map = Map(self)

    def game_loop(self):
        while True:
            self.event_loop()
            self.update()
            self.draw()

    def update(self):
        self.window.flip()
        self.window.set_caption(f"{GAME_TITLE} - {self.clock.get_fps() :.1f}")

    def draw(self):
        self.display.fill("white")
        self.map.draw()
        self.player.draw()

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
                self.map = Map(self)


if __name__ == "__main__":
    game = Game()
    game.game_loop()
