from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
class MyApp(App):
    def build(self):

        btn = Button(text = "This is button")
        txt  = Label(text = "This is Label")
        btn.on_press = test
        layout = BoxLayout
        layout.add_widget(txt)
        layout.add_widget(btn)
        
        
        return layout

def test():
    print("hello!")

app = MyApp()
app.run()