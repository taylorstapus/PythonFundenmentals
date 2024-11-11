# Taylor Stapus

# start of the game explaining rules and commands
intro = 'Welcome to The Simplified Dragon Text Game!\n' \
        'Your goal is to move between the rooms.\n' \
        'The commands you can use are: North, South, West and East\n' \
        'To leave the game enter: Exit\n' \
        'Good luck!'
print(intro)

# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
}


# function created to show the players current location and use'-' to break up text
def location():
    print('-' * 30)  # dashes used for formatting aesthetic purposes
    print('You are in the {}'.format(current_room))  # prints whatever current room is throughout the game


# function created to navigate through rooms with what the player inputs
def navigate(room, direction):   # Function name with room and directions as the parameters
    if direction in rooms[room]:  # Checking if the direction is one of the keys of the (rooms) dictionary
        last_room = rooms[room]  # Getting particular room from the (rooms) definitions and assigning it to a variable
        new_room = last_room[direction]  # Gets the directions associated in (last_room) to create variable for the new room in which those directions lead
        return new_room  # ends execution of current function and returns new value to the calling function
    elif direction == 'Exit':   # What happens if the player's input is 'Exit'
        print('You have left the game! Thank you for playing!')
        return room  # game ends here because there is no more calling function
    else:
        print('That is not a valid direction. Try again!')  # What is printed if the input does not match direction
        return room  # ends execution of current function and returns old value to the calling function


# start player in Great Hall
current_room = 'Great Hall'  # sets location

player_move = ''  # awaits player's input

# starts loop if player input is not 'Exit'
while player_move != 'Exit':  # when the player's input is not Exit
    location()     # calls location function
    player_move = input('Where would you like to go?:\n')  # Inquired player to input something
    current_room = navigate(current_room, player_move)   # Changes current room to what the output is after the input goes through the navigation function
