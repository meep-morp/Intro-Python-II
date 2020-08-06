# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, items=[], enemies=[]):
        self.name = name
        self.description = description
        self.items = items
        self.enemies = enemies

    def __str__(self):
        return f"{self.name}\n{self.description}"

    def takeItem():
        pass

    def addItem(self, item):
        self.items.append(item)
