import Tkinter
import os
from Tkinter import *
from ttk import *

import config
from src import utils
from src.handlers.base_handler import BaseHandler
from src.models.basic_model import BasicModel
from src.models.constitutive_model import ConstitutiveModel


class MaterialEditorHandler(BaseHandler):
    def _configure(self):
        self.__load_models()
        first_model = self.models.keys()[0]
        self.chosen_model_variable = StringVar(value=first_model)

        self.material_properties_frame = Frame(self.frame)
        self.material_properties_frame.grid(column=0, row=0, sticky=N + W + E + S)
        self.basic_model = BasicModel(self.material_properties_frame)

        self.model_type_combobox = Combobox(self.frame, values=self.models.keys(),
                                            textvariable=self.chosen_model_variable)
        self.model_type_combobox.grid(column=0, row=1, sticky=S + W, padx=config.FRAME_PADDING,
                                      pady=config.FRAME_PADDING)

        self.model_variables_frame = Tkinter.LabelFrame(self.frame, text='Model properties',
                                                        borderwidth=config.FRAME_BORDER_WIDTH,
                                                        relief=config.FRAME_RELIEF)
        self.model_variables_frame.grid(column=0, row=2, sticky=W + E + S, padx=config.FRAME_PADDING,
                                        pady=config.FRAME_PADDING)

        self.model_variables_frame.grid_columnconfigure(0, weight=1)
        self.model_variables_frame.grid_columnconfigure(1, weight=2)
        self.model_variables_frame.grid_columnconfigure(2, weight=1)
        self.model_variables_frame.grid_columnconfigure(3, weight=4)
        self.models[first_model].populate(self.model_variables_frame)

        self.create_model_button = Button(self.frame, text="Create")
        self.create_model_button.grid(column=0, row=3, sticky=S + W, padx=config.FRAME_PADDING,
                                      pady=config.FRAME_PADDING)

    def generate_material(self):
        """
        Create material with user-defined plastic behaviour
        :return: None
        """
        pass

    def __load_models(self):
        self.models = {}

        contents = [os.path.join(config.MODEL_DIR, c) for c in os.listdir(config.MODEL_DIR)]
        subdirs = [d for d in contents if os.path.isdir(d) and utils.is_valid_model_dir(d)]

        for subdir in subdirs:
            model = ConstitutiveModel(subdir)
            self.models[model.name] = model
        pass
