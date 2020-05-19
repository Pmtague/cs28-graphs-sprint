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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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

# Spawn in starting room

# print("Traversal Path", traversal_path)

# Create a dictionary to store room ids and unexplored directions as we travel
visited = {}

# Create a list to keep track of the current path we are on in case we need to backtrack
backtrack_path = [None]

# Create a dictionary to grab reverse directions
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# While the length of the visited rooms is less than the length of the room graph
while len(visited) < len(room_graph) - 1:

    # If current room is not visited:
    if player.current_room.id not in visited:

        # Add the current room to visited as the key and the list of available exits as the value
        visited[player.current_room.id] = player.current_room.get_exits()
        # print("Visited", visited)

        # Store the last direction in a variable
        last_direction = backtrack_path[-1]
        # print("Last Direction", last_direction)

        # Remove last direction from visited[0][1]
        if last_direction != None:
            visited[player.current_room.id].remove(last_direction)
            # print("Visited after remove", visited)
            # print("Length of available directions", len(visited[player.current_room.id]))

    # If we hit a dead end, backtrack until we find another unexplored path
    while len(visited[player.current_room.id]) < 1:

        # Remove the last direction from the backtrack path
        backtrack = backtrack_path.pop()

        # Add the last direction to the traversal path
        traversal_path.append(backtrack)

        # Move the player back
        current_room = player.travel(backtrack)

    # Take the first available exit
    direction = visited[player.current_room.id].pop(0)
    # print("Movement Direction", direction)

    # Add the random direction to the traversal list
    traversal_path.append(direction)
    # print("Traversal Path after move", traversal_path)

    # Track the opposite direction for backtracking
    backtrack_path.append(reverse[direction])
    # print("Backtrack path after move", backtrack_path)

    # Move player in selected direction
    player.travel(direction)

    # Update the current room
    current_room = player.current_room.id
    # print("Current room at end", current_room)



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
