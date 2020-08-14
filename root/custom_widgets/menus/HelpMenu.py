from tkinter import Menu
from tkinter.ttk import Menubutton


class HelpMenu(Menu):
    def __init__(self, mb, *args, **kwargs):
        super().__init__(mb, *args, **kwargs)
        self.add_command(label="Manual", command=self.show_manual)

    def show_manual(self):
        print("MANUAL")
        # TODO: display the docs


class HelpMenuButton(Menubutton):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, direction='below', text='Help', *args, **kwargs)
        self.config(menu=HelpMenu(self))
