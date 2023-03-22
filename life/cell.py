from typing import Final, List, Tuple, Union

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
    
    @property
    def _neighbour_locations(self) -> List[List[Tuple[int, int]]]:
        """
            Get neighbouring cells.

            Returns
            -------
            A List[List[Tuple[int, int]]] of the surrounding cell x & y coordinates.
            Will return impossible cell locations, will require further data validation.
        """
        x = self.x
        y = self.y
        return [
            [(x-1, y+1), (x  , y+1), (x+1, y+1)],
            [(x-1, y  ),             (x+1, y  )],
            [(x-1, y-1), (x  , y-1), (x+1, y-1)],
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
        cell_neighbours: List[List[Union[None, Cell]]] = []

        for row_index, cell_row in enumerate(cell_neighbour_locations):
            for cell_x, cell_y in cell_row:
                # Check that the cell is within the bounds of the Board.
                if (
                    (cell_x <= self.board.width and cell_x > 0)
                    and (cell_y <= self.board.height and cell_y > 0)
                ):
                    # Cell is within the boards bounds.
                    cell_at_location = self.board.get_cell(cell_x, cell_y)
                    cell_neighbours[row_index].append(cell_at_location)
                else:
                    # Cell is out of the boards bounds.
                    cell_neighbours[row_index].append(None)
        
        return cell_neighbours
