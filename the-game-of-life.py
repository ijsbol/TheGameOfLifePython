import life

game_board = life.Board(25, 10)

game_board._board[5][5] = life.Cell(5, 5, game_board, True)
game_board._board[6][5] = life.Cell(5, 6, game_board, True)
game_board._board[7][5] = life.Cell(5, 7, game_board, True)

print(game_board)

game_board.permutate()

print(game_board)

game_board.permutate()

print(game_board)
