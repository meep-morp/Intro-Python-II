from art import title

from room import Room
from player import Player
from enemy import Enemy
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                     passages run north and east.""", [Item('Bronze Blade', "The cracked weapon shines modestly, but it's history is brilliant")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south.""", [], [Enemy("The Serpent", "The Serpent's eyes bore into you, angered at your invasion of it's home.", 200, 50)]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# CONTROLS

print("Starting..")
print(title)
print("\nPress 'q' to quit\n")
user = input("\nWhat is your name?\n")
player = Player(user, room['outside'])
print(player)
print("\n")
print(player.current_room)
print("\n")

while not user == "q":
    # Game Loop

    if(player.current_health <= 0):
        user = "q"
        print(
            "Your injuries were too grave, you died bravely in Serpent's Lair")

    #  Drop Item
    if user == "drop":
        print("Current Items\n")
        for i, item in enumerate(player.items):
            print(f"[ {i} ]\n")
            print(item.name)
            print("\n")

        if user.lower() == "cancel":
            break

        num = int(input("Which item do you want to drop?\n"))
        player.dropItem(num)

    # CHECK IF ITEMS ARE AVAILABLE
    if len(player.current_room.items) > 0:
        for i in player.current_room.items:
            print(f"{player.name} found {i.name}\n{i.description}\n")
            user = input("Take item?\n[ Y ] [ N ]\n")

            if(user.upper() == "Y"):
                player.addItem(i)
                player.current_room.items.remove(i)
                print("Item Obtained\n")
            else:
                break

    # Check if enemies are around
    if len(player.current_room.enemies) > 0:

        for i in player.current_room.enemies:
            print(f"{player.name} found {i.name}\n{i.description}\n")
            user = input("Attack?\n[ Y ] [ N ]\n")

            if i.currentHealth <= 0:
                print("Enemy Defeated")

            while i.currentHealth >= 0:
                if(user.upper() == "Y"):

                    amount = i.hurt()
                    print(f"{i.name} hit for {amount}\n")

                    eneAttack = i.attack()
                    player.hurt(eneAttack)
                    print(f"{i.name} hit {player.name} for {eneAttack}\n")

                else:
                    print("You ran away in fear of the monster.")
                    user = 'q'

    # OUTSIDE
    if(player.current_room == room['outside']):
        user = input("Enter the cave?\n[ Y ] [ N ]\n")

        if(user.upper() == "Y"):
            player.setRoom(room['outside'].n_to)

        else:
            print(
                "You chicken out and return home to your mother's, where you live out the rest of your days.")
            user = 'q'

    # FOYER
    elif(player.current_room == room['foyer']):
        user = input("Which direction will you move?\n[ E ] [ N ] [ S ]\n")

        if(user.upper() == "E"):
            player.setRoom(room["foyer"].e_to)

        elif(user.upper() == "S"):
            player.setRoom(room["foyer"].s_to)

        elif(user.upper() == "N"):
            player.setRoom(room["foyer"].n_to)

        else:
            print("Please choose to continue...")

    # OVERLOOK
    elif(player.current_room == room['overlook']):
        user = input("Which direction will you move?\n[ S ]\n")

        if(user.upper() == "S"):
            player.setRoom(room["overlook"].s_to)
        else:
            print("Please choose to continue...")

    # NARROW
    elif(player.current_room == room['narrow']):
        user = input("Which direction will you move?\n[ W ] [ N ]\n")
        if(user.upper() == "W"):
            player.setRoom(room["narrow"].w_to)

        elif(user.upper() == "N"):
            player.setRoom(room["narrow"].n_to)

        else:
            print("Please choose to continue...")

    # TREASURE
    elif(player.current_room == room['treasure']):
        user = input("Which direction will you move?\n[ S ]\n")

        if(user.upper() == "S"):
            player.setRoom(room["treasure"].s_to)

        else:
            print("Please choose to continue...")
