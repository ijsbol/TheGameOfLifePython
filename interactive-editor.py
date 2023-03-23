import time
from typing import Final, Tuple, Any

from life import Board, Cell
import pygame

# You can edit these to configure the game.
BOARD_WRAPPING: Final[bool] = True # Enable board wrapping
DEAD_COLOUR: Final[str] = "BLACK" # Dead cell colour
ALIVE_COLOUR: Final[str] = "WHITE" # Alive cell colour
CELL_OUTLINE_COLOUR: Final[str] = "WHITE" # Cell outline colour
BLOCK_SIZE: Final[int] = 10 # Size of the cells (in pixels)
FRAME_RATE: Final[float] = 0.1 # Maximum frame rate (time between frames)
OUTLINE_CELLS: Final[bool] = False # Should the cells be outlined?
OUTLINE_OFFSET_VALUE: Final[int] = 1 # If cells are outlined, how big of an outline should there be? (in pixels)
WINDOW_CELL_WIDTH: Final[int] = 50 # How many cells wide should the window be
WINDOW_CELL_HEIGHT: Final[int] = 50 # How many cells tall should the window be

# Do not edit these unless you want to break stuff.
ALLOW_ITTERATIONS: bool = False
WINDOW_HEIGHT: Final[int] = BLOCK_SIZE * WINDOW_CELL_WIDTH
WINDOW_WIDTH: Final[int] = BLOCK_SIZE * WINDOW_CELL_HEIGHT
OUTLINE_OFFSET: Final[int] = OUTLINE_OFFSET_VALUE if OUTLINE_CELLS else 0

# If you wish to parse kwargs listed in the README.md file, then do that here after wrapping=BOARD_WRAPPING.
GAME_BOARD = Board(WINDOW_CELL_WIDTH, WINDOW_CELL_HEIGHT, wrapping=BOARD_WRAPPING)


def draw_grid() -> None:
    """
    Draw the game board to the screen in a grid formation.
    """

    for cell_pos_x, window_pos_x in enumerate(range(0, WINDOW_WIDTH, BLOCK_SIZE)):

        for cell_pos_y, window_pos_y in enumerate(range(0, WINDOW_HEIGHT, BLOCK_SIZE)):

            rect = pygame.Rect(window_pos_x, window_pos_y, BLOCK_SIZE-OUTLINE_OFFSET, BLOCK_SIZE-OUTLINE_OFFSET)

            cell = GAME_BOARD.get_cell(cell_pos_x, cell_pos_y)
            cell_colour = ALIVE_COLOUR if cell.alive else DEAD_COLOUR

            pygame.draw.rect(SCREEN, cell_colour, rect)

def figure_out_which_cell(mouse_click_location: Tuple[int]) -> Cell:
    # There is probably a better way of doing this, however; I am very tired.

    window_pos_x, window_pos_y = mouse_click_location

    cell_pos_x = window_pos_x // BLOCK_SIZE
    cell_pos_y = window_pos_y // BLOCK_SIZE

    cell = GAME_BOARD.get_cell(cell_pos_x, cell_pos_y)

    return cell

def flip_cell_state(cell: Cell) -> None:
    cell.alive = not cell.alive
    GAME_BOARD.set_cell(cell.x, cell.y, cell)

def carry_out_user_interaction(first_clicked_state_has_been_set: bool, mouse_first_clicked_cell_alive_state: bool) -> Tuple[bool]:
    mouse_pos = pygame.mouse.get_pos()
    clicked_cell = figure_out_which_cell(mouse_pos)

    if not first_clicked_state_has_been_set:
        mouse_first_clicked_cell_alive_state = clicked_cell.alive
        first_clicked_state_has_been_set = True

    if clicked_cell.alive == mouse_first_clicked_cell_alive_state:
        flip_cell_state(clicked_cell)
    
    return first_clicked_state_has_been_set, mouse_first_clicked_cell_alive_state

if __name__ == "__main__":
    pygame.init()
    time_delta = 0

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(CELL_OUTLINE_COLOUR)

    mouse_first_clicked_cell_alive_state = False
    first_clicked_state_has_been_set = False
    mouse_is_currently_clicked = False

    while True:
        # The game loop

        draw_grid()
        
        events_this_frame = pygame.event.get()
        for event in events_this_frame:
            if event.type == pygame.QUIT:
                # Check if the player has closed the game.
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_currently_clicked = True
                first_clicked_state_has_been_set, mouse_first_clicked_cell_alive_state = (
                    carry_out_user_interaction(
                        first_clicked_state_has_been_set,
                        mouse_first_clicked_cell_alive_state
                    )
                )
                
            elif event.type == pygame.MOUSEBUTTONUP:
                first_clicked_state_has_been_set = False
                mouse_is_currently_clicked = False
            
            elif event.type == pygame.MOUSEMOTION and mouse_is_currently_clicked:
                first_clicked_state_has_been_set, mouse_first_clicked_cell_alive_state = (
                    carry_out_user_interaction(
                        first_clicked_state_has_been_set,
                        mouse_first_clicked_cell_alive_state
                    )
                )

                    
        keys_pressed_this_frame = pygame.key.get_pressed()
        if keys_pressed_this_frame[pygame.K_SPACE]:
            # If space key is pressed, resume the simulation.
            ALLOW_ITTERATIONS = True
        elif keys_pressed_this_frame[pygame.K_TAB]:
            # If tab key is pressed, pause the simulation.
            ALLOW_ITTERATIONS = False

        # Update the display
        pygame.display.update()

        time_delta += CLOCK.tick(60) / 1000
        if (
            time_delta >= FRAME_RATE
            and ALLOW_ITTERATIONS
        ):
            GAME_BOARD.permutate()