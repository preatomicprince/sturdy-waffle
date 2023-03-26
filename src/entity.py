from definitions import F_Vec2

class Ent_Comp:
    """Component containing variables found in all entities"""
    def __init__(self, texture: str, pos: F_Vec2):
        self.texture = pygame.image.load(texture)
        self.rect = self.texture.get_rect()
        self.pos = pos