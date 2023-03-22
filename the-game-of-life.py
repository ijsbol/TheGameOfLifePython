import life
import time

game_board = life.Board(10, 10)


game_board.set_cell(4, 3, life.Cell(4, 3, True))
game_board.set_cell(4, 4, life.Cell(4, 4, True))
game_board.set_cell(4, 5, life.Cell(4, 5, True))

game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)
game_board.generation(); time.sleep(0.2)