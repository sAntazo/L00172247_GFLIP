class GravFlip:
    def __init__(self, direction="up"):
        self.direction = direction

    def toggle_gravity(self):
        if self.direction == "up":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "up"
        else:
            raise ValueError("Invalid direction")
        return self.direction

    def apply_gravity(self, object_position):
        if self.direction == "up":
            object_position["y"] += 1
        elif self.direction == "down":
            object_position["y"] -= 1
        return object_position
