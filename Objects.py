import pygame

MOB_WIDTH = 128
MOB_HEIGHT = 256

################################################
####    The mob class is for both humans    ####
####    and zombies and contains methods    ####
################################################    
class Mob():
    
    def __init__(self, ID, mob_type, location, images):
        self.ID = ID
        self.mob_position = 0,0
        self.type = mob_type
        self.location = location
        self.image = images

    def set_location(self, new_location):
        self.location = new_location
        
    def set_position(self, x, y):
        self.mob_position = x, y
        
    def get_location(self):
        return self.location
    
    def get_type(self):
        return self.type
    
    def get_image(self):
        return pygame.image.load(self.image).convert_alpha()
    
    def get_position(self):
        return self.mob_position
    

class Location():
    
    def __init__(self, location_name):
        self.name = location_name
        self.mobs_at_location = []
    
    def remove_mob(self, Mob):
        self.mobs_at_location.remove(Mob)
        
    def add_mob(self, Mob):
        self.mobs_at_location.append(Mob)
    
    def get_number_of_mobs_at_location(self):
        return self.mobs_at_location.__len__()
   
    
        
class Elevator(Location):
    
    def __init__(self):
        self.mobs_at_location = []
        self.image_path = "lift.jpg"
        self.name = "elevator"
        self.current_location = "lobby"
        self.elevator_position = (0,0)
        
    def move(self):
        if(self.current_location == "lobby"):
            self.current_location = "penthouse"
        else:
            self.current_location = "lobby"
            
    def set_position(self, position_in):
        self.elevator_position = position_in
    
    def get_position(self):
        return self.elevator_position
        
    def check_full(self):
        if(len(self.mobs_at_location) == 2):
            return True
        else:
            return False
        
    def get_image(self):
        return pygame.image.load(self.image_path).convert()    
    
