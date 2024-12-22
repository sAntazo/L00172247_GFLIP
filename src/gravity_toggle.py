import time

class ScheduledGravityFlip(GravityFlip):
    """
    A class to extend GravityFlip with a scheduled gravity toggle.

    Methods:
        schedule_gravity_inversion(duration): Schedules gravity inversion after a set duration.
    """

    def schedule_gravity_inversion(self, duration):
        """
        Schedules gravity inversion after a set duration.

        Args:
            duration (int): The number of seconds before toggling gravity.
        """
        time.sleep(duration)
        self.toggle_gravity()
