import Tkinter
import os
from Tkinter import *
from ttk import *

import config
from src import utils
from src.handlers.base_handler import BaseHandler
from src.models.basic_model import BasicModel
from src.models.constitutive_model import ConstitutiveModel
from src.templates.user_model_template import UserModelTemplate


class MaterialEditorHandler(BaseHandler):
    def __init__(self, frame, materials_container):
        self.__materials_container = materials_container
        super(MaterialEditorHandler, self).__init__(frame)

    def _configure(self):
        self.__load_models()
        first_model = self.models.keys()[0]
        self.chosen_model_variable = StringVar(value=first_model)

        self.material_properties_frame = Frame(self.frame)
        self.material_properties_frame.grid(column=0, row=0, sticky=N + W + E + S)
        self.basic_model = BasicModel(self.material_properties_frame)

        self.model_type_combobox = Combobox(self.frame, values=self.models.keys(),
                                            textvariable=self.chosen_model_variable)
        self.model_type_combobox.bind('<<ComboboxSelected>>', self.__on_model_selected)
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

        self.__on_model_selected()

        self.options_frame = Frame(self.frame)
        self.options_frame.grid(column=0, row=3, columnspan=3, sticky=N + W + S, padx=config.FRAME_PADDING,
                                pady=config.FRAME_PADDING)

        self.model_variable_label = Label(self.options_frame, text='Model name:')
        self.model_variable_label.grid(column=0, row=0, sticky=W, padx=config.FRAME_PADDING,
                                       pady=config.FRAME_PADDING)

        self.model_name_variable = StringVar()
        self.model_variable_entry = Entry(self.options_frame, textvariable=self.model_name_variable)
        self.model_variable_entry.grid(column=1, row=0, sticky=W, padx=config.FRAME_PADDING,
                                       pady=config.FRAME_PADDING)

        self.create_model_button = Button(self.options_frame, text='Create', command=self.__on_create_click)
        self.create_model_button.grid(column=2, row=0, sticky=W, padx=config.FRAME_PADDING,
                                      pady=config.FRAME_PADDING)

    def generate_material(self):
        """
        Create material with user-defined plastic behaviour
        :return: None
        """
        pass

    def __load_models(self):
        """
        Load valid user material models
        :return: None
        """
        self.models = {}

        contents = [os.path.join(config.MODEL_DIR, c) for c in os.listdir(config.MODEL_DIR)]
        subdirs = [d for d in contents if os.path.isdir(d) and utils.is_valid_model_dir(d)]

        for subdir in subdirs:
            model = ConstitutiveModel(subdir)
            self.models[model.name] = model

    def __on_model_selected(self, event=None):
        """
        Populate model parameters editor with controls related to selected model
        :param event: event that triggered execution of the method
        :return: event
        """
        self.models[self.chosen_model_variable.get()].populate(self.model_variables_frame)
        return event

    def __on_create_click(self):
        """
        Create UserMaterialTemplate from material and model parameters
        :return: None
        """
        selected_model = self.models[self.chosen_model_variable.get()]
        UserModelTemplate(name=self.model_variable_entry.get(), master=self.__materials_container,
                          basic_model=self.basic_model, constitutive_model=selected_model)
