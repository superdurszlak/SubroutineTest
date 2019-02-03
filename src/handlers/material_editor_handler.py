import json
import os
from Tkinter import *
from ttk import *

import config
from src import utils
from src.handlers.base_handler import BaseHandler


class ConstitutiveModel:
    """
    Constitutive model parameters container
    """
    def __init__(self, subdir):
        """
        :param subdir: Constitutive model directory
        """
        json_path = os.path.join(subdir, config.CONFIG_FILE)
        self.vuhard_path = os.path.join(subdir, config.VUHARD_FILE)
        with open(json_path, 'r') as json_file:
            json_contents = json.load(json_file)
        self.variables = json_contents['variables']
        self.variables.sort(key=lambda x: x['identifier'])
        self.name = json_contents['name']
        self.frames = []
        for variable in self.variables:
            variable['holder'] = DoubleVar(value=0.0)

    def populate(self, frame):
        if not isinstance(frame, Frame):
            raise ValueError('frame must be Tkinter.LabelFrame instance')
        for child in frame.winfo_children():
            child.destroy()
        self.frames = []
        for user_variable in self.variables:
            user_frame = Frame(frame)
            user_frame.pack(sticky=N)
            name_label = Label(user_frame, text=user_variable['name'])
            value_label = Entry(user_frame)



class MaterialEditorHandler(BaseHandler):
    def _configure(self):
        self.__load_models()
        self.model_type_choicebox = Combobox(self.frame)

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
