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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


def go_back(direction):
    if direction is 'n':
        return 's'
    elif direction is 's':
        return 'n'
    elif direction is 'e':
        return 'w'
    elif direction is 'w':
        return 'e'
    return


def maze_traversal():

    traversal_path = []
    visited = {}
    reverse_path = []

    visited[player.current_room.id] = player.current_room.get_exits()
    # print("VISITED:", visited)
    world_measure = len(room_graph) - 1

    while len(visited) < world_measure:
        if player.current_room.id not in visited:
            visited[player.current_room.id] = player.current_room.get_exits()
            # print("VISITED2:", visited)
            # print("REVERSED:", reverse)
            visited[player.current_room.id].remove(reverse_path[-1])
        while len(visited[player.current_room.id]) == 0:
            re_path = reverse_path.pop()
            traversal_path.append(re_path)
            player.travel(re_path)
            # print("VISITED3:", visited)
            # print("REVERSED2:", reverse)
            print("TRAVEL:", traversal_path)

        move = visited[player.current_room.id].pop(0)
        traversal_path.append(move)
        new_move = go_back(move)
        reverse_path.append(new_move)
        player.travel(move)

    return traversal_path


traversal_path = maze_traversal()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# this is my first commit
