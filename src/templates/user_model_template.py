from Tkinter import *

import config
from src.models.basic_model import BasicModel
from src.models.constitutive_model import ConstitutiveModel


class UserModelTemplate(Frame):
    def __init__(self, master, name, basic_model, constitutive_model, **kw):
        Frame.__init__(self, master, borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF,
                       width=master.winfo_width() - 2 * config.FRAME_PADDING, **kw)
        if not isinstance(basic_model, BasicModel):
            raise TypeError('basic_model must be instance of BasicModel')
        if not isinstance(constitutive_model, ConstitutiveModel):
            raise TypeError('constitutive_model must be instance of ConstitutiveModel')

        self.density = basic_model.density_variable.get()
        self.elastic_modulus = basic_model.elastic_variable.get()
        self.poisson_ratio = basic_model.poisson_ratio_variable.get()
        self.thermal_conductivity = basic_model.thermal_conductivity_variable.get()
        self.heat_capacity = basic_model.heat_capacity_variable.get()
        self.inelastic_heat_fraction = basic_model.inelastic_heat_variable.get()
        self.user_variables = [v[config.KEY_HOLDER].get() for v in constitutive_model.variables]

        self.pack(fill=X, expand=1, padx=config.FRAME_PADDING, pady=config.FRAME_PADDING)
        self.name = name
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)

        quoted_name = 'Name: %s' % name
        self.__material_name_label = Label(self, text=quoted_name)
        self.__material_name_label.grid(row=0, column=0, sticky=W, padx=config.ELEMENT_PADDING,
                                        pady=config.ELEMENT_PADDING)

        material_type = 'Type: %s' % constitutive_model.name
        self.__material_type_label = Label(self, text=material_type)
        self.__material_type_label.grid(row=0, column=1, sticky=W, padx=config.ELEMENT_PADDING,
                                        pady=config.ELEMENT_PADDING)

        variable_string = '(%d model variables)' % len(constitutive_model.variables)
        self.__variables_label = Label(self, text=variable_string)
        self.__variables_label.grid(row=0, column=2, sticky=W, padx=config.ELEMENT_PADDING,
                                    pady=config.ELEMENT_PADDING)

        self.__delete_button = Button(self, text='Delete', command=self.__on_delete_click)
        self.__delete_button.grid(row=0, column=3, sticky=E, padx=config.ELEMENT_PADDING,
                                  pady=config.ELEMENT_PADDING)

    def __on_delete_click(self):
        self.destroy()
