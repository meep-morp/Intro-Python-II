from art import title

from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Lantern", "Could be useful in a dark cave.", ["emit_light"])]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                     passages run north and east.""", [Item('Bronze Blade', "The cracked weapon shines modestly, but it's history is brilliant")], ["emit_light"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south."""),
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

    # CHECK IF ITEMS ARE AVAILABLE
    # if len(player.current_room.items) > 0:
    #     for i in player.current_room.items:
    #         print(f"{player.name} found {i.name}\n{i.description}\n")
    #         user = input("Take item?\n[ Y ] [ N ]\n")

    #         if(user.upper() == "Y"):
    #             player.addItem(i)
    #             player.current_room.items.remove(i)
    #             print("Item Obtained\n")
    #         else:
    #             break

    # CHECK LIGHT SOURCES
    # if("emit_light" not in player.current_room.attrs):
    #     for item in player.items:
    #         if "emit_light" in item.attrs:
    #             break
    #         else:
    #             print("It's Pitch black!")
    #             user = input("Return to entrance?\n[ Y ] [ N ]\n")
    #             if(user.upper() == "Y"):
    #                 player.setRoom(room['outside'])

    #             else:
    #                 print("You were eaten by Grue.")
    #                 user = "q"
    #                 break

    # CHECK CURRENT ROOM
    for r in room:
        print(room[r])
        if(room[r] == player.current_room):
            user = input(
                "Which Direction do you take?\n[ N ] [ E ] [ S ] [ W ]\n")
            if(user.upper() == "E"):
                if(room[r].e_to == None):
                    print("You cannot go that way!")
                else:
                    player.setRoom(room[r].e_to)

            elif(user.upper() == "S"):
                if(room[r].s_to == None):
                    print("You cannot go that way!")
                else:
                    player.setRoom(room[r].s_to)

            elif(user.upper() == "N"):
                if(room[r].n_to == None):
                    print("You cannot go that way!")
                else:
                    player.setRoom(room[r].n_to)

            elif(user.upper() == "W"):
                if(room[r].w_to == None):
                    print("You cannot go that way!")
                else:
                    player.setRoom(room[r].w_to)

            else:
                print("Please choose to continue...")
