from kivy.lang import Builder
from kivymd.app import MDApp
 
KV = """
MDBoxLayout:
    orientation: 'vertical'
    padding: '10dp'
    
    MDScrollView:
        MDList:
            spacing: '10dp'
            # Add 10 MDCards
            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: '150dp'
                radius: 10
                MDLabel:
                    text: "Card 1 Content"
                    theme_text_color: 'Secondary'
        
            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: '150dp'
                radius: 10
                MDLabel:
                    text: "Card 2 Content"
                    md_bg_color: (1, 1, 0.5, 0.6)
            
            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: '150dp'
                radius: 10
                elevation: 10
                MDLabel:
                    text: "Card 2 Content"
                    theme_text_color: 'Secondary'
                        
            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: '150dp'
                radius: 10
                elevation: 10
                MDLabel:
                    text: "Card 2 Content"
                    theme_text_color: 'Secondary'
                        
            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: '150dp'
                radius: 10
                elevation: 10
                MDLabel:
                    text: "Card 2 Content"
                    theme_text_color: 'Secondary'
                        
            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: '150dp'
                radius: 10
                elevation: 10
                MDLabel:
                    text: "Card 2 Content"
                    theme_text_color: 'Secondary'
                        
            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: '150dp'
                radius: 10
                elevation: 10
                MDLabel:
                    text: "Card 2 Content"
                    theme_text_color: 'Secondary'
                        
            MDCard:
                orientation: 'vertical'
                size_hint_y: None
                height: '150dp'
                radius: 10
                elevation: 10
                MDLabel:
                    text: "Card 2 Content"
                    theme_text_color: 'Secondary'
 
    # Repeat similar structure for Cards 3 to 10
 
    # Example for Card 3:
    # MDCard:
    #     orientation: 'vertical'
    #     size_hint_y: None
    #     height: '150dp'
    #     radius: 10
    #     elevation: 10
    #     MDLabel:
    #         text: "Card 3 Content"
    #         theme_text_color: 'Secondary'
 
    # ... Repeat for Cards 4 to 10 ...
 
    # End of MDCards
"""
 
class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
 
if __name__ == '__main__':
    MyApp().run()