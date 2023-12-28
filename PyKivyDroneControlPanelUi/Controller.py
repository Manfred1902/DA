from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.widget import Widget


Builder.load_file('controller.kv')


class RootWidget(Widget):
    pass


class LitApp(App):
    def build(self):
        test = RootWidget()
        return test


if __name__ == '__main__':
    LitApp().run()
