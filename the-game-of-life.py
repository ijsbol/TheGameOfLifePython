import life

game_board = life.Board(25, 10)
print(game_board)

cell_at_0_0 = game_board._get_cell(0, 0)
print(cell_at_0_0)
print(cell_at_0_0.alive)