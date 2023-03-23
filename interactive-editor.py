import time
from typing import Final, Tuple, Any

from life import Board, Cell
import pygame

# Board wrapping allows for infinite travel.
BOARD_WRAPPING: Final[bool] = True

DEAD_COLOUR: Final[str] = "BLACK"
ALIVE_COLOUR: Final[str] = "WHITE"
BLACKGROUND_COLOUR: Final[str] = "WHITE"
BLOCK_SIZE: Final[int] = 20
FRAME_RATE: Final[float] = 0.1

ALLOW_ITTERATIONS: bool = False

WINDOW_CELL_WIDTH: Final[int] = 50
WINDOW_CELL_HEIGHT: Final[int] = 50

WINDOW_HEIGHT: Final[int] = BLOCK_SIZE * WINDOW_CELL_WIDTH
WINDOW_WIDTH: Final[int] = BLOCK_SIZE * WINDOW_CELL_HEIGHT
GAME_BOARD = Board(WINDOW_CELL_WIDTH, WINDOW_CELL_HEIGHT, wrapping=BOARD_WRAPPING)

def draw_grid() -> None:
    """
    Draw the game board to the screen in a grid formation.
    """

    for cell_pos_x, window_pos_x in enumerate(range(0, WINDOW_WIDTH, BLOCK_SIZE)):

        for cell_pos_y, window_pos_y in enumerate(range(0, WINDOW_HEIGHT, BLOCK_SIZE)):

            rect = pygame.Rect(window_pos_x, window_pos_y, BLOCK_SIZE-1, BLOCK_SIZE-1)

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
    SCREEN.fill(BLACKGROUND_COLOUR)

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