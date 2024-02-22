import time, asyncio

num = 0




def giveNumOne(number):
    num = number

    while(num == 1):
        print("Hier die Nummer 1")
        time.sleep(2)



MDTopAppBar:
            title: "MDTopAppBar"
            left_action_items: [["menu", "This is the navigation"]]
            pos_hint: {"top": 1, "right": 1}
            right_action_items:
                [["dots-vertical", lambda x: app.controller_screen("controller_screen"), "Switch to Controller"]]
            left_action_items:



ScrollView:
            MDList:
                id: md_list
                MDExpansionPanel:
                    icon: "android"
                    panel_cls: MDExpansionPanelTwoLine(text="Panel 1", secondary_text="Secondary text line")
                    content:
                        MDTextField:
                            id: text_input1
                            hint_text: "Enter text here"
                        MDFillRoundFlatButton:
                            text: "start1"
                            on_press: app.start1(text_input1.text)
                MDExpansionPanel:
                    icon: "apple"
                    panel_cls: MDExpansionPanelTwoLine(text="Panel 2", secondary_text="Secondary text line")
                    content:
                        MDTextField:
                            id: text_input2
                            hint_text: "Enter text here"
                        MDFillRoundFlatButton:
                            text: "start2"
                            on_press: app.start2(text_input2.text)





def on_start():
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