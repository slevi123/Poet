from tkinter import Canvas


class EditorLineNumbers(Canvas):
    def __init__(self, parent, editor, *args, **kwargs):
        super().__init__(parent, bg='red', *args, **kwargs)
        self.editor = editor
        editor.bind("<<Change>>", self._on_change, add=True)
        editor.bind("<Configure>", self._on_change, add=True)

    def redraw_linenums(self):
        self.delete("all")
        x = self.winfo_width() // 2 - 5
        i = self.editor.index("@0,0")
        while True:
            dline = self.editor.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(x, y, anchor="n", text=linenum)
            i = self.editor.index("%s+1line" % i)

    def _on_change(self, event):
        self.redraw_linenums()


class SyllableCounter(EditorLineNumbers):
    def redraw_linenums(self):
        self.delete("all")
        x = self.winfo_width() // 2
        i = self.editor.index("@0,0")
        # print('kezdodik')
        while True:
            dline = self.editor.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]  # stores the height in pixels
            linenum = str(i).split(".")[0]
            text_from_line = self.editor.get(f"{linenum}.0", f"{linenum}.end")
            szotagszam = self.szotagszam(text_from_line)
            # print(i)
            self.create_text(x, y, anchor="nw", text=szotagszam)
            i = self.editor.index("%s+1line" % i)

    @staticmethod  # TODO: athelyezni megfelelobb helyre
    def szotagszam(sztring):
        szam = 0
        for letter in sztring.lower():
            if letter in 'aáeéiíoóöőuúüű':
                szam += 1
        return szam
