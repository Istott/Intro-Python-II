from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance ",
        "North of you, the cave mount beckons", ['axe', 'sword']), 

    'foyer':    Room("Foyer. ", """Dim light filters in from the south. Dusty
passages run north and east.""", ['penny', 'flashlight']),

    'overlook': Room("Grand Overlook. ", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['umbrella', 'cane']),

    'narrow':   Room("Narrow Passage. ", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['vase', 'portrait']),

    'treasure': Room("Treasure Chamber. ", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['feather', 'string']),
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

player = Player('bob', room['outside'])
# item = Item(room.Room.Item)

def set_direction(player, direction):
    attribute = direction + '_to'

    if hasattr(player.location, attribute):
        player.location = getattr(player.location, attribute)
    else:
        print('\nYou`re not very smart are you?..... try again')


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
# possible_direction('n', 's', 'w', 'e')
welcome = input('Welcome to the haunted Mansion....press enter to start ')

while True:
    print('\n')
    print(f'Hello {player.name}, you are in the {player.location}')
    print('\nitems in this room: ')
    player.location.itemList()


    command = input("\nWhat would you like to do: ").strip().lower().split()
    first_char = command[0]
    command = first_char[0]

    if command == 'q':
        print('\nQuiters are for Losers!!!\n')
        break

    if command == 'n':
        set_direction(player, command)
    elif command == 's':
        set_direction(player, command)
    elif command == 'e':
        set_direction(player, command)
    elif command == 'w':
        set_direction(player, command)
    else:
        print('\nYou make no sense, try again')
