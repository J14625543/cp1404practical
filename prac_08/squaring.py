from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class NumberSquaringApp(App):
    """A simple Kivy app to compute the square of a number."""

    def build(self):
        """Configure the app window and load the interface layout."""
        Window.size = (220, 120)
        self.title = "Number Squarer"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def calculate_square(self, input_value):
        """Square the given input and show the result on screen."""
        try:
            squared_value = pow(int(input_value), 2)
            self.root.ids.result_label.text = str(squared_value)
        except (ValueError, TypeError):
            self.root.ids.result_label.text = ""



