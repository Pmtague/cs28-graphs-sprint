from room import Room
from player import Player
from world import World
from util import Queue, Stack

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
        # print("Rooms", room_graph[room][1])

# Assign a current room variable
# current_room = player.current_room.id


# Use DFT to move through the graph from current room

# def traversal(current_room = player.current_room.id, visited = None):

#     # Initialize an empty set for visited rooms
#     if visited is None:
#         visited = set()
 
#     # Add the current room to visited
#     visited.add(current_room)
#     print(visited)

#     # Assign a variable for the exits list
#     exits = player.current_room.get_exits()

#     # Loop through the unexplored exits
#     for exit in exits:
#         print("Exits", exit)
#         # If the exit is unexplored
#         if visited[-1][1][exit][1] == "?":

#             # Run the entire function on the next_vert
#             traversal(room_graph[player.current_room.id][1][exit][0], visited)
        
#     if exits == None:
#         pass


# Spawn in starting room
def traversal(current_room, room_graph, traversal_path):

    print("Current Room", current_room)

    # Instantiate an empty stack
    s = Stack()

    # Push the current room id onto the stack
    s.push(current_room.id)

    # Mark the current room as visited
    visited = set()

    # While the stack is not empty
    while s.size() > 0:

        # Pop first room
        room = s.pop()

        # If room is not visited:
        if room not in visited:
            visited.add(current_room.id)
            print("Visited", visited)

            # Find the available exits in the current room
            exits = current_room.get_exits()
            print("Exits", exits)

            # Determine which of the available exits are unexplored
            unexplored_exits = []
            unexplored_rooms = []

            for exit in exits:
                if room_graph[current_room.id][1][exit][1]:
                    unexplored_exits.append(exit)
                    unexplored_rooms.append(room_graph[current_room.id][1][exit][0])
                    print("Unexplored Rooms", unexplored_rooms)
                    
            # Add the rooms in the unexplored directions to the stack
            for new_room in unexplored_rooms:
                random_room = random.choice(unexplored_rooms)
                if random_room not in unexplored_rooms:
                    s.push(random_room)
                    print("Random", s)

            # # Update the current room to the unvisited room in the random direction
            # current_room.id = room_graph[current_room.id][1][random_direction][0]
            # print("Current Room", current_room)

            # # Add the direction moved to the traversal path
            # new_traversal_path = traversal_path.copy()
            # new_traversal_path.append(random_direction)
            # print("Traversal Path", new_traversal_path)

            # # Mark the exit as explored
            # room_graph[current_room.id][1][random_direction][1] = None

            # If there are unexplored exits, repeat from choosing one of the available exits at random

        # If there are not unexplored exits, move back a room and check for unexplored exits

        # Continue backward until you find the closest room with unexplored exits

        # Start again from choosing one of the available exits at random

        # When rooms visited = 500, you're done


traversal(player.current_room, room_graph, traversal_path)

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
