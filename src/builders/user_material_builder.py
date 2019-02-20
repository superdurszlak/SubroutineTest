from src.builders.base_builder import BaseBuilder
from src.builders import *


class UserMaterialBuilder(BaseBuilder):
    def __init__(self):
        super(UserMaterialBuilder, self).__init__()
        self._required_arguments = [
            MATERIAL_TEMPLATE,
            MATERIAL_NAME,
            MODEL_NAME
        ]
        self._provided_arguments = []
        self._provided_arguments_dict = {}

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME]
        material_name = kwargs[MATERIAL_NAME]
        material_template = kwargs[MATERIAL_TEMPLATE]
        # TODO: complete material generation
        mdb.models['Model-3'].Material(name='Material-2')
        mdb.models['Model-3'].materials['Material-2'].Density(table=((23.0, ), ))
        mdb.models['Model-3'].materials['Material-2'].Elastic(table=((123.0, 0.4), ))
        mdb.models['Model-3'].materials['Material-2'].Plastic(hardening=USER, table=((
            33.0, ), (44.0, ), (55.0, )))
        mdb.models['Model-3'].materials['Material-2'].Conductivity(table=((123.0, ), ))
        mdb.models['Model-3'].materials['Material-2'].InelasticHeatFraction()
        mdb.models['Model-3'].materials['Material-2'].SpecificHeat(table=((312.0, ), ))


