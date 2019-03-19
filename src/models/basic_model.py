from Tkinter import *

import config


class BasicModel:
    """
    Basic physical properties model
    """
    def __init__(self, frame):
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        self._mechanical_label_frame = LabelFrame(frame, text='Mechanical properties',
                                                  borderwidth=config.FRAME_BORDER_WIDTH, relief=config.FRAME_RELIEF)
        self._mechanical_label_frame.grid(column=0, row=0, sticky=W + E, padx=config.FRAME_PADDING,
                                          pady=config.FRAME_PADDING)

        self._thermal_label_frame = LabelFrame(frame, text='Thermal properties', borderwidth=config.FRAME_BORDER_WIDTH,
                                               relief=config.FRAME_RELIEF)
        self._thermal_label_frame.grid(column=1, row=0, sticky=W + E, padx=config.FRAME_PADDING,
                                       pady=config.FRAME_PADDING)

        self._mechanical_value_label = Label(self._mechanical_label_frame, text="Value")
        self._mechanical_value_label.grid(column=1, row=0, sticky=W, padx=config.ELEMENT_PADDING,
                                          pady=config.ELEMENT_PADDING)
        self._mechanical_unit_label = Label(self._mechanical_label_frame, text="Unit")
        self._mechanical_unit_label.grid(column=2, row=0, sticky=W, padx=config.ELEMENT_PADDING,
                                         pady=config.ELEMENT_PADDING)
        self._thermal_value_label = Label(self._thermal_label_frame, text="Value")
        self._thermal_value_label.grid(column=1, row=0, sticky=W, padx=config.ELEMENT_PADDING,
                                       pady=config.ELEMENT_PADDING)
        self._thermal_unit_label = Label(self._thermal_label_frame, text="Unit")
        self._thermal_unit_label.grid(column=2, row=0, sticky=W, padx=config.ELEMENT_PADDING,
                                      pady=config.ELEMENT_PADDING)

        self._density_label = Label(self._mechanical_label_frame, text='Density')
        self.density_variable = DoubleVar()
        self._density_entry = Entry(self._mechanical_label_frame, textvariable=self.density_variable)
        self._density_unit = Label(self._mechanical_label_frame, text='kg/m^3')
        self._density_label.grid(row=1, column=0, sticky=E, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        self._density_entry.grid(row=1, column=1, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        self._density_unit.grid(row=1, column=2, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)

        self._elastic_label = Label(self._mechanical_label_frame, text='Elastic modulus')
        self.elastic_variable = DoubleVar()
        self._elastic_entry = Entry(self._mechanical_label_frame, textvariable=self.elastic_variable)
        self._elastic_unit = Label(self._mechanical_label_frame, text='Pa')
        self._elastic_label.grid(row=2, column=0, sticky=E, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        self._elastic_entry.grid(row=2, column=1, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        self._elastic_unit.grid(row=2, column=2, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)

        self._poisson_ratio_label = Label(self._mechanical_label_frame, text='Poisson\'s ratio')
        self.poisson_ratio_variable = DoubleVar()
        self._poisson_ratio_entry = Entry(self._mechanical_label_frame, textvariable=self.poisson_ratio_variable)
        self._poisson_ratio_unit = Label(self._mechanical_label_frame, text='-')
        self._poisson_ratio_label.grid(row=3, column=0, sticky=E, padx=config.ELEMENT_PADDING,
                                       pady=config.ELEMENT_PADDING)
        self._poisson_ratio_entry.grid(row=3, column=1, sticky=W, padx=config.ELEMENT_PADDING,
                                       pady=config.ELEMENT_PADDING)
        self._poisson_ratio_unit.grid(row=3, column=2, sticky=W, padx=config.ELEMENT_PADDING,
                                      pady=config.ELEMENT_PADDING)

        self._thermal_conductivity_label = Label(self._thermal_label_frame, text='Thermal conductivity')
        self.thermal_conductivity_variable = DoubleVar()
        self._thermal_conductivity_entry = Entry(self._thermal_label_frame,
                                                 textvariable=self.thermal_conductivity_variable)
        self._thermal_conductivity_unit = Label(self._thermal_label_frame, text='W/(m*K)')
        self._thermal_conductivity_label.grid(row=1, column=0, sticky=E, padx=config.ELEMENT_PADDING,
                                              pady=config.ELEMENT_PADDING)
        self._thermal_conductivity_entry.grid(row=1, column=1, sticky=W, padx=config.ELEMENT_PADDING,
                                              pady=config.ELEMENT_PADDING)
        self._thermal_conductivity_unit.grid(row=1, column=2, sticky=W, padx=config.ELEMENT_PADDING,
                                             pady=config.ELEMENT_PADDING)

        self._heat_capacity_label = Label(self._thermal_label_frame, text='Heat capacity')
        self.heat_capacity_variable = DoubleVar()
        self._heat_capacity_entry = Entry(self._thermal_label_frame, textvariable=self.heat_capacity_variable)
        self._heat_capacity_unit = Label(self._thermal_label_frame, text='J/(kg*K)')
        self._heat_capacity_label.grid(row=2, column=0, sticky=E, padx=config.ELEMENT_PADDING,
                                       pady=config.ELEMENT_PADDING)
        self._heat_capacity_entry.grid(row=2, column=1, sticky=W, padx=config.ELEMENT_PADDING,
                                       pady=config.ELEMENT_PADDING)
        self._heat_capacity_unit.grid(row=2, column=2, sticky=W, padx=config.ELEMENT_PADDING,
                                      pady=config.ELEMENT_PADDING)

        self._inelastic_heat_label = Label(self._thermal_label_frame, text='Inelastic heat fraction')
        self.inelastic_heat_variable = DoubleVar()
        self._inelastic_heat_entry = Entry(self._thermal_label_frame, textvariable=self.inelastic_heat_variable)
        self._inelastic_heat_unit = Label(self._thermal_label_frame, text='-')
        self._inelastic_heat_label.grid(row=3, column=0, sticky=E, padx=config.ELEMENT_PADDING,
                                        pady=config.ELEMENT_PADDING)
        self._inelastic_heat_entry.grid(row=3, column=1, sticky=W, padx=config.ELEMENT_PADDING,
                                        pady=config.ELEMENT_PADDING)
        self._inelastic_heat_unit.grid(row=3, column=2, sticky=W, padx=config.ELEMENT_PADDING,
                                       pady=config.ELEMENT_PADDING)

    @property
    def properties(self):
        return {
            config.ELASTIC_MODULUS: self.elastic_variable.get(),
            config.POISSON_RATIO: self.poisson_ratio_variable.get(),
            config.DENSITY: self.density_variable.get(),
            config.THERM_CONDUCTIVITY: self.thermal_conductivity_variable.get(),
            config.HEAT_CAPACITY: self.heat_capacity_variable.get(),
            config.INELASTIC_HEAT: self.inelastic_heat_variable.get()
        }
