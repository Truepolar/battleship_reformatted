class Player:

    def __init__(self,field,ship_list = None,health = None):
        self.field = field
        self.ship_list = ship_list or []
        self.health = health

    
