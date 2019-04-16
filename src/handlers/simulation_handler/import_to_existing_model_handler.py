from Tkinter import StringVar, N, S, E, W, LabelFrame

import config
from src.builders import *
from src.builders.job_builder import JobBuilder
from src.builders.user_material_builder import UserMaterialBuilder
from src.handlers.simulation_handler.base_simulation_handler import BaseSimulationHandler


class ImportToExistingModelHandler(BaseSimulationHandler):
    """
    Import to existing CAE model handler
    """

    def __init__(self):
        BaseSimulationHandler.__init__(self)
        self.source_material_name = StringVar(value="")
        self.target_material_name = StringVar(value="")

    @property
    def builders(self):
        material_builder = UserMaterialBuilder()
        job_buidler = JobBuilder()

        material_builder.next_builder = job_buidler
        return [
            material_builder,
            job_buidler
        ]

    @property
    def parameters(self):
        return {
            SOURCE_MATERIAL_NAME: self.source_material_name.get(),
            TARGET_MATERIAL_NAME: self.target_material_name.get()
        }

    def _populate(self, frame):

        settings_frame = LabelFrame(frame, text='Material import', borderwidth=config.FRAME_BORDER_WIDTH,
                                    relief=config.FRAME_RELIEF)
        settings_frame.grid(column=0, row=0, sticky=W + E + N + S, padx=config.FRAME_PADDING,
                            pady=config.FRAME_PADDING)
        self._create_entry_line(self.source_material_name, 'Source material', None, settings_frame, 0, None)
        self._create_entry_line(self.target_material_name, 'Target material', None, settings_frame, 1, None)


