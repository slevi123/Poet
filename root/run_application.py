import tkinter as tk

from root.custom_widgets.MainWindow import MainWindow

# TODO: szakaszokra tagolas szinekkel


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).pack(expand=True, fill='both')
    # root.attributes("-fullscreen", True)
    root.mainloop()
