from typing import Final, Tuple

from .board import Board
from .cell import Cell

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

__all__: Final[Tuple[str, ...]] = (
    "Board",
    "Cell",
    "CELL_ALIVE_CHAR",
    "CELL_DEAD_CHAR",
    "BOARD_TOP_CHAR",
    "BOARD_BOTTOM_CHAR",
    "BOARD_LEFT_SIDE_CHAR",
    "BOARD_RIGHT_SIDE_CHAR",
)
