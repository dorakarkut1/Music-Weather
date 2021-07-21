import kivy
from decision import decision_maker
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from kivy.uix.widget import Widget
from decision import decision_maker 
from kivy.core.window import Window

# An App running a video file

class MyGrid(Widget):
    pass
        

class MyApp(App):

    def build(self):
        return MyGrid()
    


# Start the Video App

if __name__ == '__main__':
    
    MyApp().run()