from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine, MDExpansionPanelThreeLine
from kivymd.uix.label import MDLabel

from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from kivy.core.window import Window

from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.screenmanager import MDScreenManager

from kivy.uix.button import Button
from kivy.input.motionevent import MotionEvent

from __init__ import giveNumOne

import asyncio


Window.clearcolor = 1,1,1,1 

class LoginScreen(Screen):
    pass

class MenuScreen(Screen):
    def on_start(self):
        sm = MDScreenManager()
        screen = MDScreen()
        box = MDBoxLayout(orientation="vertical", spacing=10, padding=10)
        toolbar = MDTopAppBar(title="My App")
        panel1 = MDExpansionPanel(
            icon="language-python", 
            panel_cls=MDExpansionPanelOneLine(text="Python"), 
            content=MDLabel(text="This is Python.")
        )
        panel2 = MDExpansionPanel(
            icon="language-java", 
            panel_cls=MDExpansionPanelOneLine(text="Java"), 
            content=MDLabel(text="This is Java.")
        )
        box.add_widget(toolbar)
        box.add_widget(panel1)
        box.add_widget(panel2)
        screen.add_widget(box)
        sm.add_widget(screen)
        return sm

class ControlScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(UpBtn(text='Active Button', on_press=self.on_press))

    def on_press(self, instance):
        print("Button is being pressed")

class SettingsScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        Builder.load_file('./kv_files/login.kv')
        


        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        

        sm = ScreenManager(transition = NoTransition())
        sm.add_widget(LoginScreen(name='screen_login'))
        sm.add_widget(MenuScreen(name='screen_menu'))
        sm.add_widget(SettingsScreen(name='screen_settings'))
        sm.add_widget(ControlScreen(name='screen_controls'))

        return sm



    def logger(self):
        
        self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
    #def clear(self):
	#	self.root.ids.welcome_label.text = "WELCOME"		
	#	self.root.ids.user.text = ""		
	#	self.root.ids.password.text = ""



class UpBtn(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 0, 0, 1]  # Change the background color to red
            giveNumOne(1) # <-- hier methode für input übergabe
            self.dispatch('on_press')
        return True

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]  # Change the background color back to white
            giveNumOne(0) # <-- hier methode für input übergabe
            self.dispatch('on_release')
        return True

MainApp().run()