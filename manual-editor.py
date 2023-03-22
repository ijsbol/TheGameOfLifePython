from life import Board, Cell

game_board = Board(20, 10)

# Cube (stable)
game_board.set_cell(18, 8, Cell(18, 8, True))
game_board.set_cell(18, 9, Cell(18, 9, True))
game_board.set_cell(19, 8, Cell(19, 8, True))
game_board.set_cell(19, 9, Cell(19, 9, True))

# Pole (alters state every generation)
game_board.set_cell(18, 0, Cell(18, 0, True))
game_board.set_cell(18, 1, Cell(18, 1, True))
game_board.set_cell(18, 2, Cell(18, 2, True))

# Glider (moves across the board)
game_board.set_cell(0, 2, Cell(0, 2, True))
game_board.set_cell(1, 2, Cell(1, 2, True))
game_board.set_cell(2, 2, Cell(2, 2, True))
game_board.set_cell(2, 1, Cell(2, 1, True))
game_board.set_cell(1, 0, Cell(1, 0, True))

# Run
game_board.run_generations(29)
