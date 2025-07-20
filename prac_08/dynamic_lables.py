from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NameListApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        return Builder.load_file('dynamic_labels.kv')

    def on_start(self):
        container = self.root.ids.main
        for user in self.user_names:
            new_label = Label(text=user)
            container.add_widget(new_label)


if __name__ == "__main__":
    NameListApp().run()
