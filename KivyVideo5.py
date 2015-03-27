from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.widget import Widget



class Widgets(Widget):
    pass


class SimpleKivy3(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    SimpleKivy3().run()
        
    

