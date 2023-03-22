import life
import time

game_board = life.Board(20, 10)

# Cube (stable)
game_board.set_cell(18, 8, life.Cell(18, 8, True))
game_board.set_cell(18, 9, life.Cell(18, 9, True))
game_board.set_cell(19, 8, life.Cell(19, 8, True))
game_board.set_cell(19, 9, life.Cell(19, 9, True))

# Pole (alters state every generation)
game_board.set_cell(18, 0, life.Cell(18, 0, True))
game_board.set_cell(18, 1, life.Cell(18, 1, True))
game_board.set_cell(18, 2, life.Cell(18, 2, True))

# Glider (moves across the board)
game_board.set_cell(0, 2, life.Cell(0, 2, True))
game_board.set_cell(1, 2, life.Cell(1, 2, True))
game_board.set_cell(2, 2, life.Cell(2, 2, True))
game_board.set_cell(2, 1, life.Cell(2, 1, True))
game_board.set_cell(1, 0, life.Cell(1, 0, True))


game_board.run_generations(29)