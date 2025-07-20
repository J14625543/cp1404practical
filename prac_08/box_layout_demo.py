from kivy.app import App
from kivy.lang import Builder


class LayoutExampleApp(App):
    """Example Kivy app showcasing BoxLayout and user input."""

    def build(self):
        """Initialize the app and load the UI from KV file."""
        self.title = "BoxLayout Example"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

