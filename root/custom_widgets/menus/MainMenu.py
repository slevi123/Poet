from tkinter import Frame

from root.custom_widgets.menus.FileMenu import FileMenuButton
from root.custom_widgets.menus.HelpMenu import HelpMenuButton
from root.custom_widgets.menus.LookMenu import LookMenuButton


class MainMenu(Frame):  # TODO: modify this
    def __init__(self, parent, tab_handler, *args, **kwargs):
        self.parent = parent
        super().__init__(parent, *args, **kwargs)
        FileMenuButton(self, tab_handler).pack(side='left')
        LookMenuButton(self).pack(side='left')
        HelpMenuButton(self).pack(side='left')
