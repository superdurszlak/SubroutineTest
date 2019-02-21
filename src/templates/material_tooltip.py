from Tkinter import *

import config


class MaterialTooltip:
    def __init__(self, master, text):
        self.master = master
        self.text = text
        self.master.bind('<Enter>', self.enter)
        self.master.bind('<Leave>', self.close)
        self.top_level = None
        self.label = None

    def enter(self, _):
        def create():
            x, y, cx, cy = self.master.bbox('insert')
            x += self.master.winfo_rootx() + 25
            y += self.master.winfo_rooty() + 20
            self.top_level = Toplevel(self.master)
            self.top_level.wm_overrideredirect(True)
            self.top_level.wm_geometry('+%d+%d' % (x, y))
            self.label = Label(self.top_level, text=self.text, justify='left',
                               background='white', relief='solid', borderwidth=1)
            self.label.pack(ipadx=1)

        self.master.after(config.TOOLTIP_DELAY, create)

    def close(self, _):
        if self.top_level is not None:
            def destroy():
                self.label.destroy()
                self.top_level.destroy()
                self.top_level = None
                self.label = None

            self.top_level.after(config.TOOLTIP_DELAY, destroy)
