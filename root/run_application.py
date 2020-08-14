import tkinter as tk

from root.custom_widgets.MainWindow import MainWindow

# TODO: szakaszokra tagolas szinekkel
# TODO: add synonime and rhyme search support
# TODO: add english support
# TODO: create a browser interface

if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(expand=True, fill='both')
    # root.attributes("-fullscreen", True)
    root.mainloop()
