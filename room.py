import random
def roll(min, max):
    result = random.randint(min, max)
    return result

class Room:
    def __init__ (self, name, description, exit_n, exit_e, exit_s, exit_w):
        self.name = name
        self.exit_n = exit_n
        self.exit_e = exit_e
        self.exit_s = exit_s
        self.exit_w = exit_w
        self.description = description

    def look(self):
        print(self.name)
    
    
room = Room("Komnata 1", None, None, None, None, "Znajdujesz się w pierwszej komnacie. Są tu 4 wyścia.")

room.look()

def create_room():
    room1 = Room("Komnata 2", None, None, None, None, "Znajdujesz się w drugiej komnacie. Są tu 4 wyścia.")
    exits_roll = roll(1,3)
    print(exits_roll)
    return room1

print(room.name)
create_room()
print(room1.name)

exits = {"n": "polnoc", "e": "wschod", "s": "poludnie", "w": "zachod"}