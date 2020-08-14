from tkinter.ttk import PanedWindow

from root.custom_widgets.text_editor.ChangeEventText import ChangeEventText
from root.custom_widgets.text_editor.EditorExtensions import EditorLineNumbers, SyllableCounter
from root.services.FileHandler import FileHandler


class TextEditorFrame(PanedWindow):  # TODO: maybe use ttk.PanedWindow
    def __init__(self, parent, path=None, *args, **kwargs):
        super().__init__(parent, orient='horizontal', *args, **kwargs)

        self.editor = ChangeEventText(self)
        self.syllable_counter = SyllableCounter(self, self.editor)
        self.line_number = EditorLineNumbers(self, self.editor)

        self.file_handler = FileHandler(self.editor, path=path)

        self.add(self.line_number, weight=2)
        self.add(self.editor, weight=91)
        self.add(self.syllable_counter, weight=5)

        self.syllable_counter.config(width=30)
        self.line_number.config(width=40)
