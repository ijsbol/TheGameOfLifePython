from typing import Final, List, Tuple, Union

from . import CELL_ALIVE_CHAR, CELL_DEAD_CHAR

class Board:
    """For type hinting purposes, this avoids a circular import problem."""

class Cell:
    def __init__(self, x: int, y: int, board: Board, alive: bool = False) -> None:
        """
            Initialises a Cell object.
        """

        self.x: Final[int] = x
        self.y: Final[int] = y
        self.alive: Final[bool] = alive
        self.board: Final[Board] = board
    

    def __str__(self) -> str:
        """
            Returns a string representation of the cell.
        """

        return CELL_ALIVE_CHAR if self.alive else CELL_DEAD_CHAR


    @property
    def _neighbour_locations(self) -> List[Tuple[int, int]]:
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


    def get_neighbour_cells(self) -> List[List]:
        """
            Get an iterable List[List] of all neighbouring cells.

            Returns
            -------
            A List[List[Union[None, Cell]]] of all cell neighbours.
            `None` is used when a cell would have been out of bounds.
        """

        cell_neighbour_locations = self._neighbour_locations
        cell_neighbours: List[Union[None, Cell]] = []

        for cell_x, cell_y in cell_neighbour_locations:
            # Check that the cell is within the bounds of the Board.
            if (
                (cell_x < self.board.width and cell_x >= 0)
                and (cell_y < self.board.height and cell_y >= 0)
            ):
                # Cell is within the boards bounds.
                cell_at_location = self.board.get_cell(cell_x, cell_y)
                cell_neighbours.append(cell_at_location)
            else:
                # Cell is out of the boards bounds.
                cell_neighbours.append(None)
        
        return cell_neighbours
