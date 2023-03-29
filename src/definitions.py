SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900
FPS = 30 #Currrently unused. Can be added to clock.tick() in main loop
TOOLBAR_HEIGHT = 40

BG_TILE_SIZE = 100 #height and width length
ROW_COUNT = 6
COL_COUNT = 50

class I_Vec2:
    """"2D integer vector"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return I_Vec2(self.x + other.x, self.y + other.y)    

    def __sub__(self, other):
        return I_Vec2(self.x - other.x, self.y - other.y)    

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"x:{self.x}, y:{self.y}\n"

    def tup(self)->tuple:
        """Returns tuple in format (x, y)"""
        return (self.x, self.y)
class F_Vec2:
    """2D float vector"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def tup(self)->tuple:
        """Returns tuple in format (x, y)"""
        return (self.x, self.y)