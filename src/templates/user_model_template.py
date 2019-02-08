from Tkinter import *

import config


class UserModelTemplate(Frame):
    def __init__(self, master, name, basic_model, constitutive_model, **kw):
        Frame.__init__(self, master, borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF,
                       width=master.winfo_width() - 2 * config.FRAME_PADDING, **kw)
        self.name = name

        self.density = basic_model.density_variable.get()
        self.elastic_modulus = basic_model.elastic_variable.get()
        self.poisson_ratio = basic_model.poisson_ratio_variable.get()
        self.thermal_conductivity = basic_model.thermal_conductivity_variable.get()
        self.heat_capacity = basic_model.heat_capacity_variable.get()
        self.inelastic_heat_fraction = basic_model.inelastic_heat_variable.get()
        self.user_variables = [v[config.KEY_HOLDER].get() for v in constitutive_model.variables]

        self.pack(fill=X, expand=1, padx=config.FRAME_PADDING, pady=config.FRAME_PADDING)
        self.grid_columnconfigure(0, weight=9)
        self.grid_columnconfigure(1, weight=1)

        quoted_name = '"%s"' % name

        material_type = '%s model' % constitutive_model.name

        variable_string = '%d model variables' % len(constitutive_model.variables)

        label_text = '%s, %s, %s' % (quoted_name, material_type, variable_string)
        self.__material_name_label = Label(self, text=label_text)
        self.__material_name_label.grid(row=0, column=0, sticky=W, padx=config.ELEMENT_PADDING,
                                        pady=config.ELEMENT_PADDING)

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
