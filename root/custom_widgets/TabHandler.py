from json import load
from tkinter.ttk import Notebook

from root.custom_widgets.text_editor.TextEditor import TextEditorFrame


class TabHandler(Notebook):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.enable_traversal()
        self.tabs = []
        self.settings = {}
        # self.
        self.add(TextEditorFrame(self), text='elso')
        self.add(TextEditorFrame(self, height=300), text='masodik')

    def load_saved_data(self):
        self.settings = load(open('data/starting_data.json'))

    def __del__(self):
        # self.save_data_for_later()
        super().__del__()

    # def save_data_for_later(self):
    #     dump( load( open('data/starting_data.json') )
