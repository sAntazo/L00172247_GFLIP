class GravityLogger:
    """
    A utility class to log gravity flip actions to a file.

    Methods:
        log_event(event): Logs a gravity-related event.
    """

    @staticmethod
    def log_event(event):
        """
        Logs a gravity-related event to a file.

        Args:
            event (str): The event description.
        """
        with open("gravity_log.txt", "a") as log_file:
            log_file.write(f"{event}\n")
