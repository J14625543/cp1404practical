from kivy.app import App
from kivy.lang import Builder


class LayoutExampleApp(App):
    """Example Kivy app showcasing BoxLayout and user input."""

    def build(self):
        """Initialize the app and load the UI from KV file."""
        self.title = "BoxLayout Example"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def greet_user(self):
        """Generate and print a greeting based on user input."""
        input_field = self.root.ids.name_input
        user_name = input_field.text.strip()
        if user_name:
            message = f"Hello, {user_name}!"
            print(message)


