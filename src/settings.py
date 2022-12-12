"""
Stores all the game settings in one common location
"""

from typing import Final

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
TILESET_DUNGEON = "./resources/tilemaps/dungeon.png"

# Player
PLAYER_SPEED = 0.004
PLAYER_ROTATION_SPEED = 0.004
PLAYER_SIZE_SCALE = 16
