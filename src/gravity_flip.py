class GravityFlip:
    """
    A class to manage gravity flipping functionality.

    Attributes:
        gravity_state (str): The current state of gravity ("up" or "down").
    """

    def __init__(self):
        """
        Initializes the GravityFlip class with the default gravity state as 'down'.
        """
        self.gravity_state = "down"

    def toggle_gravity(self):
        """
        Toggles the gravity state between "up" and "down".

        Returns:
            str: The new gravity state.
        """
        if self.gravity_state == "down":
            self.gravity_state = "up"
        else:
            self.gravity_state = "down"
        return self.gravity_state

    def apply_gravity(self, position):
        """
        Applies the gravity effect to a given position.

        Args:
            position (dict): A dictionary containing the "y" coordinate.

        Returns:
            dict: The updated position after applying gravity.
        """
        if self.gravity_state == "down":
            position["y"] += 1
        else:
            position["y"] -= 1
        return position
