import random
import time

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
            print(f"-Imię: {self.name_m}, Życie: {self.current_hp}/{self.max_hp}")

    def attack(self, attacked):
         print(f"\n{self.name_m} atakuje {attacked.name_d}!")
         time.sleep(2)
         #szansa na unik
         attack_speed = self.agility + roll(1,6)
         avoid_chance = attacked.agility + roll(1,4)
         if attack_speed > avoid_chance:
            #szansa na blok
            attack_chance = self.strenght + self.agility + roll(1,6)
            block_chance = attacked.strenght + attacked.agility + roll(1,4)
            if attack_chance > block_chance:
                damage = self.strenght + roll(2, 4)
                attacked.current_hp -= damage
                print(f"--{self.name_m} trafia {attacked.name_d} zadając {damage} pkt. obrażeń")
                time.sleep(2)
                print(f"--{self.name_m}: {self.current_hp}/{self.max_hp} pkt życia\n--{attacked.name_m}: {attacked.current_hp}/{attacked.max_hp} pkt życia")
            else:
                 print(f"--BLOK ({attack_chance}/{block_chance})")
         else:
              print(f"--UNIK ({attack_speed}/{avoid_chance})")


player = Character("Mruczek", "Mruczka", "kot", 18, 12, 20, 30, 30, 0)
enemy = Character("Burek", "Burka", "pies", 16, 15, 20, 30, 30, 0)
enemy1 = Character("Ślimior", "Ślimiora", "ślimak", 10, 1, 1, 30, 30, 0)

attacked = enemy


def fight(attacker, defender):
    while True:
        time.sleep(2)
        attacker.attack(defender)
        if defender.current_hp < 1:
            time.sleep(2)
            print("Zwyciestwo")
            break
        time.sleep(2)
        defender.attack(attacker)
        if attacker.current_hp < 1:
            time.sleep(2)
            print("Porażka")
            break

player.przedstaw()
enemy.przedstaw()
fight(player, enemy)

answer = input("Czy chcesz zażyć miksturę życia? (tak/nie)")
if answer == "tak":
    print("Ozdrowienie!")
    player.current_hp = player.max_hp

player.przedstaw()
enemy1.przedstaw()
fight(player, enemy1)



