from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETERS = 1.60934


class DistanceConverterApp(App):
    """A Kivy App for converting miles into kilometers."""

    def build(self):
        """Initialize the application window and load the interface."""
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

