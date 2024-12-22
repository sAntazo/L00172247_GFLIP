import json

class GravityExporter:
    """
    A utility class to export the gravity state to a JSON file.

    Methods:
        export_state(state): Exports the current gravity state to a JSON file.
    """

    @staticmethod
    def export_state(state):
        """
        Exports the current gravity state to a JSON file.

        Args:
            state (str): The current gravity state.
        """
        with open("gravity_state.json", "w") as json_file:
            json.dump({"gravity_state": state}, json_file)
