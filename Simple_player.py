import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from decision import decision_maker 
from kivy.core.window import Window

# An App running a video file

class MyGrid(GridLayout):
    def __init__(self,name,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.rows=2
        self.inside = GridLayout(cols=2, row_force_default=True, row_default_height=int(Window.height)/8.9)
        play = Button(text="PLAY", background_color=[0,0,0,1],size_hint_y=None, height=int(Window.height)/8.9)
        pause = Button(text="PAUSE", background_color=[0,0,0,1],size_hint_y=None, height=int(Window.height)/8.9)
        self.inside.add_widget(play)
        self.inside.add_widget(pause)
        video = Video(source=name)
        video.state='play'
        video.options = {'eos': 'loop'}
        video.allow_stretch=True
        self.add_widget(video)
        self.add_widget(self.inside)
        

class MyVideoApp(App):

    def build(self):
        name = decision_maker()
        return MyGrid(name)
    


# Start the Video App

if __name__ == '__main__':
    
    MyVideoApp().run()