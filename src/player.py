# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room):
        self.current_health = 100
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"{self.name} is at {self.current_room.name}"

    def setRoom(self, room):
        self.current_room = room
        print("\n")
        print(room)
        print("\n")

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        newItem = self.items[item]
        print(f"{newItem.name} was dropped.\n")
        self.items.pop(item)
        self.current_room.addItem(newItem)

    def hurt(self, amount):
        self.current_health -= amount
