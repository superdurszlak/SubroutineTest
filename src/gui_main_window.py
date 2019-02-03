import os
from Tkinter import *
import config

from src import utils
from src.handlers.materials_handler import MaterialsHandler
from src.handlers.simulation_type_handler import SimulationTypeHandler


class GuiMainWindow:
    """
    SubroutineTest main window class
    """
    def __init__(self):
        """
        Pre-configure main window layout and invoke specific handlers
        """
        self.master = Tk()
        self.master.title('Subroutine Test plugin')
        self.master.iconbitmap(os.path.join(config.RESOURCES_DIR, 'icon.ico'))
        self.master.minsize(config.MIN_WIDTH, config.MIN_HEIGHT)
        self.__create_basic_controls()
        self.__load_material_models()
        side_frames_width = config.MIN_WIDTH / 2
        bottom_frame_width = config.MIN_WIDTH + config.FRAME_PADDING*2
        bottom_frame_height = 50
        side_frames_height = config.MIN_HEIGHT
        self.simulation_type_frame = Frame(self.master, width=side_frames_width, height=side_frames_height,
                                           borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
        self.simulation_type_frame.grid(row=0, column=0, padx=config.FRAME_PADDING, pady=config.FRAME_PADDING,
                                        sticky=N+W+S+E)
        self.materials_frame = Frame(self.master, width=side_frames_width, height=side_frames_height)
        self.materials_frame.grid(row=0, column=1, sticky=N+W+S+E)
        self.controls_frame = Frame(self.master, width=bottom_frame_width, height=bottom_frame_height,
                                    borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
        self.controls_frame.grid(row=1, column=0, columnspan=2, padx=config.FRAME_PADDING, pady=config.FRAME_PADDING)

        self.simulation_type_handler = SimulationTypeHandler(self.simulation_type_frame)
        self.materials_handler = MaterialsHandler(self.materials_frame)

    def run(self):
        """
        Run window main loop
        """
        self.master.mainloop()

    def __create_basic_controls(self):
        pass

    def __load_material_models(self):
        contents = [os.path.join(config.MODEL_DIR, c) for c in os.listdir(config.MODEL_DIR)]
        subdirs = [d for d in contents if os.path.isdir(d) and utils.is_valid_model_dir(d)]

