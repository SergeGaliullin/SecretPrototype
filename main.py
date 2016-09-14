from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

Builder.load_file('design.kv')


class TutorialApp(App):
    def build(self):
        return Label(text='H')


if __name__ == "__main__":
    TutorialApp().run()