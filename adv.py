from room import Room
from player import Player
from world import World
from util import Queue

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


''' Here's my code '''

# Mark all exits unexplored

for room in room_graph:
    for direction in room_graph[room][1]:
        room_graph[room][1][direction] = [room_graph[room][1][direction], "?"]
        print("Rooms", room_graph[room][1])

# Assign a current room variable
# current_room = player.current_room.id


# Use DFT to move through the graph from current room

def traversal(current_room = player.current_room.id, visited = None):

    # Initialize an empty set for visited rooms
    if visited is None:
        visited = set()
 
    # Add the current room to visited
    visited.add(current_room)
    print(visited)

    # Assign a variable for the exits list
    exits = player.current_room.get_exits()

    # Loop through the unexplored exits
    for exit in exits:
        print("Exits", exit)
        # If the exit is unexplored
        if visited[-1][1][exit][1] == "?":

            # Run the entire function on the next_vert
            traversal(room_graph[player.current_room.id][1][exit][0], visited)
        
    if exits == None:
        pass

traversal(player.current_room.id)

        # Get new current room
        # Mark new room visited
        
            # 
        # Get current room unexplored exits
        # If there is an unexplored exit (room.n_to = None) in the same direction as the last direction moved, move that direction
        # Otherwise, if len of Exits is greater than 0, take the first exit in Exits
        # Otherwise, use BFS to find the nearest room with unexplored exits

# Helper function to use BFS to find the nearest unexplored path

# def backtrack(curr_index = -1):

#     reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

#     # Store previous direction in a variable
#     prev_dir = reverse[traversal_path[curr_index]]

#     # Move back to previous room
#     player.travel(prev_dir)

#     # Add new move to the traversal path
#     traversal.append(prev_dir)

#     # Check for unexplored exits
#     exits = player.current_room.get_exits()

#     # If exits == None
#     if exits == None:
#         curr_index -= 2
#         backtrack(curr_index)
    
#     # If there are unexplored exits
#     else:
#         current_room = player.current_room
#         # traversal(current_room)

# backtrack(curr_index= -1)

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
