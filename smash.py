import random

class Character:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

    def decrement_health(self, damage):
        self.health -= damage

    def random_attack(self):
        return random.choice(self.attacks)

class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def fight(self):
        while self.character1.health > 0 and self.character2.health > 0:
            attack1 = self.character1.random_attack()
            self.character2.decrement_health(attack1['damage'])
            print(f"{self.character1.name} attacks {self.character2.name} with {attack1['name']} for {attack1['damage']} damage.")
            if self.character2.health <= 0:
                print(f"{self.character2.name} has been defeated!")
                break

            attack2 = self.character2.random_attack()
            self.character1.decrement_health(attack2['damage'])
            print(f"{self.character2.name} attacks {self.character1.name} with {attack2['name']} for {attack2['damage']} damage.")
            if self.character1.health <= 0:
                print(f"{self.character1.name} has been defeated!")
                break

        if self.character1.health > 0:
            return self.character1.name
        else:
            return self.character2.name
