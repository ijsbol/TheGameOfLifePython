from typing import Final, List, Tuple

class Cell:
    def __init__(self, x: int, y: int, alive: bool = False) -> None:
        self.x: Final[int] = x
        self.y: Final[int] = y
        self.alive: Final[bool] = alive
    
    def get_neighbour_locations(self) -> List[Tuple[int, int]]:
        x = self.x
        y = self.y
        return [
            (x-1, y+1), (x  , y+1), (x+1, y+1),
            (x-1, y  ),             (x+1, y  ),
            (x-1, y-1), (x  , y-1), (x+1, y-1),
        ]
