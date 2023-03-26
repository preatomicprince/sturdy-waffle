SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900
FPS = 60 #Currrently unused. Can be added to clock.tick() in main loop

BG_TILE_SIZE = 16 #height and width length
ROW_COUNT = 20
COL_COUNT = 40
class I_Vec2:
    """"2D integer vector"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class F_Vec2:
    """2D float vector"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def tup(self)->tuple:
        """Returns tuple in format (x, y)"""
        return (self.x, self.y)