""" Make decision on video
This is an Kivy App running a video file. Contains class MyApp and MyGrid.
Properties are defined in Kivy language file my.kv.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    """
    Creating an object that will define the appearance and functions of the application

    """

    video = ObjectProperty(None)

    def press_pause(self):
        """
        Method that pauses the video
        """

        self.video.state='pause'

    def press_play(self):
        """
        Method that turns on the video
        """

        self.video.state='play'


class MyApp(App):
    """
    Class that builds the application
    """

    def build(self):
        return MyGrid()


if __name__ == '__main__':

    MyApp().run()
