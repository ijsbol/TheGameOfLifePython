import life

game_board = life.Board(50, 50)
print(game_board.board)

cell_at_0_0 = game_board.get_cell(0, 0)
print(cell_at_0_0)
print(cell_at_0_0.alive)