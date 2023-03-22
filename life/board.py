from . import Cell
from typing import Final, List

class Board:
    def __init__(self, width: int, height: int) -> None:
        """
            Initialises a Board object.
        """

        self.width: Final[int] = width
        self.height: Final[int] = height
        self.board: List[List[Cell]] = []


    def _generate_empty_board(self) -> List[List[Cell]]:
        """
            Generate an empty board with the provided width & height.

            Returns
            -------
            A List[List[Cell]].
        """
        
        empty_board: List[List[Cell]] = []
        
        for x in range(self.width):
            empty_board[x] = []
            
            for y in range(self.height):
                new_cell = Cell(x, y)
                empty_board[x].append(new_cell)
        
        return empty_board


    def get_cell(self, x: int, y: int) -> Cell:
        return self.board[x][y]
