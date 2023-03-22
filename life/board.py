from typing import Final, List
from . import (
    Cell,
    BOARD_TOP_CHAR,
    BOARD_BOTTOM_CHAR,
    BOARD_LEFT_SIDE_CHAR,
    BOARD_RIGHT_SIDE_CHAR,
)

class Board:
    def __init__(self, width: int, height: int) -> None:
        """
            Initialises a Board object.
        """

        self.width: Final[int] = width
        self.height: Final[int] = height
        self._board: List[List[Cell]] = self._generate_empty_board()


    def __str__(self) -> str:
        """
            Returns a string representation of the board.
        """
        
        formatted_board = ""
        
        # Set the top of the str board
        board_width_including_edges = self.width+2
        formatted_board += BOARD_TOP_CHAR*(board_width_including_edges)

        for row_of_cells in self._board:
            # Starting a new line
            formatted_board += "\n"

            for row_index, cell in enumerate(row_of_cells):
                if row_index == 0:
                    # Start of a new row
                    formatted_board += BOARD_LEFT_SIDE_CHAR

                formatted_board += str(cell) #f"({cell.x}, {cell.y}) "

            # End of a row
            formatted_board += BOARD_RIGHT_SIDE_CHAR

        # Set the bottom of the str board
        formatted_board += "\n" + BOARD_BOTTOM_CHAR*(board_width_including_edges)

        return formatted_board


    def _generate_empty_board(self) -> List[List[Cell]]:
        """
            Generate an empty board with the provided width & height.

            Returns
            -------
            A List[List[Cell]].
        """
        
        empty_board: List[List[Cell]] = []
        
        for y in range(self.height):
            empty_board.append([])

            for x in range(self.width):
                new_cell = Cell(x, y, self)
                empty_board[y].append(new_cell)
        
        return empty_board


    def get_cell(self, x: int, y: int) -> Cell:
        return self._board[x][y]
