from typing import Final, List, Tuple

from . import CELL_ALIVE_CHAR, CELL_DEAD_CHAR

class Cell:
    def __init__(self, x: int, y: int, alive: bool = False) -> None:
        """
        Initialises a Cell object.
        """

        self.x: Final[int] = x
        self.y: Final[int] = y
        self.alive: Final[bool] = alive

    def __str__(self) -> str:
        """
        Returns a string representation of the cell.
        """

        return CELL_ALIVE_CHAR if self.alive else CELL_DEAD_CHAR

    @property
    def neighbour_locations(self) -> List[Tuple[int, int]]:
        """
        Get neighbouring cells.

        Returns
        -------
        A List[Tuple[int, int]] of the surrounding cell x & y coordinates.
        Will return impossible cell locations, will require further data validation.
        """

        x = self.x
        y = self.y
        
        return [
            (x-1, y+1), (x  , y+1), (x+1, y+1),
            (x-1, y  ),             (x+1, y  ),
            (x-1, y-1), (x  , y-1), (x+1, y-1),
        ]
