"""
Stores all the game settings in one common location
"""

from typing import Final, Tuple
import math

# Window and game display
GAME_TITLE: Final = "Unnamed raycaster 2D"
FRAMES_PER_SECOND: Final = 60

DISPLAY_WIDTH: Final = 1024
DISPLAY_HEIGHT: Final = 768
DISPLAY_RESOLUTION: Final = DISPLAY_WIDTH, DISPLAY_HEIGHT

BLOCK_SCALE: Final = 32  # 32x32px
BLOCK_SCALE_HALVED: Final = BLOCK_SCALE // 2
BLOCK_SCALE_WITH_OFFSET: Final = BLOCK_SCALE + BLOCK_SCALE_HALVED

MAP_COLUMNS: Final = 32
MAP_ROWS: Final = 24
MAP_SIZE: Final = MAP_COLUMNS, MAP_ROWS

MAP_CENTER_COLUMN: Final = MAP_COLUMNS // 2
MAP_CENTER_ROW: Final = MAP_ROWS // 2
MAP_CENTER: Final = MAP_CENTER_COLUMN, MAP_CENTER_ROW

# Tilesets
TILESET_DUNGEON: str = "./resources/tilemaps/dungeon.png"

# Player
PLAYER_SPEED: float = 0.004
PLAYER_ROTATION_SPEED: float = 0.004
PLAYER_SIZE_SCALE: int = 16

# Raycasting
FOV: Final = math.pi / 3
HALF_FOV: Final = FOV / 2
NUMBER_OF_RAYS: Final = DISPLAY_WIDTH // 2
DELTA_ANGLE: Final = FOV / NUMBER_OF_RAYS
MAX_DEPTH: Final = 20
SCREEN_DISTANCE: Final = (DISPLAY_WIDTH // 2) / math.tan(HALF_FOV)
RAY_TO_DISPLAY_SCALE: Final = DISPLAY_WIDTH // NUMBER_OF_RAYS

# Skybox
FLOOR_COLOR: Tuple[int, int, int] = (20, 20, 20)
