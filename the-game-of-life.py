import life

game_board = life.Board(10, 10)

game_board._board[3][4] = life.Cell(4, 3, game_board, True)
game_board._board[4][4] = life.Cell(4, 4, game_board, True)
game_board._board[5][4] = life.Cell(4, 5, game_board, True)

game_board.generation()
game_board.generation()
game_board.generation()
game_board.generation()
game_board.generation()
game_board.generation()
game_board.generation()
game_board.generation()
game_board.generation()
game_board.generation()