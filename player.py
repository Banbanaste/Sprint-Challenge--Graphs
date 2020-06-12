class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.backtrack = []

    def travel(self, direction, show_rooms=False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if direction is "n":
                self.backtrack.insert(0, "s")
            if direction is "s":
                self.backtrack.insert(0, "n")
            if direction is "e":
                self.backtrack.insert(0, "w")
            if direction is "w":
                self.backtrack.insert(0, "e")

            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")
