from tkinter.ttk import PanedWindow

from root.custom_widgets.ChangeEventText import ChangeEventText
from root.custom_widgets.EditorExtensions import EditorLineNumbers, SyllableCounter


class TextEditorFrame(PanedWindow):  # TODO: maybe use ttk.PanedWindow
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, orient='horizontal', *args, **kwargs)
        self.editor = ChangeEventText(self)
        self.syllable_counter = SyllableCounter(self, self.editor)
        self.line_number = EditorLineNumbers(self, self.editor)

        self.add(self.line_number, weight=2)
        self.add(self.editor, weight=91)
        self.add(self.syllable_counter, weight=5)
        # self.line_number.grid(row=0, column=1, sticky='ns')
        # self.editor.grid(row=0, column=2, sticky='nsew')
        # self.syllable_counter.grid(row=0, column=3, sticky='nsew')
        # self.syllable_indicator = tk.
        # tk.Button(text='TEST', command=self.redraw_linenums).pack()

        self.resize()

    def resize(self):

        height = self.winfo_reqheight()
        width = self.winfo_reqwidth()
        # self.editor.config(height=height)
        self.syllable_counter.config(width=30)
        self.line_number.config(width=40)

    def test(self):
        i = 1
        while True:
            start = self.editor.index(f"{i}.0")
            if self.editor.dlineinfo(start) is not None:
                end = self.editor.index(f"{i}.end")
                i += 1
                print(end.split('.')[1])
                print(self.editor.get(start, end))
            else:
                break
