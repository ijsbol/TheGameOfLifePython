from typing import Final

FANCY_MODE: Final[bool] = True

if FANCY_MODE:
    CELL_ALIVE_CHAR: Final[str] = "⬜"
    CELL_DEAD_CHAR: Final[str] = "⬛"

    BOARD_TOP_CHAR: Final[str] = ""
    BOARD_BOTTOM_CHAR: Final[str] = ""
    BOARD_LEFT_SIDE_CHAR: Final[str] = ""
    BOARD_RIGHT_SIDE_CHAR: Final[str] = ""
else:
    CELL_ALIVE_CHAR: Final[str] = "o"
    CELL_DEAD_CHAR: Final[str] = " "

    BOARD_TOP_CHAR: Final[str] = "_"
    BOARD_BOTTOM_CHAR: Final[str] = "‾"
    BOARD_LEFT_SIDE_CHAR: Final[str] = "|"
    BOARD_RIGHT_SIDE_CHAR: Final[str] = "|"

from .cell import Cell
from .board import Board