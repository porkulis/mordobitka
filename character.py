import random
import time
import os
clear = lambda: os.system('cls')

def roll(min, max):
     result = random.randint(min, max)
     return result
     
class Character:
    def __init__ (self, name_m, name_d, race, strenght, agility, condition, max_hp, current_hp, experience_points):
        self.name_m = name_m
        self.name_d = name_d
        self.race = race
        self.strenght = strenght
        self.agility = agility
        self.condition = condition
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.experience_points = experience_points

    def przedstaw(self):
            print(f"Imię: {self.name_m}, Życie: {self.current_hp}/{self.max_hp}")

    def attack(self, attacked):
        clear()
        print(f"{self.name_m} atakuje {attacked.name_d}.\n\n")
        print_hp(a, b)
        time.sleep(2)
        #szansa na unik
        attack_roll = roll(1,9)
        attack_speed = self.agility + attack_roll + 5
        defend_roll = roll(1,9)
        avoid_chance = attacked.agility + defend_roll
        if attack_roll > 6:
            attack_description = "błyskawiczny"
        elif attack_roll > 3:
            attack_description = "standardowy"
        else:
            attack_description = "powolny"
        clear()
        print(f"{self.name_m} atakuje {attacked.name_d}.")
        print(f"{self.name_m} wyprowadza {attack_description} atak!\n")
        print_hp(a, b)
        time.sleep(2)
        if attack_speed > avoid_chance:
            #szansa na blok
            attack_chance = self.strenght + self.agility + attack_roll + 5
            block_chance = attacked.strenght + attacked.agility + defend_roll
            if attack_chance > block_chance:
                damage = int((2 * roll(2, 4)) * (self.strenght/10))
                attacked.current_hp -= damage
                clear()
                print(f"{self.name_m} atakuje {attacked.name_d}.")
                print(f"{self.name_m} wyprowadza {attack_description} atak!")
                print(f"{self.name_m} trafia {attacked.name_d} zadając {damage} pkt. obrażeń")
                print_hp(a, b)
                time.sleep(2)
            else:
                clear()
                print(f"{self.name_m} atakuje {attacked.name_d}.")
                print(f"{self.name_m} wyprowadza {attack_description} atak!")
                print(f"BLOK ({attack_chance} vs {block_chance})")
                print_hp(a, b)
                time.sleep(2)
        else:
            clear()
            print(f"{self.name_m} atakuje {attacked.name_d}.")
            print(f"{self.name_m} wyprowadza {attack_description} atak!")
            print(f"UNIK ({attack_speed} vs {avoid_chance})")
            print_hp(a, b)
            time.sleep(2)
        clear()
        print(f"\n\n")
        print_hp(a, b)

#strenght, agility, condition, max_hp, current_hp, experience_points
player = Character("Mruczek", "Mruczka", "kot", 15, 15, 20, 50, 50, 0)
enemy = Character("Burek", "Burka", "pies", 15, 15, 20, 12, 12, 0)
enemy1 = Character("Ślimior", "Ślimiora", "ślimak", 10, 1, 1, 30, 30, 0)
enemy2 = Character("Goblin", "Goblina", "goblin", 15, 15, 20, 12, 12, 0)
enemy3 = Character("Behemot", "Behemota", "behemot", 30, 30, 20, 100, 100, 0)




def fight(attacker, defender):
    while True:
        time.sleep(2)
        attacker.attack(defender)
        if defender.current_hp < 1:
            time.sleep(2)
            clear()
            print(f"{defender.name_m} pada na ziemię brocząc krwią.\n\n")
            print_hp(a, b)
            time.sleep(2)
            clear()
            print(f"Zwyciestwo!\n\n")
            print_hp(a, b)
            break
        time.sleep(2)
        defender.attack(attacker)
        if attacker.current_hp < 1:
            clear()
            print(f"{attacker.name_m} pada na ziemię brocząc krwią.\n\n")
            print_hp(a, b)
            time.sleep(2)
            clear()
            print(f"Porażka!\n\n")
            break

def print_hp(a, b):
    print(f'''
________________________________________________
{a.name_m}: [{a.current_hp}] HP vs {b.name_m} [{b.current_hp}] HP
    ''')

a=player

def set_fight(opponent):
    global b
    b = opponent
    fight(a, b)

