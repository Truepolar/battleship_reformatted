def collision_checker(coordinates,field):
    for i,value in enumerate(coordinates):
        if field[value[1]][value[0]] == 1:
            collision = True
            return collision

    return False


