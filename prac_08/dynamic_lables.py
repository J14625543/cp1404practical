from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NameListApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_names = ["Alice", "Bob", "Charlie", "Diana"]

