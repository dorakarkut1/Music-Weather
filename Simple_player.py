import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
 

# An App running a video file

class MyVideoApp(App):
    def build(self):
        video = Video(source='spring.mp4')
        video.state='play'
        video.options = {'eos': 'loop'}
        video.allow_stretch=True
        return video
    


# Start the Video App

if __name__ == '__main__':
    MyVideoApp().run()