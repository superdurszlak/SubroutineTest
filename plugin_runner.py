from Tkinter import *
import ttk
import tkFileDialog

from abaqus import mdb, session
from abaqusConstants import *

from src.main_gui import MainGUI


def run():
    session.graphicsOptions.setValues(
        highlightMethodHint=XOR,
        antiAlias=OFF,
        translucencyMode=1
    )
    gui = MainGUI()
