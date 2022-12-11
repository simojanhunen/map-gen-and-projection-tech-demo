import pygame as pg
import math

from settings import *


class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.initialized = False
        self.starting_tile = None
        self.x, self.y = (0, 0)
        self.angle = 0

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

    def check_if_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_collisions(self, dx, dy):
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
        dy = -((MAP_ROWS // 2) - self.y)
        dx = (MAP_COLS // 2) - self.x
        self.angle = -math.atan2(dy, dx)

        self.initialized = True

    def update(self) -> None:
        if not self.initialized:
            self.initialize()
        self.move()

    def draw(self) -> None:
        if self.initialized:
            scaled_x = self.x * BLOCK_SCALE + BLOCK_SCALE // 2
            scaled_y = self.y * BLOCK_SCALE + BLOCK_SCALE // 2
            end_x = BLOCK_SCALE // 2 * math.cos(self.angle)
            end_y = BLOCK_SCALE // 2 * math.sin(self.angle)

            self.map_exit = pg.draw.circle(
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
