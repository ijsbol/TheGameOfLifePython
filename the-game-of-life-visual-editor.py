from life import Board, Cell
from typing import Final, List

ALIVE_CELL_VISUAL_REPRESENTATION: Final[str] = "⬜"
DEAD_CELL_VISUAL_REPRESENTATION: Final[str] = "⬛"

# Edit this varaible.
# Make sure that the width is consistent.
STARTING_GENERATION: Final[str] = """
⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛
⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜
"""


def run_game_of_life(starting_generation: str) -> None:
    starting_generation_is_valid: bool = validate_starting_generation(STARTING_GENERATION)
    if not starting_generation_is_valid:
        # Starting generation has invalid formatting.
        return

    starting_generation_rows = starting_generation.split("\n")
    starting_generation_rows = starting_generation_rows[1:-1] # Remove the empty first and last rows
    board_width = len(starting_generation_rows[0])
    board_height = len(starting_generation_rows)

    game_board = initialize_game_board(starting_generation_rows, board_width, board_height)

    game_board.run_generations(29)

def validate_starting_generation(starting_generation: str) -> bool:
    """
    Checks that the starting generation is valid and can be parsed.
    
    Returns
    -------
    `bool` on if the starting generation is valid.
    """

    starting_generation_rows = starting_generation.split("\n")
    starting_generation_rows = starting_generation_rows[1:-1] # Remove the empty first row
    length_of_first_row = len(starting_generation_rows[0])

    for row_index, row in enumerate(starting_generation_rows):
        length_of_row = len(row)
        if length_of_row != length_of_first_row:
            # Formatting error : Inconsistent row length.
            print(f"Formatting Erorr: Inconsistent row length at row {row_index}. Length was {length_of_row} when should be {length_of_first_row}.")
            return False

        for cell in row:
            if cell not in [ALIVE_CELL_VISUAL_REPRESENTATION, DEAD_CELL_VISUAL_REPRESENTATION]:
                # Formatting error : Unknown cell type.
                print(f"Formatting Error: Unknown cell type `{cell}` in row {row_index}. Expected {ALIVE_CELL_VISUAL_REPRESENTATION} or {DEAD_CELL_VISUAL_REPRESENTATION}.")
                return False

    return True

def initialize_game_board(starting_generation_rows: List[str], board_width: int, board_height: int) -> Board:
    game_board = Board(board_width, board_height)
    
    for y, cell_row in enumerate(starting_generation_rows):
        for x, cell in enumerate(cell_row):
            cell_is_alive = True if cell == ALIVE_CELL_VISUAL_REPRESENTATION else False
            new_cell = Cell(x, y, cell_is_alive)
            game_board.set_cell(x, y, new_cell)
    
    return game_board

    return game_board

if __name__ == "__main__":
    run_game_of_life(STARTING_GENERATION)
