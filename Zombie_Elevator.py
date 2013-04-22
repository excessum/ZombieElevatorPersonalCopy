import pygame

import Objects
import sys

##################################################
####    Final static variables that can be    ####
####    easily edited depending on needs.     ####
####    Also holds positions of elevators     ####
##################################################

LOBBY_ELEVATOR_POSITION = (10,550) 
PENTHOUSE_ELEVATOR_POSITION = (10,50) 
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

#################################################
####    Create all the objects with the      ####
####    values in globals scope so all       ####
####    the methods can use them easily      ####
#################################################

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
human1 = Objects.Mob('1','human', 'lobby', 'Human1.png')
human2 = Objects.Mob('2','human', 'lobby', 'Human2.png')
human3 = Objects.Mob('3','human', 'lobby', 'Human3.png')
zombie1 = Objects.Mob('1','zombie', 'lobby', 'Zombie1.png')
zombie2 = Objects.Mob('2','zombie', 'lobby', 'Zombie2.png')
zombie3 = Objects.Mob('3','zombie', 'lobby', 'Zombie3.png')
elevator = Objects.Elevator()
elevator.set_position(LOBBY_ELEVATOR_POSITION)

#################################################
####    Main methods that acts as a          ####
####    controller allowing easy menu        ####
####    switches.                            ####
#################################################

def main():
    main_loop('girl')
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        title_screen_input = title_screen()
        x, y = title_screen_input.split(',')
        if x == 'play':
            main_loop(y)
        elif x == 'instructions':
            instructions()

def title_screen():
    pass


################################################
####    Main loop contains all the code for ####
####    the main game including the logic   ####
################################################
            
def main_loop(gender):

################################################
####    Declaring all variables that are    ####
####    not of global scope and setting     ####
####    there values if applicable          ####
################################################

    lobby = Objects.Location('lobby')
    penthouse = Objects.Location ('penthouse')
    running = 1    
    lobby.add_mob(human1)
    lobby.add_mob(human2)
    lobby.add_mob(human3)
    lobby.add_mob(zombie1)
    lobby.add_mob(zombie2)
    lobby.add_mob(zombie3)
    h_x_position_array = [150, 225, 325]
    z_x_position_array = [725, 625, 525]
    lobby_y_position = 630
    pent_y_position = 250
    human1.set_position(h_x_position_array[0], lobby_y_position)
    human2.set_position(h_x_position_array[1], lobby_y_position)
    human3.set_position(h_x_position_array[2],lobby_y_position)
    zombie1.set_position(z_x_position_array[0], lobby_y_position)
    zombie2.set_position(z_x_position_array[1], lobby_y_position)
    zombie3.set_position(z_x_position_array[2], lobby_y_position)
    
################################################
####    Set a default selected mob so the   ####
####    selected_mob can access Mob object  ####
####    methods and then set the bg image   ####
####    depending on the gender passed in   ####
####    the parameter.                      ####
################################################
    
    selected_mob = human1
    if gender == 'girl':
        background = pygame.image.load('girl_background.jpg').convert()
    else:
        background = pygame.image.load('boy_background.jpg').convert()
    while running:
        for event in pygame.event.get():
            
            ################################################
            ####    All this code is detecting the key  ####
            ####    events through pygame and reacting  ####
            ####    with the appropriate logic          ####
            ################################################
            
            if event.type == pygame.QUIT:
                running = 0
                    
            if event.type == pygame.KEYDOWN:
                
                ################################################
                ####    If any of the number keys 1 to 6    ####
                ####    are pressed, select the Mob object  ####
                ####    that it references.                 ####
                ####    1: human1, 2: human2, 3:human3      ####
                ####    4: zombie1, 5: zombie2, 6:zombie3   ####
                ################################################
                
                if event.key == pygame.K_1:
                    selected_mob = human1
                    print 'human 1 selected'
                elif event.key == pygame.K_2:
                    selected_mob = human2
                    print 'human 2 selected'
                elif event.key == pygame.K_3:
                    selected_mob = human3
                    print 'human 3 selected'
                elif event.key == pygame.K_4:
                    selected_mob = zombie3
                    print 'zombie 1 selected'
                elif event.key == pygame.K_5:
                    selected_mob = zombie2
                    print 'zombie 2 selected'
                elif event.key == pygame.K_6:
                    selected_mob = zombie1
                    print 'zombie 3 selected'
                    
                ################################################
                ####    If the left key is pressed and the  ####
                ####    mob is not currently in the lift    ####
                ####    AND the elevator is currently on    ####
                ####    same floor AND the lift is not full ####
                ####    move the mob into the lift.         ####
                ################################################
                    
                if event.key == pygame.K_LEFT:
                    print 'left key pressed'
                    if selected_mob.get_location() != "elevator":    
                        if selected_mob.get_location() == "lobby":
                            if elevator.current_location == "lobby":
                                if elevator.check_full() == False:
                                    lobby.remove_mob(selected_mob)
                                    elevator.add_mob(selected_mob)
                                    selected_mob.set_location('elevator')
                                    x, y = LOBBY_ELEVATOR_POSITION
                                    selected_mob.set_position(x,y) #PLACE HOLDER FOR WHERE GROUND ELEVATOR IS LOCATED
                            else:
                                if elevator.current_location == "penthouse":
                                    if elevator.check_full():
                                        penthouse.remove_mob(selected_mob)
                                        selected_mob.set_location('elevator')
                                        elevator.add_mob(selected_mob)
                                        selected_mob.set_pos(PENTHOUSE_ELEVATOR_POSITION) # PLACE HOLDER FOR PENTHOUSE ELEVATOR
                                        
                ################################################
                ####    If the right key is pressed and the ####
                ####    mob is currently in the lift then   ####
                ####    move the mob from the elevator onto ####
                ####    the floor where the elevator is     ####
                ####    located and check for win/loss      ####
                ################################################
                                        
                if event.key == pygame.K_RIGHT:
                    print selected_mob.get_type()
                    print 'right key pressed'
                    if selected_mob.get_location() == 'elevator':
                        if elevator.current_location == "lobby":
                            if selected_mob.get_type() == 'human': 
                                selected_mob.set_position(h_x_position_array[int(selected_mob.ID)-1],lobby_y_position)
                            else:
                                selected_mob.set_position(z_x_position_array[int(selected_mob.ID)-1],lobby_y_position)
                            selected_mob.set_location('lobby')
                            elevator.remove_mob(selected_mob)
                            lobby.add_mob(selected_mob)
                        else:
                            if selected_mob.get_type() == 'human': 
                                selected_mob.set_position(h_x_position_array[int(selected_mob.ID)-1],lobby_y_position)
                            else:
                                selected_mob.set_position(z_x_position_array[int(selected_mob.ID)-1],lobby_y_position)
                            elevator.remove_mob(selected_mob)
                            selected_mob.set_location('penthouse')
                            lobby.add_mob(selected_mob)
                        if penthouse.get_number_of_mobs_at_location() == 6:
                            victory()
                        else:
                            loop_counter = 0
                            z_counter = 0
                            h_counter = 0
                            #################################################
                            ####    Loop through penthouse to check for   ###
                            ####        victory or defeat conditions      ###
                            #################################################
                            
                            while loop_counter < penthouse.get_number_of_mobs_at_location():
                                if penthouse.mobs_at_location[loop_counter].get_type == 'zombie':
                                    z_counter += 1
                                else:
                                    h_counter += 1
                                    loop_counter +=1
                                                                       
                                if z_counter > h_counter:
                                    game_over()
                                    
                            #################################################
                            ###########Reset all the counters################
                            #################################################
                                    
                            loop_counter = 0
                            z_counter = 0
                            h_counter = 0
                                
                            #################################################
                            ####       Loop through lobby to check for    ###
                            ####        victory or defeat conditions      ###
                            #################################################
             
                            while (loop_counter < lobby.get_number_of_mobs_at_location()) and (lobby.get_number_of_mobs_at_location() != 0) :
                                if lobby.mobs_at_location[loop_counter].get_type == 'zombie':
                                    z_counter += 1
                                else:
                                    h_counter += 1
                                    loop_counter +=1
                                                                       
                                if z_counter > h_counter:
                                    game_over()
                                    
                ################################################
                ####    If the up key is pressed when the   ####
                ####    elevator is at the lobby and there  ####
                ####    is at least one mob currently in    ####
                ####    the elevator then move the elevator ####
                ####    up.                                 ####
                ################################################
                                    
                if event.key == pygame.K_UP:
                    if elevator.current_location == 'lobby':
                        if elevator.get_number_of_mobs_at_location() == 0:
                            pass
                        else:
                            move_elevator('up')
                            
                ################################################
                ####    If the down key is pressed when the ####
                ####    elevator is at the penthouse and    ####
                ####    there is at least one mob currently ####
                ####    in the elevator then move the       ####
                ####    elevator down.                      ####
                ################################################
                            
                if event.key == pygame.K_DOWN:
                    if elevator.current_location == 'penthouse':
                        if elevator.get_number_of_mobs_at_location() == 0:
                            pass
                        else:
                            move_elevator('down')
        screen.blit(background, (0, 0))
        
        
        
        ################################################
        ####            Redraw the screen           ####
        ################################################
        
        repaint()
        pygame.display.update()
 
################################################
####    Method used to move a mob from one  ####
####    location to another, just used to   ####
####    make code easier to read.           ####
################################################
        
def move_mob(mob, from_location, to_location):
    from_location.remove_mob(mob)
    to_location.add_mob(mob)
    
#################################################
####    Method used to do the victory screen ####
####    and procedure once victory condition ####
####    is met                               ####
#################################################
    
def victory():
    #Do victory procedure
    print 'victory!'
    
#################################################
####    Method used to do the defeat screen  ####
####    and procedure once defeat condition  ####
####    is met                               ####
#################################################
    
def game_over():
    #Do game over procedure
    print 'game over!'

#################################################
####    Method used to move the elevator up  ####
####    or down with the characters in an    ####
####    animated fashion                     ####
#################################################
def move_elevator(direction):
    pass
    
#################################################
####    Method used to repaint all the       ####
####    objects that can move positions      ####
#################################################

def repaint():
    screen.blit(human1.get_image(), human1.get_position())
    screen.blit(human2.get_image(), human2.get_position())
    screen.blit(human3.get_image(), human3.get_position())
    screen.blit(zombie1.get_image(), zombie1.get_position())
    screen.blit(zombie2.get_image(), zombie2.get_position())
    screen.blit(zombie3.get_image(), zombie3.get_position())
    screen.blit(elevator.get_image(), elevator.elevator_position)

def instructions():
    pass

if __name__ == '__main__':
    main()
    
    
                
        
    
