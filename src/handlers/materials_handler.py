from Tkinter import *

import config
from src.handlers.base_handler import BaseHandler
from src.handlers.material_editor_handler import MaterialEditorHandler
from src.handlers.material_list.material_list_label_frame import MaterialListLabelFrame


class MaterialsHandler(BaseHandler):
    """
    User defined materials management handler
    """

    def _configure(self):
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.materials_list_frame = MaterialListLabelFrame(master=self.frame, text='Materials',
                                                           width=config.MIN_WIDTH / 2,
                                                           borderwidth=config.FRAME_BORDER_WIDTH,
                                                           relief=config.FRAME_RELIEF)
        self.materials_list_frame.grid(row=0, column=0, sticky=N + W + S + E,
                                       padx=config.FRAME_PADDING, pady=config.FRAME_PADDING)

        self.materials_edit_frame = LabelFrame(self.frame, text='Material editor',
                                               borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
        self.materials_edit_frame.grid(row=1, column=0, sticky=N + W + S + E,
                                       padx=config.FRAME_PADDING, pady=config.FRAME_PADDING)
        self.material_edit_handler = MaterialEditorHandler(self.materials_edit_frame, self.materials_list_frame)

    @property
    def materials_list(self):
        return self.materials_list_frame
