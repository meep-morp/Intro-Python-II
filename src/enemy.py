class Enemy():
    def __init__(self, name, baseHealth, baseAttack):
        self.name = name
        self.baseHealth = baseHealth
        self.baseAttack = baseAttack

    def __str__(self):
        return self.name
