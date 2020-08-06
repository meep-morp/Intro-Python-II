import random


class Enemy():
    def __init__(self, name, description, baseHealth, baseAttack):
        self.name = name
        self.description = description
        self.baseHealth = baseHealth
        self.baseAttack = baseAttack
        self.currentHealth = baseHealth

    def hurt(self):
        amount = random.randrange(1, self.baseHealth)
        self.currentHealth -= amount
        return amount

    def attack(self):
        return random.randrange(self.baseAttack, self.baseAttack + 10)

    def __str__(self):
        return self.name
