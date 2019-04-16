import abc
from Tkconstants import E, W
from Tkinter import Label, Entry

import config
from src.utils import is_positive_float


class BaseSimulationHandler:
    """
    Base class for all simulation handlers
    """

    def __init__(self):
        self._validator = None

    def populate(self, frame):
        """
        Clear frame object and populate it with handler's controls

        :param frame: Frame object to which UI controls will be bound
        :return: None
        """
        for child in frame.winfo_children():
            child.destroy()
        self._validator = frame.register(is_positive_float)
        self._populate(frame)

    @abc.abstractmethod
    def _populate(self, frame):
        """
        Class-specific inner implementation of populate method

        :param frame: Frame object to which UI controls will be bound
        :return: None
        """
        pass

    @abc.abstractproperty
    def parameters(self):
        """
        Dictionary of parameters relevant for this handler and possibly nested handlers
        :return: dictionary of parameters
        """
        pass

    @abc.abstractproperty
    def builders(self):
        """
        Get all builders relevant for this handler and possibly nested handlers
        :return: list of builders, with each builder tied to previous one as 'next_builder'
        """
        pass

    @staticmethod
    def _create_entry_line(variable, name, unit, frame, row_index, validator):
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
        if name is not None:
            variable_label = Label(frame, text=name)
            variable_label.grid(column=0, row=row_index, sticky=E, padx=config.ELEMENT_PADDING,
                                pady=config.ELEMENT_PADDING)
        if validator is not None:
            variable_entry = Entry(frame, textvariable=variable, validate='focusout', validatecommand=validator)
        else:
            variable_entry = Entry(frame, textvariable=variable)
        variable_entry.grid(column=1, row=row_index, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        if unit is not None:
            variable_unit = Label(frame, text=unit)
            variable_unit.grid(column=2, row=row_index, sticky=W, padx=config.ELEMENT_PADDING,
                               pady=config.ELEMENT_PADDING)
