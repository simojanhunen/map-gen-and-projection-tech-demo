"""
Player control, events and drawing
"""

import pygame as pg
import math

from typing import Tuple

from settings import *


class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.initialized: bool = False
        self.starting_tile: Tuple[int, int] = None
        self.x: int = 0
        self.y: int = 0
        self.angle: float = 0
        self.player_rect: pg.Rect = None

    def move(self) -> None:
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.dt
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy -= speed_cos
        if keys[pg.K_d]:
            dx -= speed_sin
            dy += speed_cos

        self.check_collisions(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROTATION_SPEED * self.game.dt
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROTATION_SPEED * self.game.dt

    def check_if_wall(self, x: int, y: int) -> bool:
        return (x, y) not in self.game.map.world_map

    def check_collisions(self, dx: float, dy: float) -> None:
        scale = PLAYER_SIZE_SCALE / self.game.dt
        if self.check_if_wall(round(self.x + dx * scale), round(self.y)):
            self.x += dx
        if self.check_if_wall(round(self.x), round(self.y + dy * scale)):
            self.y += dy

        # print(
        #     f"Player is colliding with floor: {self.check_if_wall(int(self.x), int(self.y))}"
        # )

    def initialize(self) -> None:
        # Position
        self.x, self.y = self.starting_tile

        # FOV angle
        dy = -(MAP_CENTER_ROW - self.y)
        dx = MAP_CENTER_COLUMN - self.x
        self.angle = -math.atan2(dy, dx)

        self.initialized = True

    def update(self) -> None:
        if not self.initialized:
            self.initialize()
        self.move()
        self.check_if_exit()

    def check_if_exit(self) -> None:
        if self.player_rect and self.game.map.map_exit:
            if self.player_rect.colliderect(self.game.map.map_exit):
                self.game.new_game()

    def draw(self) -> None:
        if self.initialized:
            scaled_x = self.x * BLOCK_SCALE + BLOCK_SCALE_HALVED
            scaled_y = self.y * BLOCK_SCALE + BLOCK_SCALE_HALVED
            end_x = BLOCK_SCALE_HALVED * math.cos(self.angle)
            end_y = BLOCK_SCALE_HALVED * math.sin(self.angle)

            self.player_rect = pg.draw.circle(
                self.game.display,
                "green",
                (
                    scaled_x,
                    scaled_y,
                ),
                8,
            )

            pg.draw.line(
                self.game.display,
                "magenta",
                (
                    scaled_x,
                    scaled_y,
                ),
                (
                    scaled_x + end_x,
                    scaled_y + end_y,
                ),
                2,
            )
