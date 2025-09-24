from player import Player


class Ship:

    def __init__(self,coordinate,status = True):
        self.coordinate = coordinate
        self.status = status


    @staticmethod
    def footprint_processing(coordinate_set):
        coordinate_list = []

        #horizontal
        if coordinate_set[2] == 0:
            for i in range(coordinate_set[3]):
                temp_coordinate = [coordinate_set[0],coordinate_set[1]]
                coordinate_set[0] += 1
                coordinate_list.append(temp_coordinate)
        
        #vertical
        else:
            for i in range(coordinate_set[3]): 
                temp_coordinate = [coordinate_set[0],coordinate_set[1]]
                coordinate_set[1] += 1
                coordinate_list.append(temp_coordinate)
        
        return(coordinate_list)
    
    def add_coordinate(player,coordinate_list):
        temp_ship = Ship(coordinate_list)
        player.ship_list.append(temp_ship)