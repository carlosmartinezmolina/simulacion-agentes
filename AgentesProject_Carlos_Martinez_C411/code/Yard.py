class Yard:
    def __init__(self):
        self.symbol = '#'
        self.childrenSymbol = '$'
        self.robotSymbol = '@'
        self.children = False
        self.robot = False
        self.robotCarryOnChildren = False
        
    def thereAreChildren(self):
        return self.chilfren