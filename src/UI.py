class Buttons:
    """ this class creates a button, it collets the width/height of the button, selects its location"""
    
    def __init__(self, x, y, image, file, scale):
        """width = file.get_width()
        height = file.get_height() I NEED TO FIGURE OUT HOW TO MAKE THIS SCALE"""
        
        self.x = x
        self.y = y
        self.file = file
        self.image = pygame.image.load(self.file)
        """self.image = pygame.transform.scale(image, (int(width * scale)), (int(height * scale))) """
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        """here we can see if the buttons been clicked"""
        self.clicked = False
        
    def draw(self, screen):    
        """this gets the mouse possition"""
        pos = pygame.mouse.get_pos()
        
        """this checks if the mouse possition is over a button"""
        if self.rect.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                button.clicked = True
                
                
        """this turns the clicked off after its clicked"""
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
            
        screen.blit(self.image, (self.x, self.y))    
        

"""this creates buttons that get added to a list thats blitted later on"""
button_list = []

house_button = Buttons(300, 300, "button",r"C:\Users\jstee\OneDrive\Desktop\python\ski_game_assets\arrow_left.png", 1)  
button_list.append(house_button)  

blood_farm_button = Buttons(300, 300, "button",r"C:\Users\jstee\OneDrive\Desktop\python\ski_game_assets\arrow_left.png", 1)    
button_list.append(blood_farm_button)

mine_button = Buttons(300, 300, "button",r"C:\Users\jstee\OneDrive\Desktop\python\ski_game_assets\arrow_left.png", 1)  
button_list.append(mine_button)  

lumber_mill_button = Buttons(300, 300, "button",r"C:\Users\jstee\OneDrive\Desktop\python\ski_game_assets\arrow_left.png", 1)    
button_list.append(lumber_mill_button)

stable_button = Buttons(300, 300, "button",r"C:\Users\jstee\OneDrive\Desktop\python\ski_game_assets\arrow_left.png", 1)  
button_list.append(stable_button)
  
lab_button = Buttons(300, 300, "button",r"C:\Users\jstee\OneDrive\Desktop\python\ski_game_assets\arrow_left.png", 1)  
button_list.append(lab_button)