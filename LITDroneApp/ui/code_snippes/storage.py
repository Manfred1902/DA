class Content(MDBoxLayout):
    def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.orientation = 'vertical'
    self.add_widget(
        MDLabel(
            text="This is a label inside the content",
            halign="center",
        )
    )

def on_start(self):
    for i in range(10):
        self.root.ids.box.add_widget(
            MDExpansionPanel(
                content=Content(),
                panel_cls=MDExpansionPanelThreeLine(
                    text="Text",
                    secondary_text="Secondary text",
                    tertiary_text="Tertiary text",
                )
            )
        )