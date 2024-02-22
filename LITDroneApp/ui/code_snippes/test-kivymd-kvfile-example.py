from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('test-kvfile-example.kv')
    
    def on_start(self):
        panel1 = MDExpansionPanel(
            icon="language-python", 
            panel_cls=MDExpansionPanelOneLine(text="Python"), 
            content=MDLabel(text="This is Python!", size_hint_y=None)
        )
        panel2 = MDExpansionPanel(
            icon="language-java", 
            panel_cls=MDExpansionPanelOneLine(text="Java"), 
            content=MDLabel(text="This is Java.", size_hint_y=None)
        )
        self.root.ids.list_box.add_widget(panel1)
        self.root.ids.list_box.add_widget(panel2)

MainApp().run()