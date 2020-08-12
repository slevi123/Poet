from tkinter import ttk

from root.custom_widgets.TextEditor import TextEditorFrame


class MainWindow(ttk.Frame):  # TODO: use ttk.PanedWindow
    # NOTE: self.add() to register widgets
    # TODO: add notebook, support for multiple files
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.root = parent

        # self.add(
        #     ttk.Sizegrip(self)
        # )

        # self.add(
        text_editor = TextEditorFrame(self, height=300).pack(expand=True, fill='both')

        # )
