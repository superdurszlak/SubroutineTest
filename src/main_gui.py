from Tkinter import *
import config
import ttk


class MainGUI:
    """SubroutineTest main GUI class"""
    def __init__(self):
        self.master = Tk()
        self.master.minsize(config.MIN_WIDTH, config.MIN_HEIGHT)
        self.master.mainloop()
