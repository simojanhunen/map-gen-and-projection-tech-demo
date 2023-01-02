import pygame as pg
import math
from settings import *


class RayCasting:
    def __init__(self, game) -> None:
        self.game = game
        self.raycasting_result = []

    def raycast(self) -> None:
        self.raycasting_result = []
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUMBER_OF_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # Verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # Remove fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)

            # Get projection height based on depth
            projection_height = SCREEN_DISTANCE / (depth + 0.0001)

            # Save raycasting result
            self.raycasting_result.append((ray, depth, projection_height))

            ray_angle += DELTA_ANGLE

    def update(self) -> None:
        self.raycast()

    def draw(self) -> None:

        # Draw floor (half of the vertical space is occupied by solid color)
        pg.draw.rect(
            self.game.display,
            FLOOR_COLOR,
            (0, (DISPLAY_HEIGHT // 2), DISPLAY_WIDTH, DISPLAY_HEIGHT),
        )

        for ray, depth, projection_height in self.raycasting_result:

            # Draw walls
            color = [255 / (3 + depth**5 * 0.00002)] * 4
            pg.draw.rect(
                self.game.display,
                color,
                (
                    ray * RAY_TO_DISPLAY_SCALE,
                    (DISPLAY_HEIGHT // 2) - projection_height // 2,
                    RAY_TO_DISPLAY_SCALE,
                    projection_height,
                ),
            )
