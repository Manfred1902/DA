from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButtonSpeedDial

kvstring = '''
<DroneController>:
    orientation: 'vertical'

    MDLabel:
        text: 'Drone Controller'
        halign: 'center'
        fontstyle: 'H5'

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotationrootbutton: True
'''


class DroneController(BoxLayout):
    pass


class DroneControllerApp(MDApp):
    data = {
        'ArrowUp': 'Move Forward',
        'ArrowDown': 'Move Backward',
        'ArrowLeft': 'Move Left',
        'ArrowRight': 'Move Right',
        'Camera': 'Toggle Camera',
        'Power': 'Power Off'
    }

    def build(self):
        return DroneController()


if __name__ == '__main__':
    # Load KV string
    Builder.load_string(kvstring)
    # Run DroneControllerApp
    DroneControllerApp().run()