import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty

# An App running a video file

class MyGrid(Widget):
    video = ObjectProperty(None)
    def press_pause(self):
        self.video.state='pause'
    def press_play(self):
        self.video.state='play'
        

class MyApp(App):

    def build(self):
        return MyGrid()
    


# Start the Video App

if __name__ == '__main__':
    
    MyApp().run()