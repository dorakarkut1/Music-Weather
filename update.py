from functools import partial

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


tree = {
    '0':   ['Hi!', 'A', 'B'],
    'A':   ['Yes', 'AA', 'AB','AC'],
    'AA':  ['Seneca', 'AAA', 'AAB'],
    'AAA': ['Yes', 'AAA', 'AAB'],
    'AAB': ['No', 'AAA', 'AAB'],
    'AB':  ['Cato', "AA", "AB"],
    'AC':  ['Neither'],
    'B':   ["No",'BA','BB'],
    'BA':  ['xx'],
    'BB':  ['xxx']
}


class RootWidget(FloatLayout):
    current_node = '0'

    def __init__(self, **kwargs):
        super(FloatLayout, self).__init__(**kwargs)
        self._rebuild()

    def update_node(self, i, *args):
        self.current_node = i
        self._rebuild()

    def _rebuild(self, *args):
        self.clear_widgets()  # clear current buttons

        child_nodes = tree[self.current_node][1:]
        j = len(child_nodes)
        # Answer Buttons
        for i in child_nodes:
            answer_button = Button(
                pos=(100, j*75),
                size_hint=(0.8, 0.1),
                text=tree[i][0],
            )
            answer_button.bind(
                on_release=partial(self.update_node, i)
            )
            j -= 1
            print(i)
            self.add_widget(answer_button)


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()