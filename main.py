from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label

Builder.load_file('design.kv')

class RootWidget(BoxLayout):
    pass


class TutorialApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    TutorialApp().run()