import pygame as pg
from random import randint

from settings import *
from map_generator import generate_32x24_map


class Map:
    def __init__(self, game=None) -> None:
        self.game = game
        self.map_layout = None
        self.world_map = {}

        self.randomize()
        self.populate_world_map()

    def populate_world_map(self):
        for j, row in enumerate(self.map_layout):
            # For value in jth row and ith column add value to position (i, j) if it is not False
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        if self.game:
            for pos in self.world_map:
                left_pos, top_pos = pos
                left, top, width, height = (
                    left_pos * BLOCK_SCALE,
                    top_pos * BLOCK_SCALE,
                    BLOCK_SCALE,
                    BLOCK_SCALE,
                )
                pg.draw.rect(
                    surface=self.game.display,
                    color="black",
                    rect=(left, top, width, height),
                    width=0,
                )

    def randomize(self):
        map_layout_s = generate_32x24_map()

        # Convert string format to numbers
        map_layout_s = (
            map_layout_s.replace(" ", "#")
            .replace("<", ".")
            .replace(">", ".")
            .replace(".", "0")
            .replace("#", str(randint(1, 1)))
        )

        # Create map layout from string
        map_layout = [[] * MAP_COLS] * MAP_ROWS
        for i, row in enumerate(map_layout_s.split("\n")[:-1]):
            map_layout[i] = [*row]

        # Convert string integers to integers
        self.map_layout = [[int(i) for i in row] for row in map_layout]


if __name__ == "__main__":
    map = Map()
