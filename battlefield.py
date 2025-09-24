class Battlefield:
    
    def __init__(self,gridsquare):
        self.gridsquare = gridsquare

    @staticmethod
    def create_battlefield(gridsquare):
        field = []
        
        for i in range(gridsquare):
            row = []
            row = [0]*10
            field.append(row)
        return field
    

    @staticmethod       
    def print_field(field):
        i = 1
        print(" ",end="")
        for a in range(len(field)):
            print(a+1,end="  ")
        print("\n")

        for row in field:
            print(row,i)
            i += 1

    @staticmethod
    def collision_checker(coordinates,field):
        for i,value in enumerate(coordinates):
            if field[value[1]][value[0]] == 1:
                collision = True
                return collision

        return False

    def add_ship(player,index):
        print(f"\n...Adding ship number : {index + 1} ...")
        for i in player.ship_list[index].coordinate:
            print(i,end="\n")
            column = i[0]-1
            row = i[1]-1
            print(player.field[row][column])
            player.field[row][column] = 1


