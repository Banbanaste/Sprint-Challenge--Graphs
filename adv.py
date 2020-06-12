from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def dft(direction):
    while player.travel(direction) is not str(player.travel(direction)):
        print(direction)
        traversal_path.append(direction)
        player.travel(direction)
    traversal_path.append(player.backtrack)


def bft(starting_vertex, traversal_path):
    # Create an empty queue and enqueue the starting vertex ID
    q = Queue()

    # Create a Set to store visited vertices
    visited = {}
    world_map = {}

    q.enqueue([starting_vertex.id])

    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first vertex
        path = q.dequeue()

        v = world.rooms[path[-1]]

        player.backtrack = []

        # If that vertex has not been visited...
        if v.id not in visited:
            # Visit it
            visited[v.id] = path
            world_map[v.id] = {}

            # Then add all of its neighbors to the back of the queue
            for direction in v.get_exits():
                print(direction)
                # dft(direction)
                if player.travel(direction) is not str(player.travel(direction)):
                    traversal_path.append(direction)
                else:
                    traversal_path.append(player.backtrack)
                    player.backtrack = []

                q.enqueue(path + [v.get_room_in_direction(direction).id])
                world_map[v.id][direction] = v.get_room_in_direction(
                    direction).id
    print(visited)
    print(world_map)
    print(traversal_path)

    """ for i in visited:
        if len(visited[i]) > 1:
            backtrack = []
            map_ref = visited[i].pop(0)
            # print(visited[i])
            for j in visited[i]:
                # print("map_ref: ", map_ref)
                # print(j)
                direction = world_map[map_ref][j]
                back_dir = world_map[j][map_ref]
                # print("direction: ", direction)
                # print("back_dir: ", back_dir)
                traversal_path.append(direction)
                backtrack.insert(0, back_dir)
                # print("last j:", visited[i][-1])
                if j == visited[i][-1]:
                    traversal_path += backtrack
                else:
                    map_ref = j
    # print(traversal_path)
    return traversal_path """


bft(player.current_room, traversal_path)


# TRAVERSAL TEST - DO NOT MODIFY
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


# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
