from typing import Final, List, Union, Optional
from time import sleep
from random import choice

from . import (
    Cell,
    BOARD_TOP_CHAR,
    BOARD_BOTTOM_CHAR,
    BOARD_LEFT_SIDE_CHAR,
    BOARD_RIGHT_SIDE_CHAR,
)


class Board:
    def __init__(
        self,
        width: int,
        height: int,
        debug: bool = False,
        display_as_numbers: bool = False,
        advanced_number_display: bool = False,
        label_axis: bool = False,  # doesn't really work that well for <10 in width or height
        wrapping: bool = False,
        random_start: bool = False,
    ) -> None:
        """
        Initialises a Board object.
        """

        self.width: Final[int] = width
        self.height: Final[int] = height

        self.__debug: Final[bool] = debug
        self.__display_as_numbers: Final[bool] = debug if debug else display_as_numbers
        self.__advanced_number_display: Final[bool] = advanced_number_display
        self.__label_axis: Final[bool] = label_axis
        self.__wrapping: Final[bool] = wrapping

        if random_start:
            self._board: List[List[Cell]] = self._generate_empty_board(random_start=True)
        else:
            self._board: List[List[Cell]] = self._generate_empty_board()

    def __str__(self) -> str:
        """
        Returns a string representation of the board.
        """

        formatted_board = ""

        # Set the top of the str board
        board_width_including_edges = self.width + 2
        if self.__label_axis:
            formatted_board += "  " + "".join([str(i) for i in range(self.width)]) + "\n"
            formatted_board += BOARD_TOP_CHAR * board_width_including_edges
        else:
            formatted_board += BOARD_TOP_CHAR * board_width_including_edges

        for y, row_of_cells in enumerate(self._board):
            # Starting a new line
            formatted_board += "\n"

            for x, cell in enumerate(row_of_cells):
                if x == 0:
                    # Start of a new row
                    if self.__label_axis:
                        formatted_board += str(y)
                    formatted_board += BOARD_LEFT_SIDE_CHAR

                if self.__display_as_numbers:
                    cell_neighbours = self._get_cell_neighbours(cell)
                    alive_neighbours = self._count_alive_cells_in_neighbour_row(cell_neighbours)
                    formatted_board += str(alive_neighbours)
                
                elif self.__advanced_number_display:
                    cell_neighbours = self._get_cell_neighbours(cell)
                    alive_neighbours = self._count_alive_cells_in_neighbour_row(cell_neighbours)
                    formatted_board += f"[{'a' if cell.alive else 'd'}{str(alive_neighbours)}]"
                
                else:
                    formatted_board += str(cell)

            # End of a row
            formatted_board += BOARD_RIGHT_SIDE_CHAR

        # Set the bottom of the str board
        formatted_board += "\n" + BOARD_BOTTOM_CHAR * (board_width_including_edges)

        return formatted_board

    def _generate_empty_board(self, random_start: bool = False) -> List[List[Cell]]:
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
                if random_start:
                    alive_state = choice([False, True])
                else:
                    alive_state = False
                new_cell = Cell(x, y, alive=alive_state)
                empty_board[y].append(new_cell)

        return empty_board

    def get_cell(self, x: int, y: int) -> Cell:
        return self._board[y][x]

    def _count_alive_cells_in_neighbour_row(self, neighbours: List[Union[None, Cell]], wrapping: bool = False) -> int:
        """
        Count the number of alive cells surrounding a cell.

        Returns
        -------
        `int` of the number of alive cells.
        """

        number_of_alive_cells = 0
        for neighbour in neighbours:
            if neighbour is not None and neighbour.alive:
                # The cell is within the bounds of the board and is alive.
                number_of_alive_cells += 1

        neighbours = [str(neighbour) for neighbour in neighbours]
        if self.__debug:
            print(f"{number_of_alive_cells=} | {neighbours=}")
        return number_of_alive_cells

    def _get_cell_neighbours(self, cell: Cell, wrapping: bool = False) -> List[List[Cell]]:
        """
        Get an iterable List[List] of all neighbouring cells.

        Returns
        -------
        A List[List[Union[None, Cell]]] of all cell neighbours.
        `None` is used when a cell would have been out of bounds & wrapping is disabled.
        """
        cell_neighbour_locations = cell.neighbour_locations
        cell_neighbours: List[Union[None, Cell]] = []

        for cell_x, cell_y in cell_neighbour_locations:
            # Check that the cell is within the bounds of the Board.
            if (
                (cell_x < self.width and cell_x >= 0)
                and (cell_y < self.height and cell_y >= 0)
            ):
                # Cell is within the boards bounds.
                cell_at_location = self.get_cell(cell_x, cell_y)
                cell_neighbours.append(cell_at_location)
            else:
                # Cell is out of the boards bounds.
                if not self.__wrapping:
                    cell_neighbours.append(None)
                else:
                    if cell_x >= self.width:
                        cell_x -= self.width
                    elif cell_x < 0:
                        cell_x += self.width
                    if cell_y >= self.height:
                        cell_y -= self.height
                    elif cell_y < 0:
                        cell_y += self.height
                    cell_at_location = self.get_cell(cell_x, cell_y)
                    cell_neighbours.append(cell_at_location)

        return cell_neighbours

    def set_cell(self, x: int, y: int, cell: Cell, _board=None) -> Optional[List[List[Cell]]]:
        if _board is None:
            self._board[y][x] = cell
        else:
            _board[y][x] = cell
            return _board

    def permutate(self) -> None:
        """
        Permutate to the next itteration of the board.
        """

        temp_board: List[List[Cell]] = self._generate_empty_board()
        for y, row_of_cells in enumerate(self._board):
            for x, cell in enumerate(row_of_cells):
                cell_neighbours = self._get_cell_neighbours(cell)
                alive_neighbours = self._count_alive_cells_in_neighbour_row(cell_neighbours)
                if cell.alive:
                    # Do logic for a currently alive cell.
                    if alive_neighbours < 2:
                        # A live cell dies if it has fewer than two live neighbors.
                        new_cell = Cell(x, y, alive=False)
                        temp_board = self.set_cell(x, y, new_cell, _board=temp_board)

                    elif alive_neighbours == 2 or alive_neighbours == 3:
                        # A live cell with two or three live neighbors lives on to the next generation.
                        new_cell = Cell(x, y, alive=True)
                        temp_board = self.set_cell(x, y, new_cell, _board=temp_board)

                    elif alive_neighbours > 3:
                        # A live cell with more than three live neighbors dies.
                        new_cell = Cell(x, y, alive=False)
                        temp_board = self.set_cell(x, y, new_cell, _board=temp_board)

                else:
                    # Do logic for a currently dead cell.
                    if alive_neighbours == 3:
                        # A dead cell will be brought back to live if it has exactly three live neighbors.
                        new_cell = Cell(x, y, alive=True)
                        temp_board = self.set_cell(x, y, new_cell, _board=temp_board)
        # Update the game board to have the new board state
        self._board = temp_board

    def generation(self) -> None:
        print(self)
        self.permutate()

    def run_generations(self, amount: int = 10, time_inbetween: float = 0.2) -> None:
        for i in range(amount):
            self.generation()
            sleep(time_inbetween)
