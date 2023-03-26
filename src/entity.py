from definitions import F_Vec2

class Ent_Comp:
    """Component containing variables found in all entities"""
    ent_count = 0
    def __init__(self, texture: str, pos: F_Vec2)->None:
        self.texture = pygame.image.load(texture)
        self.rect = self.texture.get_rect()
        self.visible: bool = 1
        self.pos = pos
        
        self.ID = ent_count
        ent_count += 1
class Interact_Comp:
    """Interact component. Holds data for entities that player can click on"""
    def __init__(self)->None:
        selected: bool = 0
        mouse_over: bool = 0
