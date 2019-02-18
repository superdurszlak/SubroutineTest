import os
from Tkinter import *

import config
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
        settings_frame_width = config.MIN_WIDTH / 3
        material_frame_width = config.MIN_WIDTH - settings_frame_width
        side_frames_height = config.MIN_HEIGHT
        self.simulation_type_frame = LabelFrame(self.master, text='Simulation settings', width=settings_frame_width,
                                                height=side_frames_height, borderwidth=config.FRAME_BORDER_WIDTH,
                                                relief=config.FRAME_RELIEF)
        self.simulation_type_frame.grid(row=0, column=0, padx=config.FRAME_PADDING, pady=config.FRAME_PADDING,
                                        sticky=N + W + S + E)
        self.materials_frame = Frame(self.master, width=material_frame_width, height=side_frames_height)
        self.materials_frame.grid(row=0, column=1, sticky=N + W + S + E)

        self.materials_canvas = Canvas(self.materials_frame, width=material_frame_width, height=side_frames_height,
                                       bd=0, highlightthickness=0, relief='ridge')
        self.materials_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.materials_scrollbar = Scrollbar(self.materials_frame, orient='vertical',
                                             command=self.materials_canvas.yview)
        self.materials_scrollbar.pack(side=RIGHT, fill=Y, expand=1)
        self.materials_canvas.config(yscrollcommand=self.materials_scrollbar.set)
        self.materials_inner_frame = Frame(self.materials_canvas, width=material_frame_width, height=side_frames_height)
        self.materials_inner_frame.pack(fill=BOTH, expand=1)
        self.materials_canvas.create_window((0, 0), window=self.materials_inner_frame, anchor=NW)

        def _adjust_width(_):
            if self.materials_inner_frame.winfo_reqwidth() != self.materials_canvas.winfo_width():
                self.materials_inner_frame.config(width=self.materials_inner_frame.winfo_reqwidth())

        self.materials_canvas.bind('<Configure>', _adjust_width)
        self.materials_inner_frame.bind('<Configure>', lambda _: self.materials_canvas.configure(
            scrollregion=self.materials_canvas.bbox("all")))

        self.materials_handler = MaterialsHandler(self.materials_inner_frame)
        self.simulation_type_handler = SimulationTypeHandler(self.simulation_type_frame)
        self.simulation_type_handler.material_templates_list = self.materials_handler.materials_list_frame

    def run(self):
        """
        Run window main loop
        """
        self.master.mainloop()
