from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class DynamicStepBuilder(BaseBuilder):
    def __init__(self):
        super(DynamicStepBuilder, self).__init__()
        self._required_arguments = [
            MODEL_NAME,
            DISPLACEMENT_DURATION
        ]
        self._provided_arguments = [
            STEP_NAME
        ]

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME]
        displacement_duration = kwargs[DISPLACEMENT_DURATION]
        step_name = 'Compression_step'
        mdb.models[model_name].TempDisplacementDynamicsStep(name=step_name, previous='Initial',
                                                            timePeriod=displacement_duration)
        self._provided_arguments_dict = {
            STEP_NAME: step_name
        }
