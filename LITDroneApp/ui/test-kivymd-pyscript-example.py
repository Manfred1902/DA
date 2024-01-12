from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
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

MainApp().run()