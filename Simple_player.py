import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from decision import decision_maker 

# An App running a video file

class MyVideoApp(App):

    name = decision_maker()
    def build(self):
        f = GridLayout(rows=2)
        b = Button(text="Play")
        video = Video(source=self.name)
        video.state='play'
        video.options = {'eos': 'loop'}
        video.allow_stretch=True

        f.add_widget(video)
        f.add_widget(b)

        return f
    


# Start the Video App

if __name__ == '__main__':
    
    MyVideoApp().run()