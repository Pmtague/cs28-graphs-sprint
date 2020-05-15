from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

''' Here's my code '''

# Use DFT to move through the graph from current room
def traversal(player, prev_direction = None, visited = None):

    # Keep track of visited rooms
    visited = set()

    # Add starting room to visited
    visited.add(player.current_room.id)
    print("Visited", visited)

    # Get starting room exits
    exits = player.current_room.get_exits()
    print("Exits", exits)

    # Take the first exit in the list
    if prev_direction is None:
        player.travel(exits[0], show_rooms = False)
        prev_direction = exits[0]
        reverse_direction = reverse[prev_direction]
        print("Prev_Direction_2", prev_direction)

    # If prev_direction is not None, take the next exit that is not the prev_direction and not the opposite of the previous direction
    else:
        # Take the first exit that is not the reverse_direction or the previous direction
        for exit in exits:
            available_exits = []
            if exit != prev_direction and exit != reverse_direction():
                available_exits.append(exit)
                traversal(exit)
            else:
                
            


    # Check for previous direction in current room exits
    if prev_direction in exits:
        print("Prev_Direction", prev_direction)
        player.travel(prev_direction, show_rooms = False)
    
    else:    
        # Take the first exit in Exits
        player.travel(exits[0], show_rooms = False)
        prev_direction = exits[0]
        print("Prev_Direction_2", prev_direction)

    # Update direction values for the prev room and the current room from ? to room numbers



    # Save direction moved to traversal_path
    traversal_path.append(exits[0])
    print("Traversal_Path", traversal_path)

    for next_direction in player.current_room.get_exits():
        
        # If 
        if next_direction not in visited:

            traversal(next_direction, visited)

traversal(player)

        # Get new current room
        # Mark new room visited
        
            # 
        # Get current room unexplored exits
        # If there is an unexplored exit (room.n_to = None) in the same direction as the last direction moved, move that direction
        # Otherwise, if len of Exits is greater than 0, take the first exit in Exits
        # Otherwise, use BFS to find the nearest room with unexplored exits

# Helper function to use BFS to find the nearest unexplored path


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
