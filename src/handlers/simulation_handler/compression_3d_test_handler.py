import math
from Tkinter import *

import config
from src.builders import *
from src.builders.standard_explicit_model_builder import StandardExplicitModelBuilder
from src.builders.user_material_builder import UserMaterialBuilder
from src.handlers.simulation_handler.base_simulation_handler import BaseSimulationHandler
from src.utils import is_positive_float


class Compression3DTestHandler(BaseSimulationHandler):
    """
    Compression test handler, 3D setting
    """

    def __init__(self):
        BaseSimulationHandler.__init__(self)
        # Specimen parameters
        self.specimen_length = DoubleVar(value=15.0)
        self.specimen_radius = DoubleVar(value=10.0)
        self.material_name = StringVar(value="")
        # Model parameters
        self.tool_displacement = DoubleVar(value=3.0)
        self.friction_coefficient = DoubleVar(value=0.1)
        self.initial_temperature = DoubleVar(value=293.15)
        self.duration = DoubleVar(value=1.0)
        self.mesh_edge_length = DoubleVar(value=1.0)

    def builders(self):
        # TODO: Compose proper builder sequence for compression test
        model_builder = StandardExplicitModelBuilder()
        user_material_builder = UserMaterialBuilder()

        model_builder.next_builder = user_material_builder
        return [
            model_builder,
            user_material_builder
        ]

    def parameters(self):
        self._validate_parameters()

        radius = self.specimen_radius.get()

        scaling_factor = 1e-3

        displacement = self.tool_displacement.get() * scaling_factor * -1.0

        tool_radius = radius * scaling_factor * 1.5

        return {
            SPECIMEN_BASE_RADIUS: radius * scaling_factor,
            SPECIMEN_LENGTH: self.specimen_length.get() * scaling_factor,
            SOURCE_MATERIAL_NAME: self.material_name.get(),
            TARGET_MATERIAL_NAME: self.material_name.get(),
            SPECIMEN_TEMPERATURE: self.initial_temperature.get(),
            MESH_EDGE_LENGTH: self.mesh_edge_length.get() * scaling_factor,
            FRICTION_COEFFICIENT: self.friction_coefficient.get(),
            DISPLACEMENT_DURATION: self.duration.get(),
            TOOL_DISPLACEMENT: displacement,
            TOOL_RADIUS: tool_radius
        }

    def _populate(self, frame):
        self.__positive_validator = frame.register(is_positive_float)
        self.__dimension_validator = frame.register(self.__validate_dimensions)

        self.__create_specimen_entries(frame)

        self.__create_model_entries(frame)

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

        self._create_entry_line(self.material_name, 'Material', None, specimen_frame, 0, None)

        value_label = Label(specimen_frame, text='Value')
        value_label.grid(column=1, row=1, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        unit_label = Label(specimen_frame, text='Unit')
        unit_label.grid(column=2, row=1, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)

        self._create_entry_line(self.specimen_length, 'Length', 'mm', specimen_frame, 2,
                                (self.__dimension_validator, '%P'))
        self._create_entry_line(self.specimen_radius, 'Radius', 'mm', specimen_frame, 3,
                                (self.__dimension_validator, '%P'))

    def __create_model_entries(self, frame):
        """
        Create UI controls for defining test conditions
        :param frame: parent frame
        :return: None
        """
        conditions_frame = LabelFrame(frame, text='Model parameters', borderwidth=config.FRAME_BORDER_WIDTH,
                                      relief=config.FRAME_RELIEF)
        conditions_frame.grid(column=0, row=1, sticky=W + E + N + S, padx=config.FRAME_PADDING,
                              pady=config.FRAME_PADDING)

        value_label = Label(conditions_frame, text='Value')
        value_label.grid(column=1, row=0, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)
        unit_label = Label(conditions_frame, text='Unit')
        unit_label.grid(column=2, row=0, sticky=W, padx=config.ELEMENT_PADDING, pady=config.ELEMENT_PADDING)

        self._create_entry_line(self.initial_temperature, 'Initial temperature', 'K', conditions_frame, 1,
                                (self.__positive_validator, '%P'))
        self._create_entry_line(self.tool_displacement, 'Tool displacement', 'mm', conditions_frame, 2,
                                (self.__positive_validator, '%P'))
        self._create_entry_line(self.duration, 'Duration', 's', conditions_frame, 3,
                                (self.__positive_validator, '%P'))
        self._create_entry_line(self.mesh_edge_length, 'Mesh edge length', 'mm', conditions_frame, 4,
                                (self.__positive_validator, '%P'))
        self._create_entry_line(self.friction_coefficient, 'Friction coefficient', '-', conditions_frame, 5,
                                (self.__positive_validator, '%P'))

    def __validate_dimensions(self, v):
        """
        Validation function with dimension correctness checks

        :param v: entry value
        :return: bool
        """
        return \
            is_positive_float(v) and self.__are_parameters_consistent()

    def __are_parameters_consistent(self):
        length = self.specimen_length.get()
        displacement = self.tool_displacement.get()
        return length > displacement

    def _validate_parameters(self):
        scaling_factor = 1e-3
        positive_values = {
            SPECIMEN_BASE_RADIUS: self.specimen_radius.get() * scaling_factor,
            SPECIMEN_LENGTH: self.specimen_length.get() * scaling_factor,
            TOOL_DISPLACEMENT: self.tool_displacement.get(),
            SOURCE_MATERIAL_NAME: self.material_name.get(),
            TARGET_MATERIAL_NAME: self.material_name.get(),
            SPECIMEN_TEMPERATURE: self.initial_temperature.get(),
            MESH_EDGE_LENGTH: self.mesh_edge_length.get(),
            DISPLACEMENT_DURATION: self.duration.get(),
            FRICTION_COEFFICIENT: self.friction_coefficient.get()
        }
        for k, v in positive_values.iteritems():
            if not is_positive_float(v):
                raise ValueError("Invalid property '%s': must be positive" % k)
