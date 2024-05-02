class Weapon:
    def __init__ (self, name_m, name_d, name_n, damage):
        self.name_m = name_m
        self.name_d = name_d
        self.name_n = name_n
        self.damage = damage
    
class Armor:
    def __init__ (self, name_m, name_d, defence):
        self.name_m = name_m
        self.name_d = name_d
        self.defence = defence

nic = Weapon("pięść", "pięści", "pięściami", 0)
miecz = Weapon("miecz", "miecza", "mieczem", 10)
promien = Weapon("promień słońca", "promienia słońca", "promieniem słońca", 100)
brak = Armor("brak", "brak", 0)
zbroja = Armor("zbroja", "zbroję", 10)