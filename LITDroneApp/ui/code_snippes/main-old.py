from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


KV = '''
<LoginScreen>:


    MDBoxLayout:
        MDNavigationDrawer:
            MDNavigationRailMenuButton:
                on_release:

            MDNavigationRailFabButton:
                md_bg_color: "#b0f0d6"
                icon: "home"

            MDNavigationRailItem:
                text: "login"
                icon: "login"

        MDIconButton:
            icon: "backspace"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_press: root.manager.current = 'menu'

<MenuScreen>:
    MDBoxLayout:
        MDNavigationRail:
            MDNavigationRailMenuButton:
                on_release:

            MDNavigationRailFabButton:
                md_bg_color: "#b0f0d6"
                icon: "home"

            MDNavigationRailItem:
                text: "Git"
                icon: "git"

        MDIconButton:
            icon: "cogs"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_press: root.manager.current = 'settings'

<SettingsScreen>:
    MDBoxLayout:
        MDNavigationRail:
            MDNavigationRailMenuButton:
                on_release:

            MDNavigationRailFabButton:
                md_bg_color: "#b0f0d6"
                icon: "home"

            MDNavigationRailItem:
                text: "login"
                icon: "login"

        MDIconButton:
            icon: "backspace"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_press: root.manager.current = 'menu'
'''
class LoginScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        Builder.load_string(KV)

        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm


MainApp().run()