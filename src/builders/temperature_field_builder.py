from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class TemperatureFieldBuilder(BaseBuilder):
    def __init__(self):
        super(TemperatureFieldBuilder, self).__init__()
        self._required_arguments = [
            MODEL_NAME,
            FULL_VOLUME_SET,
            SPECIMEN_TEMPERATURE,
            ASSEMBLY_NAME
        ]
        self._provided_arguments = [
            TEMPERATURE_FIELD_NAME
        ]

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME]
        full_volume_set = kwargs[FULL_VOLUME_SET],
        specimen_temperature = kwargs[SPECIMEN_TEMPERATURE]
        assembly_name = kwargs[ASSEMBLY_NAME]
        initial_temperature_field = 'Initial_Temperature_Field'
        root_assembly = mdb.models[model_name].rootAssembly
        region = root_assembly.instances[assembly_name].sets[full_volume_set]
        mdb.models[model_name].Temperature(name=initial_temperature_field, createStepName=INITIAL_STEP, region=region,
                                           distributionType=UNIFORM,
                                           crossSectionDistribution=CONSTANT_THROUGH_THICKNESS,
                                           magnitudes=(specimen_temperature,))
        self._provided_arguments_dict = {
            TEMPERATURE_FIELD_NAME: initial_temperature_field
        }
