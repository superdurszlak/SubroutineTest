from abaqus import *
from abaqusConstants import *

import config
from src.builders import MODEL_NAME, STEP_NAME
from src.builders.base_builder import BaseBuilder


class DynamicFieldOutputRequestBuilder(BaseBuilder):
    def __init__(self):
        super(DynamicFieldOutputRequestBuilder, self).__init__()
        self._required_arguments = [
            MODEL_NAME,
            STEP_NAME
        ]

    def _build(self, **kwargs):
        output_name = 'Output_%s' % kwargs[MODEL_NAME]
        model_name = kwargs[MODEL_NAME]
        step_name = kwargs[STEP_NAME]
        mdb.models[model_name].FieldOutputRequest(
            name=output_name,
            createStepName=step_name,
            variables=(
                'S', 'SVAVG', 'PE',
                'PEVAVG', 'PEEQ', 'PEEQVAVG',
                'LE', 'ER', 'U', 'V', 'A', 'RF',
                'CSTRESS', 'NT', 'HFL', 'RFL',
                'EVF'),
            numIntervals=config.NUM_INTERVALS
        )
