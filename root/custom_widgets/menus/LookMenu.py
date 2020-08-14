from tkinter import Menu
from tkinter.ttk import Menubutton


class LookMenu(Menu):
    def __init__(self, mb, *args, **kwargs):
        super().__init__(mb, *args, **kwargs)
        self.add_command(label="Preferences")


class LookMenuButton(Menubutton):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, direction='below', text='Look', *args, **kwargs)
        self.config(menu=LookMenu(self))
