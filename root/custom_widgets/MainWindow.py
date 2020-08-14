from tkinter import ttk

from root.custom_widgets.TabHandler import TabHandler
from root.custom_widgets.menus.MainMenu import MainMenu


class MainWindow(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.root = parent

        # self.add(
        #     ttk.Sizegrip(self)
        # )
        tab_handler = TabHandler(self)
        MainMenu(self, tab_handler).pack(side='top', fill='x', pady=(0, 10))
        tab_handler.pack(side='bottom', expand=True, fill='both')
