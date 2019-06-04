import sys

from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class StaticStepBuilder(BaseBuilder):
    def __init__(self):
        super(StaticStepBuilder, self).__init__()
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
        step_name = 'Tension_step'
        step_initial = displacement_duration * 1e-1
        step_minimum = step_initial * 1e-8
        max_num_inc = sys.maxint
        max_delta_t = 10e0
        mdb.models[model_name].CoupledTempDisplacementStep(name=step_name, previous=INITIAL_STEP,
                                                           timePeriod=displacement_duration, maxNumInc=max_num_inc,
                                                           initialInc=step_initial, minInc=step_minimum,
                                                           maxInc=displacement_duration, deltmx=max_delta_t)
        self._provided_arguments_dict = {
            STEP_NAME: step_name
        }
