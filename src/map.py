"""
Map generation and tileset related functionality
"""

import pygame as pg
from random import randint
from typing import Tuple, Iterable

from settings import *
from map_generator import generate_map


class Tileset:
    def __init__(
        self,
        file: str,
        size: Tuple[int, int] = (32, 32),
        margin: int = 0,
        spacing: int = 0,
    ) -> None:
        self.file: str = file
        self.size: Tuple[int, int] = size
        self.margin: int = margin
        self.spacing: int = spacing
        self.image: pg.Surface = pg.image.load(file)
        self.rect: pg.Rect = self.image.get_rect()
        self.tiles: list[pg.Surface] = []
        self.load()

    def load(self) -> None:
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

    def __str__(self) -> str:
        return f"{self.__class__.__name__} file:{self.file} tile:{self.size}"

    def get_tile(self, index) -> pg.Surface:
        return self.tiles[index]


class Map:
    def __init__(self, game) -> None:
        self.game = game
        self.map_layout: Iterable = None
        self.world_map: dict = {}
        self.floor_map: dict = {}
        self.map_exit_tile: Tuple[int, int] = None
        self.map_exit: pg.Rect = None
        self.tileset: Tileset = Tileset("src/resources/tilemaps/dungeon.png")
        self.randomize()
        self.populate_maps()

    def populate_maps(self) -> None:
        for j, row in enumerate(self.map_layout):
            # For value in jth row and ith column add value to position (i, j) if wall else floor
            for i, value in enumerate(row):
                if value == " ":
                    pass
                elif value:
                    self.world_map[(i, j)] = value
                else:
                    self.floor_map[(i, j)] = value

    def draw(self) -> None:
        if self.game:
            for x, y in self.floor_map:
                self.game.display.blit(
                    self.tileset.get_tile(self.floor_map[x, y]),
                    (x * BLOCK_SCALE, y * BLOCK_SCALE, BLOCK_SCALE, BLOCK_SCALE),
                )

            for x, y in self.world_map:
                self.game.display.blit(
                    self.tileset.get_tile(self.world_map[x, y]),
                    (x * BLOCK_SCALE, y * BLOCK_SCALE, BLOCK_SCALE, BLOCK_SCALE),
                )

            # Draw exit tile
            map_exit_tile_x, map_exit_tile_y = self.map_exit_tile
            self.map_exit = pg.draw.circle(
                self.game.display,
                "white",
                (
                    map_exit_tile_x * BLOCK_SCALE + BLOCK_SCALE_HALVED,
                    map_exit_tile_y * BLOCK_SCALE + BLOCK_SCALE_HALVED,
                ),
                16,
            )

    def randomize(self) -> None:
        map_layout_s = generate_map(MAP_COLUMNS, MAP_ROWS)

        # Convert string format to numbers
        map_layout_s = map_layout_s.replace(".", "0").replace("#", str(randint(1, 1)))

        # Create map layout from string
        map_layout = [[] * MAP_COLUMNS] * MAP_ROWS
        for i, row in enumerate(map_layout_s.split("\n")[:-1]):
            map_layout[i] = [*row]

        # Get map exit and player start location
        self.game.player.starting_tile = find_first_tile(">", map_layout)
        self.map_exit_tile = find_first_tile("<", map_layout)

        pairs = {"<": "0", ">": "0", ".": "0"}
        pair_replacer = pairs.get
        map_layout = [[pair_replacer(n, n) for n in row] for row in map_layout]

        self.map_layout = [
            [int(i) if i != " " else i for i in row] for row in map_layout
        ]


def find_first_tile(tile, list_of_lists) -> Tuple[int, int]:
    for i, values in enumerate(list_of_lists):
        try:
            j = values.index(tile)
        except ValueError:
            continue
        return j, i
