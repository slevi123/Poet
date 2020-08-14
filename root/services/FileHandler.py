from pathlib import Path


class FileHandler:
    def __init__(self, editor, path: Path = None):
        self.editor = editor
        # self.state = ('saved' or 'modified' or 'unsaved')
        if path is None:
            self.path = path
            self.state = 'unsaved'
        else:
            self.path = path.resolve()
            if self.path.is_file():
                self.editor.delete(1.0, 'end')
                print(self.path.read_text(encoding='utf-8'))
                self.editor.insert('0.0', self.path.read_text(encoding='utf-8'))
                self.state = 'saved'
            else:
                print('fuck u')
                # TODO: raise exception if file not found (self.path.is_file() )

    def save(self):
        try:
            text = self.editor.get("0.0", 'end')
            self.path.write_text(text, encoding='utf-8')
        except PermissionError:
            print('Permission Error- to be handled (TODO)')
            # TODO: handle this

    def close(self):
        if self.state != 'saved':
            pass
            # TODO: handle if isn't saved
