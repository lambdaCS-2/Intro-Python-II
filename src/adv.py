from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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
player = Player(room['outside'])


welcome_message = "Welcome to the Adventure Game!"
wrong_way = "Nothing that way. You must turn back!"
success_message = "You found the treasure!"
quit_message = "Thanks for playing! Goodbye!"


print(welcome_message)
while True:

    print(f"You're current location is: {player.room.location} {player.room.description}")

    player_choice = input(
        "Where will you go? [n] north [s] south [e] east [w] west [q] quit:")

    if player.room.location == "Treasure Chamber":
        print(success_message)
        break

    if player_choice == "n":
        if player.room.n_to:
            player.room = player.room.n_to
        else:
            print(wrong_way)
    elif player_choice == "s":
        if player.room.s_to:
            player.room = player.room.s_to
        else:
            print(wrong_way)
    elif player_choice == "e":
        if player.room.e_to:
            player.room = player.room.e_to
        else:
            print(wrong_way)
    elif player_choice == "w":
        if player.room.w_to:
            player.room = player.room.w_to
        else:
            print(wrong_way)
    elif player_choice == "q":
        print(quit_message)
        break
