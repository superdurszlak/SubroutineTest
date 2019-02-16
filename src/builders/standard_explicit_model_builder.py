import mdb
from abaqus import *
from abaqusConstants import *

import config
from src.builders import *
from src.builders.base_builder import BaseBuilder


class StandardExplicitModelBuilder(BaseBuilder):
    def __init__(self):
        super(StandardExplicitModelBuilder, self).__init__()
        self._required_arguments = [MODEL_NAME]

    def _build(self, **kwargs):
        model_name = kwargs.get(MODEL_NAME)
        self._model = mdb.Model(name=model_name, description='', absoluteZero=config.ABSOLUTE_ZERO,
                                stefanBoltzmann=config.STEFAN_BOLTZMANN, modelType=STANDARD_EXPLICIT)
