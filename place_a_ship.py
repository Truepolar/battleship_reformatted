#orientation

def place_a_ship():

    #ask for column
    print("Please select a column number from 1-10")
    while True:
        try:
            column = int(input("Column : "))
        except:
            print("-----invalid input-----\n")
        else:
            if column < 1 or column > 10:
                print("Please choose a number between 1 and 10\n")
            else:
                break

    #ask for row
    print("\nPlease select a row number from 1-10")
    while True:
        try:
            row = int(input("Row : "))
        except:
            print("-----invalid input-----\n")
        else:
            if row < 1 or row > 10:
                print("Please choose a number between 1 and 10\n")
            else:
                break


    #ask for length
    print("\nPlease select ship length from 3-5")
    while True:
        try:
            length = int(input("Length : "))
        except:
            print("-----invalid input-----\n")
        else:
            if length < 3 or length > 5:
                print("Please choose a number between 3 and 5\n")
            else:
                break


    #ask for orientation
    print("\nPlease select an orientation, 1 for vertical | 0 for horizontal")
    while True:
        try:
            orientation = int(input("Orientation : "))
        except:
            print("-----invalid input-----\n")
        else:
            if orientation < 0 or orientation > 1:
                print("Please choose a number between 0 and 1\n")
            else:
                break
        
    return [column,row,orientation,length]




#This is to process the coords for the ship
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