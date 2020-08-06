# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = [Item("Stick", "Not the best weapon you could have..")]

    def __str__(self):
        return f"{self.name} is at {self.current_room.name}"

    def setRoom(self, room):
        self.current_room = room
        print("\n")
        print(room)
        print("\n")

    def addItem(self, item):
        self.items.append(item)
