from Tkinter import *

import config
from src.handlers.simulation_handler.base_simulation_handler import BaseSimulationHandler
from src.utils import is_positive_float


class FlatTensile2DTestHandler(BaseSimulationHandler):
    """
    Flat tensile test handler, 2D setting
    """

    def __init__(self):
        BaseSimulationHandler.__init__(self)
        self.reduced_section_length = DoubleVar(value=100.0)
        self.reduced_section_width = DoubleVar(value=15.0)
        self.grip_section_length = DoubleVar(value=30.0)
        self.grip_section_width = DoubleVar(value=30.0)
        self.taper_length = DoubleVar(value=10.0)
        self._entries_store = []

    def _populate(self, frame):
        self._entries_store = []
        self.__validator = frame.register(self.__validate_dimensions)

        self.__create_specimen_entries(frame)

        conditions_frame = LabelFrame(frame, text='Test conditions', borderwidth=config.FRAME_BORDER_WIDTH,
                                      relief=config.FRAME_RELIEF)
        conditions_frame.grid(column=0, row=1, sticky=W + E + N + S, padx=config.FRAME_PADDING,
                              pady=config.FRAME_PADDING)

    def __create_specimen_entries(self, frame):
        """
        Create UI controls for defining specimen parameters
        :param frame: parent frame
        :return: None
        """

        specimen_frame = LabelFrame(frame, text='Specimen', borderwidth=config.FRAME_BORDER_WIDTH,
                                    relief=config.FRAME_RELIEF)
        specimen_frame.grid(column=0, row=0, sticky=W + E + N + S, padx=config.FRAME_PADDING,
                            pady=config.FRAME_PADDING)

        value_label = Label(specimen_frame, text='Value')
        value_label.grid(column=1, row=0, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        unit_label = Label(specimen_frame, text='Unit')
        unit_label.grid(column=2, row=0, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)

        self.__create_entry_line(self.reduced_section_width, 'Reduced section width', 'mm', specimen_frame, 1,
                                 (self.__validator, '%P'))
        self.__create_entry_line(self.reduced_section_length, 'Reduced section length', 'mm', specimen_frame, 2,
                                 (self.__validator, '%P'))
        self.__create_entry_line(self.grip_section_width, 'Grip width', 'mm', specimen_frame, 3,
                                 (self.__validator, '%P'))
        self.__create_entry_line(self.grip_section_length, 'Grip length', 'mm', specimen_frame, 4,
                                 (self.__validator, '%P'))
        self.__create_entry_line(self.taper_length, 'Taper section length', 'mm', specimen_frame, 5,
                                 (self.__validator, '%P'))

    def __validate_dimensions(self, v):
        """
        Validation function with dimension correctness checks

        :param v: entry value
        :return: bool
        """
        grip_width = self.grip_section_width.get()
        reduced_section_width = self.reduced_section_width.get()
        taper_length = self.taper_length.get()
        return \
            is_positive_float(v) \
            and grip_width > reduced_section_width \
            and (grip_width - reduced_section_width) / 2.0 <= taper_length

    def __create_entry_line(self, variable, name, unit, frame, row_index, validator):
        """
        Create label and entry for given variable

        :param variable: DoubleVar that has to be handled
        :param name: visible name of entry
        :param unit: unit of variable
        :param frame: parent frame for entry
        :param row_index: grid row in which the entry will be placed
        :param validator: Value validator
        :return: None
        """
        variable_label = Label(frame, text=name)
        variable_label.grid(column=0, row=row_index, sticky=E, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        variable_entry = Entry(frame, textvariable=variable, validate='focusout', validatecommand=validator)
        variable_entry.grid(column=1, row=row_index, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        variable_unit = Label(frame, text=unit)
        variable_unit.grid(column=2, row=row_index, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        self._entries_store.append(variable_entry)
