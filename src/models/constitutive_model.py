import json
import os
from Tkinter import *

import config


class ConstitutiveModel:
    """
    Constitutive model's parameters container
    """

    def __init__(self, subdir):
        """
        :param subdir: Constitutive models directory
        """
        json_path = os.path.join(subdir, config.CONFIG_FILE)
        self.subroutine_path = os.path.join(subdir, config.SUBROUTINE_FILE)
        with open(json_path, 'r') as json_file:
            json_contents = json.load(json_file)
        self.variables = json_contents[config.KEY_VARIABLES]
        self.variables.sort(key=lambda x: x[config.KEY_IDENTIFIER])
        self.name = json_contents[config.KEY_VARIABLE_NAME]
        self.frames = []
        for variable in self.variables:
            variable[config.KEY_HOLDER] = DoubleVar(value=0.0)

    def populate(self, frame):
        for child in frame.winfo_children():
            child.destroy()
        value_label = Label(frame, text='Value')
        value_label.grid(row=0, column=1, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)

        unit_label = Label(frame, text='Unit')
        unit_label.grid(row=0, column=2, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)

        description_label = Label(frame, text='Description')
        description_label.grid(row=0, column=3, sticky=W, padx=config.ELEMENT_PADDING,
                               pady=config.ELEMENT_PADDING)
        for counter, user_variable in enumerate(self.variables):
            row = counter + 1
            name_label = Label(frame, text=user_variable[config.KEY_VARIABLE_NAME])
            name_label.grid(row=row, column=0, sticky=E, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
            value_label = Entry(frame, textvariable=user_variable[config.KEY_HOLDER])
            value_label.grid(row=row, column=1, sticky=E + W, padx=config.ELEMENT_PADDING,
                             pady=config.ELEMENT_PADDING)
            unit_label = Label(frame, text=user_variable[config.KEY_UNIT])
            unit_label.grid(row=row, column=2, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
            description_label = Label(frame, text=user_variable[config.KEY_DESCRIPTION])
            description_label.grid(row=row, column=3, sticky=W, padx=config.ELEMENT_PADDING,
                                   pady=config.ELEMENT_PADDING)

    @property
    def properties(self):
        return [
            {
                config.KEY_VARIABLE_NAME: v[config.KEY_VARIABLE_NAME],
                config.KEY_HOLDER: v[config.KEY_HOLDER].get()
            }
            for v in self.variables
        ]
