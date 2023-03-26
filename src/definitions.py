SCREEN_HEIGHT = 500
SCREEN_WIDTH = 700
FPS = 30 #Currrently unused. Can be added to clock.tick() in main loop

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