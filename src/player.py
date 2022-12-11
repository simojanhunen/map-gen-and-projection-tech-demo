import pygame as pg
from typing import Callable

from settings import *


class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.starting_tile = None
        pass

    def move(self) -> None:
        pass

    def update(self) -> None:
        self.move()

    def draw(self) -> None:
        if self.starting_tile:
            starting_tile_x, starting_tile_y = self.starting_tile
            self.map_exit = pg.draw.circle(
                self.game.display,
                "green",
                (
                    starting_tile_x * BLOCK_SCALE + BLOCK_SCALE // 2,
                    starting_tile_y * BLOCK_SCALE + BLOCK_SCALE // 2,
                ),
                16,
            )
        pass
