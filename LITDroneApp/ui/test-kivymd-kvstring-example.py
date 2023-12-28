from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.label import MDLabel

KV = """
MDScreenManager:
    id: sm
    MDScreen:
        id: screen
        MDBoxLayout:
            id: box
            orientation: "vertical"
            spacing: 10
            padding: 10
            MDTopAppBar:
                title: "My App"
"""

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def on_start(self):
        panel1 = MDExpansionPanel(
            icon="language-python", 
            panel_cls=MDExpansionPanelOneLine(text="Python"), 
            content=MDLabel(text="This is Python!")
        )
        panel2 = MDExpansionPanel(
            icon="language-java", 
            panel_cls=MDExpansionPanelOneLine(text="Java"), 
            content=MDLabel(text="This is Java.")
        )
        self.root.ids.box.add_widget(panel1)
        self.root.ids.box.add_widget(panel2)

MainApp().run()