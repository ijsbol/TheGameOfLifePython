from typing import Final, List, Union
from . import (
    Cell,
    BOARD_TOP_CHAR,
    BOARD_BOTTOM_CHAR,
    BOARD_LEFT_SIDE_CHAR,
    BOARD_RIGHT_SIDE_CHAR,
)

class Board:
    def __init__(self, width: int, height: int, debug: bool = False) -> None:
        """
            Initialises a Board object.
        """

        self.width: Final[int] = width
        self.height: Final[int] = height
        self._board: List[List[Cell]] = self._generate_empty_board()
        self.__debug = debug


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

                formatted_board += str(cell)

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
        return self._board[y][x]


    def _count_alive_cells_in_neighbour_row(self, neighbours: List[Union[None, Cell]]) -> int:
        """
            Count the number of alive cells surrounding a cell.

            Returns
            -------
            `int` of the number of alive cells.
        """
        
        number_of_alive_cells = 0
        for neighbour in neighbours:
            if (
                neighbour is not None
                and neighbour.alive
            ):
                # The cell is within the bounds of the board and is alive.
                number_of_alive_cells += 1
        
        neighbours = [str(neighbour) for neighbour in neighbours]
        if self.__debug:
            print(f"{number_of_alive_cells=} | {neighbours=}")
        return number_of_alive_cells


    def permutate(self) -> None:
        """
            Permutate to the next itteration of the board.
        """
        
        temp_board: List[List[Cell]] = self._generate_empty_board()
        for x, row_of_cells in enumerate(self._board):
            
            for y, cell in enumerate(row_of_cells):
                cell_neighbours = cell.get_neighbour_cells()
                alive_neighbours = self._count_alive_cells_in_neighbour_row(cell_neighbours)
                if cell.alive:
                    # Do logic for a currently alive cell.
                    if alive_neighbours < 2:
                        # A live cell dies if it has fewer than two live neighbors.
                        temp_board[x][y] = Cell(x, y, self, alive=False)

                    elif alive_neighbours == 2 or alive_neighbours == 3:
                        # A live cell with two or three live neighbors lives on to the next generation.
                        temp_board[x][y] = Cell(x, y, self, alive=True)

                    elif alive_neighbours > 3:
                        # A live cell with more than three live neighbors dies.
                        temp_board[x][y] = Cell(x, y, self, alive=False)

                else:
                    # Do logic for a currently dead cell.
                    if alive_neighbours == 3:
                        # A dead cell will be brought back to live if it has exactly three live neighbors.
                        temp_board[x][y] = Cell(x, y, self, alive=True)
        
        # Update the game board to have the new board state.
        self._board = temp_board


    def generation(self) -> None:
        print(self)
        self.permutate()