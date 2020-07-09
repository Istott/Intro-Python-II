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

def set_direction(player, direction):
    attribute = direction + '_to'

    if hasattr(player.location, attribute):
        player.location = getattr(player.location, attribute)
    else:
        print('oops.... the wall hurts when you hit it. try again')


player = Player('bob', room['outside'])
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

direction = input('what direction do you want to go: ')

while True:
    print('\n')
    print(f'Hello {player.name}, you are in {player.location}')


    first_char = input("\nfirst_char: ").strip().lower().split()
    first_first_char = first_char[0]
    first_char = first_first_char[0]

    if first_char == 'q':
        break

    if first_char == 'n':
        set_direction(player, first_char)
    elif first_char == 's':
        set_direction(player, first_char)
    elif first_char == 'e':
        set_direction(player, first_char)
    elif first_char == 'w':
        set_direction(player, first_char)
    else:
        print('oops wrong entry, try again')
