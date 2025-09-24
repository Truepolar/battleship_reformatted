from game_manager import Game_manager
from battlefield import Battlefield
from player import Player
from ship import Ship

print("Hello, Welcome to battleship.\n Press the enter key to start")
a = input()


#Display field
print("This is the battlefield")
player_field = Battlefield.create_battlefield(10)
Battlefield.print_field(player_field)


#asking how many ships to play with
print("How many ships would you like to play with, (1-5)")
while True:
    try:
        no_of_ships = int(input("Number of ships : "))
    except:
        print("-----invalid input-----\n")
    else:
        if no_of_ships < 1 or no_of_ships > 5:
            print("Please choose a number between 1 and 5\n")
        else:
            break
            
a = input()


#Create player object
player = Player(player_field)


#asking coords
for i in range(no_of_ships):
    collision = True
    while collision == True:
        collision = False
        temp_coordinate = Game_manager.promt_placement()
        coordinate_list = Ship.footprint_processing(temp_coordinate)
        collision = Battlefield.collision_checker(coordinate_list,player_field)
        if collision == False:
            Ship.add_coordinate(player,coordinate_list)
            Battlefield.add_ship(player,i)
        else:
            print("-----Invalid ship placement-----\n")
        Battlefield.print_field(player.field)