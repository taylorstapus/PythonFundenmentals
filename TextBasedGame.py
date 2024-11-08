#  Taylor Stapus

# functions for '-' printed 30 times
def blank_lines():
    print('-' * 40)


# introduction of the game stating rules and command possibilities
intro = 'Welcome to THE FINAL COUNTDOWN!'
intro2 = 'Your goal is to move between the rooms,\n'\
            'pick up all 6 items, and use those items \n'\
            'to defeat THE FINALS in the Classroom.'
intro3 = 'Remember, you cannot enter the Classroom \n'\
            'until you have picked up all the items.'
intro4 = 'The commands you can use to move are: \n'\
            'go North, go South, go West and go East '
intro5 = 'To pick up the items type: \n'\
            'get (items name)'
intro6 = 'Good luck!'
print(intro)
blank_lines()
print(intro2)
blank_lines()
print(intro3)
blank_lines()
print(intro4)
blank_lines()
print(intro5)
blank_lines()
print(intro6)
blank_lines()

# dictionary for rooms and directions
rooms = {
    'Courtyard': {'go South': 'Gymnasium', 'go North': 'Library', 'go West': 'Study Hall', 'go East': 'Cafeteria'},
    'Gymnasium': {'go East': 'Auditorium', 'go North': 'Courtyard'},
    'Auditorium': {'go West': 'Gymnasium'},
    'Study Hall': {'go North': 'Deans Office', 'go East': 'Courtyard'},
    'Deans Office': {'go South': 'Study Hall'},
    'Cafeteria': {'go West': 'Courtyard'},
    'Library': {'go South': 'Courtyard', 'go East': 'Classroom'},
}

# dictionary for items in particular rooms
items_in_rooms = {
    'Gymnasium': 'Braincell',
    'Auditorium': 'Cat',
    'Study Hall': 'Note',
    'Deans Office': 'Pencil',
    'Cafeteria': 'Coffee',
    'Library': 'Book',
}

inventory = []


# function created to show the players current location and use'-' to break up text
def location():
    print('-' * 40)
    print('You are in the {}'.format(current_room))


# function for inventory
def print_inventory():
    print('Inventory:', inventory)


# function for showing items in room
def show_items(room):
    rooms_with_items = items_in_rooms.keys()
    if current_room in rooms_with_items:
        print('You see a', items_in_rooms[room])


# function created to navigate through rooms with what the player inputs
def navigate(room, direction):
    if direction in rooms[room]:
        last_room = rooms[room]
        new_room = last_room[direction]
        return new_room
    else:
        print('That is not a valid direction. Try again!')
        return room


# pick up item function
def pickup_item(item, room):
    item = item[4:]
    if room in items_in_rooms.keys() and item in items_in_rooms[room]:
        inventory.append(item)
        items_in_rooms.pop(room)
        print('You have retrieved the', item)
    else:
        print('Invalid move! Try again.')


# start player in Great Hall
current_room = 'Courtyard'

player_move = ''

# starts loop if player input is not 'Classroom'
while current_room != 'Classroom':
    location()
    print_inventory()
    show_items(current_room)
    print('-' * 40)
    player_move = input('What would like to do?:\n')

    if player_move[0:2] == 'go':
        current_room = navigate(current_room, player_move)
    elif player_move[0:3] == 'get':
        pickup_item(player_move, current_room)
    else:
        print('Invalid move! Try again')

if len(inventory) == 6:
    print('Congrats! You have defeated THE FINALS! Thank you for playing')
else:
    print('OH NO! You did not have all the items to defeat THE FINALS. GAME OVER.')
