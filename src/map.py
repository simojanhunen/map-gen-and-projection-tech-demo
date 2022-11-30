import pygame as pg
from random import randint

from settings import *
from map_generator import generate_32x24_map


class Tileset:
    def __init__(self, file, size=(32, 32), margin=0, spacing=0) -> None:
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pg.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()

    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pg.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)

    def __str__(self):
        return f"{self.__class__.__name__} file:{self.file} tile:{self.size}"

    def get_tile(self, index):
        return self.tiles[index]


class Map:
    def __init__(self, game=None) -> None:
        self.game = game
        self.map_layout = None
        self.world_map = {}
        self.floor_map = {}
        self.tileset = Tileset("src/resources/tilemaps/dungeon.png")
        self.randomize()
        self.populate_maps()

    def populate_maps(self):
        for j, row in enumerate(self.map_layout):
            # For value in jth row and ith column add value to position (i, j) if wall else floor
            for i, value in enumerate(row):
                if value == " ":
                    pass
                elif value:
                    self.world_map[(i, j)] = value
                else:
                    self.floor_map[(i, j)] = value

    def draw(self):
        if self.game:
            for x, y in self.floor_map:
                self.game.display.blit(
                    self.tileset.get_tile(self.floor_map[x, y]),
                    (x * BLOCK_SCALE, y * BLOCK_SCALE),
                )

            for x, y in self.world_map:
                self.game.display.blit(
                    self.tileset.get_tile(self.world_map[x, y]),
                    (x * BLOCK_SCALE, y * BLOCK_SCALE),
                )

    def randomize(self):
        map_layout_s = generate_32x24_map()

        # Convert string format to numbers
        map_layout_s = (
            map_layout_s.replace("<", ".")
            .replace(">", ".")
            .replace(".", "0")
            .replace("#", str(randint(1, 1)))
        )

        # Create map layout from string
        map_layout = [[] * MAP_COLS] * MAP_ROWS
        for i, row in enumerate(map_layout_s.split("\n")[:-1]):
            map_layout[i] = [*row]

        self.map_layout = [
            [int(i) if i != " " else i for i in row] for row in map_layout
        ]


if __name__ == "__main__":
    map = Map()
