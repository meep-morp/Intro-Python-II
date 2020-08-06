# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, items=[], attrs=[], enemy=[]):
        self.name = name
        self.description = description
        self.items = items
        self.attrs = attrs
        self.enemy = enemy

    def __str__(self):
        return f"{self.name}\n{self.description}"
