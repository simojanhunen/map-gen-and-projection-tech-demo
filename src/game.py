"""
Game entry point
"""

# 3rd party and standard libraries
import pygame as pg
import sys

# Internal libraries
from settings import *


class Game:
    def __init__(self) -> None:
        pg.init()
        self.window = pg.display
        self.display = self.window.set_mode(DISPLAY_RESOLUTION)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        pass

    def game_loop(self):
        while True:
            self.event_loop()
            self.update()
            self.draw()

    def update(self):
        self.window.flip()
        self.window.set_caption(f"{GAME_TITLE} - {self.clock.get_fps() :.1f}")

    def draw(self):
        self.display.fill("magenta")

    def event_loop(self):
        for event in pg.event.get():
            # Process key presses
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()


if __name__ == "__main__":
    game = Game()
    game.game_loop()
