from Tkinter import *

from abaqus import session
from abaqusConstants import *

from src.gui_main_window import GuiMainWindow


def run():
    session.graphicsOptions.setValues(
        highlightMethodHint=XOR,
        antiAlias=OFF,
        translucencyMode=1
    )
    gui = GuiMainWindow()
    gui.run()
