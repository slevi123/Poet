from itertools import count
from pathlib import Path
from tkinter import Menu
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.ttk import Menubutton

from root.custom_widgets.text_editor.TextEditor import TextEditorFrame


class FileMenu(Menu):
    new_tab_id = count()

    def __init__(self, mb, tab_handler, *args, **kwargs):
        super().__init__(mb, *args, **kwargs)
        self.tab_handler = tab_handler
        self.add_command(label="New", command=self._on_new)
        self.add_command(label="Open", command=self._on_open)
        self.add_command(label="Open Recent")  # TODO: implement this
        self.add_command(label="Save", command=self._on_save)
        self.add_command(label="Save as", command=self._on_save_as)
        self.add_command(label="Close", command=self._on_close)

    def get_current_tab(self):
        current_tab_name = self.tab_handler.select()
        current_tab = self.tab_handler.nametowidget(current_tab_name)
        return current_tab

    def _on_new(self):
        new_id = next(FileMenu.new_tab_id)
        self.tab_handler.add(child := TextEditorFrame(self.tab_handler), text=f"new_file_{new_id}.txt")
        self.tab_handler.select(child)

    def _on_save(self):
        file_handler = self.get_current_tab().file_handler
        # TODO: move to path property
        if file_handler.path is None:
            file_handler.path = Path(asked := asksaveasfilename()).resolve()
            if asked:
                self.tab_handler.tab(self.get_current_tab(), text=file_handler.path.name)
                file_handler.save()
        else:
            file_handler.save()

    def _on_save_as(self):
        file_handler = self.get_current_tab().file_handler
        file_handler.path = Path(asked := asksaveasfilename()).resolve()
        if asked:
            self.tab_handler.tab(self.get_current_tab(), text=file_handler.path.name)
            file_handler.save()

    def _on_open(self):
        path = Path(asked := askopenfilename()).resolve()
        if asked:
            self.tab_handler.add(child := TextEditorFrame(self.tab_handler, path=path), text=path.name)
            self.tab_handler.select(child)

    def _on_close(self):
        current_tab = self.get_current_tab()
        current_tab.file_handler.close()
        self.tab_handler.forget(current_tab)


class FileMenuButton(Menubutton):
    def __init__(self, parent, tab_handler, *args, **kwargs):
        super().__init__(parent, direction='below', text='File', *args, **kwargs)
        self.config(menu=FileMenu(self, tab_handler))
