class Battlefield:
    
    def __init__(self,gridsquare):
        self.gridsquare = gridsquare

    @staticmethod
    def create_battlefield(gridsquare):
        field = []
        row = []

        for o in range (gridsquare):
            row.append(0)
        for i in range(gridsquare):
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


    def add_ship():
        print() 

