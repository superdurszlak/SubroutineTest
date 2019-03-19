import json
import os
from Tkinter import *

import config
from src.templates.material_tooltip import MaterialTooltip


class UserModelTemplate(Frame):
    def __init__(self, master, name, model_name, subroutine_path, basic_model, constitutive_model, **kw):
        Frame.__init__(self, master, borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF,
                       width=master.winfo_width() - 2 * config.FRAME_PADDING, **kw)
        self.__basic_model = basic_model
        self.__constitutive_model = constitutive_model
        self.__model_name = model_name
        self.name = name
        self.subroutine_path = subroutine_path
        self.density = basic_model[config.DENSITY]
        self.elastic_modulus = basic_model[config.ELASTIC_MODULUS]
        self.poisson_ratio = basic_model[config.POISSON_RATIO]
        self.thermal_conductivity = basic_model[config.THERM_CONDUCTIVITY]
        self.heat_capacity = basic_model[config.HEAT_CAPACITY]
        self.inelastic_heat_fraction = basic_model[config.INELASTIC_HEAT]
        self.user_variables = [v[config.KEY_HOLDER] for v in constitutive_model]

        self.pack(fill=X, expand=1, padx=config.FRAME_PADDING, pady=config.FRAME_PADDING)
        self.grid_columnconfigure(0, weight=9)
        self.grid_columnconfigure(1, weight=1)

        quoted_name = '"%s"' % name

        material_type = '%s model' % self.__model_name

        variable_string = '%d model variables' % len(self.__constitutive_model)

        label_text = '%s, %s, %s' % (quoted_name, material_type, variable_string)
        self.__material_name_label = Label(self, text=label_text)
        self.__material_name_label.grid(row=0, column=0, sticky=W, padx=config.ELEMENT_PADDING,
                                        pady=config.ELEMENT_PADDING)

        self.__tooltip = MaterialTooltip(self.__material_name_label, self.__make_text())

        self.__delete_button = Button(self, text='Delete', command=self.__on_delete_click)
        self.__delete_button.grid(row=0, column=1, sticky=E, padx=config.ELEMENT_PADDING,
                                  pady=config.ELEMENT_PADDING)
        try:
            self.master.subscribe(self)
        except KeyError:
            self.destroy()
            raise

    def __on_delete_click(self):
        self.master.remove(self.name)

    def __make_text(self):
        pairs = [
                    ('Density', self.density),
                    ('Elastic modulus', self.elastic_modulus),
                    ('Poisson\'s ratio', self.poisson_ratio),
                    ('Thermal conductivity', self.thermal_conductivity),
                    ('Heat capacity', self.heat_capacity),
                    ('Inelastic heat fraction', self.inelastic_heat_fraction)
                ] + [
                    (v[config.KEY_VARIABLE_NAME], v[config.KEY_HOLDER]) for v in self.__constitutive_model
                ]
        return "\n".join("%s=%f" % v for v in pairs)

    def to_json(self, file_path):
        with open(file_path, 'w') as json_file:
            data = {
                config.NAME: self.name,
                config.KEY_MODEL_NAME: self.__model_name,
                config.BASIC_PROPERTIES: self.__basic_model,
                config.MODEL_PROPERTIES: self.__constitutive_model,
                config.SUBROUTINE_PATH: self.subroutine_path
            }
            json.dump(data, json_file)

    @classmethod
    def from_json(cls, parent, file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            name = str(data[config.NAME])
            model_name = str(data[config.KEY_MODEL_NAME])
            subroutine_path = str(data[config.SUBROUTINE_PATH])
            basic_model = data[config.BASIC_PROPERTIES]
            constitutive_model = data[config.MODEL_PROPERTIES]
            return cls(parent, name, model_name, subroutine_path, basic_model, constitutive_model)
