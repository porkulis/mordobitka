import random
def roll(min, max):
    result = random.randint(min, max)
    return result

class Room:
    def __init__ (self, name):
        self.name = name
        self.exits = {}

    def add_exits(self, diretion, next_room):
        self.exits[direction] = next_room

    def look(self):
        print(self.name)
        print(self.exits)
    
room1 = Room("Komnata 1")
room2 = Room("Komnata 2")
room3 = Room("Komnata 3")
room4 = Room("Komnata 4")