
class GravityFlip:
    def __init__(self):
        self.gravity_state = "down" 

    def toggle_gravity(self):
        if self.gravity_state == "down":
            self.gravity_state = "up"
        else:
            self.gravity_state = "down"
        return self.gravity_state

    def apply_gravity(self, position):
        if self.gravity_state == "down":
            position["y"] += 1
        else:
            position["y"] -= 1
        return position
