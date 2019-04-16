from abaqus import *
from abaqusConstants import *

from src.builders.base_builder import BaseBuilder
from src.builders import *


class UserMaterialBuilder(BaseBuilder):
    def __init__(self):
        super(UserMaterialBuilder, self).__init__()
        self._required_arguments = [
            MATERIAL_TEMPLATE,
            TARGET_MATERIAL_NAME,
            MODEL_NAME
        ]
        self._provided_arguments = [
            USER_SUBROUTINE
        ]

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME]
        material_name = kwargs[TARGET_MATERIAL_NAME]
        material_template = kwargs[MATERIAL_TEMPLATE]
        density = material_template.density
        elastic_modulus = material_template.elastic_modulus
        poisson_ratio = material_template.poisson_ratio
        thermal_conductivity = material_template.thermal_conductivity
        heat_capacity = material_template.heat_capacity
        inelastic_heat_fraction = material_template.inelastic_heat_fraction
        user_variables = material_template.user_variables
        user_variables = tuple([(v, ) for v in user_variables])
        # TODO: complete material generation
        mdb.models[model_name].Material(name=material_name)
        mdb.models[model_name].materials[material_name].Density(table=((density, ), ))
        mdb.models[model_name].materials[material_name].Elastic(table=((elastic_modulus, poisson_ratio), ))
        mdb.models[model_name].materials[material_name].Plastic(hardening=USER, table=user_variables)
        mdb.models[model_name].materials[material_name].Conductivity(table=((thermal_conductivity, ), ))
        mdb.models[model_name].materials[material_name].InelasticHeatFraction(fraction=inelastic_heat_fraction)
        mdb.models[model_name].materials[material_name].SpecificHeat(table=((heat_capacity, ), ))
        self._provided_arguments_dict = {
            USER_SUBROUTINE: material_template.subroutine_path
        }


