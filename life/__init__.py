from typing import Final

CELL_ALIVE_CHAR: Final[str] = "o"
CELL_DEAD_CHAR: Final[str] = "x"

BOARD_TOP_CHAR: Final[str] = "-"
BOARD_BOTTOM_CHAR: Final[str] = "-"
BOARD_LEFT_SIDE_CHAR: Final[str] = "|"
BOARD_RIGHT_SIDE_CHAR: Final[str] = "|"

from .cell import Cell
from .board import Board