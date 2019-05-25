from Tkinter import *

import config
from src.builders import *
from src.builders.assembly_builder import AssemblyBuilder
from src.builders.border_conditions_builder import BorderConditionsBuilder
from src.builders.field_output_request_builder import FieldOutputRequestBuilder
from src.builders.flat_specimen_part_builder import FlatSpecimenPartBuilder
from src.builders.flat_specimen_sketch_builder import FlatSpecimenSketchBuilder
from src.builders.job_builder import JobBuilder
from src.builders.standard_explicit_model_builder import StandardExplicitModelBuilder
from src.builders.step_builder import StepBuilder
from src.builders.temperature_field_builder import TemperatureFieldBuilder
from src.builders.user_material_builder import UserMaterialBuilder
from src.handlers.simulation_handler.base_simulation_handler import BaseSimulationHandler
from src.utils import is_positive_float


class FlatTensile2DTestHandler(BaseSimulationHandler):
    """
    Flat tensile test handler, 2D setting
    """

    def __init__(self):
        BaseSimulationHandler.__init__(self)
        # Specimen parameters
        self.reduced_section_length = DoubleVar(value=100.0)
        self.reduced_section_width = DoubleVar(value=15.0)
        self.grip_section_length = DoubleVar(value=30.0)
        self.grip_section_width = DoubleVar(value=30.0)
        self.taper_length = DoubleVar(value=10.0)
        self.material_name = StringVar(value="")
        # Model parameters
        self.initial_temperature = DoubleVar(value=293.15)
        self.tool_displacement = DoubleVar(value=100.0)
        self.duration = DoubleVar(value=1.0)
        self.mesh_edge_length = DoubleVar(value=1.0)

    @property
    def parameters(self):
        self._validate_parameters()
        # Millimeters need to be converted back to meters
        conversion_factor = 1e-3
        return {
            GRIP_LENGTH: self.grip_section_length.get() * conversion_factor,
            GRIP_WIDTH: self.grip_section_width.get() * conversion_factor,
            TAPER_LENGTH: self.taper_length.get() * conversion_factor,
            REDUCED_WIDTH: self.reduced_section_width.get() * conversion_factor,
            REDUCED_LENGTH: self.reduced_section_length.get() * conversion_factor,
            MESH_EDGE_LENGTH: self.mesh_edge_length.get() * conversion_factor,
            DISPLACEMENT_DURATION: self.duration.get(),
            TOOL_DISPLACEMENT: self.tool_displacement.get() * conversion_factor,
            SPECIMEN_TEMPERATURE: self.initial_temperature.get(),
            SOURCE_MATERIAL_NAME: self.material_name.get(),
            TARGET_MATERIAL_NAME: self.material_name.get()
        }

    @property
    def builders(self):
        model_builder = StandardExplicitModelBuilder()
        sketch_builder = FlatSpecimenSketchBuilder()
        material_builder = UserMaterialBuilder()
        part_builder = FlatSpecimenPartBuilder()
        assembly_builder = AssemblyBuilder()
        step_builder = StepBuilder()
        output_builder = FieldOutputRequestBuilder()
        bc_builder = BorderConditionsBuilder()
        initial_field_builder = TemperatureFieldBuilder()
        job_buidler = JobBuilder()

        model_builder.next_builder = sketch_builder
        sketch_builder.next_builder = material_builder
        material_builder.next_builder = part_builder
        part_builder.next_builder = assembly_builder
        assembly_builder.next_builder = step_builder
        step_builder.next_builder = output_builder
        output_builder.next_builder = bc_builder
        bc_builder.next_builder = initial_field_builder
        initial_field_builder.next_builder = job_buidler
        return [
            model_builder,
            sketch_builder,
            material_builder,
            part_builder,
            assembly_builder,
            step_builder,
            bc_builder,
            initial_field_builder
        ]

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

        self._create_entry_line(self.reduced_section_width, 'Reduced section width', 'mm', specimen_frame, 2,
                                (self.__dimension_validator, '%P'))
        self._create_entry_line(self.reduced_section_length, 'Reduced section length', 'mm', specimen_frame, 3,
                                (self.__dimension_validator, '%P'))
        self._create_entry_line(self.grip_section_width, 'Grip width', 'mm', specimen_frame, 4,
                                (self.__dimension_validator, '%P'))
        self._create_entry_line(self.grip_section_length, 'Grip length', 'mm', specimen_frame, 5,
                                (self.__dimension_validator, '%P'))
        self._create_entry_line(self.taper_length, 'Taper section length', 'mm', specimen_frame, 6,
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

    def __validate_dimensions(self, v):
        """
        Validation function with dimension correctness checks

        :param v: entry value
        :return: bool
        """
        return \
            is_positive_float(v) and self.__are_parameters_consistent()

    def __are_parameters_consistent(self):
        grip_width = self.grip_section_width.get()
        reduced_section_width = self.reduced_section_width.get()
        taper_length = self.taper_length.get()
        return grip_width > reduced_section_width and (grip_width - reduced_section_width) / 2.0 <= taper_length

    def _validate_parameters(self):
        positive_values = {
            GRIP_LENGTH: self.grip_section_length.get(),
            GRIP_WIDTH: self.grip_section_width.get(),
            TAPER_LENGTH: self.taper_length.get(),
            REDUCED_WIDTH: self.reduced_section_width.get(),
            REDUCED_LENGTH: self.reduced_section_length.get(),
            MESH_EDGE_LENGTH: self.mesh_edge_length.get(),
            DISPLACEMENT_DURATION: self.duration.get(),
            TOOL_DISPLACEMENT: self.tool_displacement.get(),
            SPECIMEN_TEMPERATURE: self.initial_temperature.get()
        }
        for k, v in positive_values.iteritems():
            if not is_positive_float(v):
                raise ValueError("Invalid property '%s': must be positive" % k)
