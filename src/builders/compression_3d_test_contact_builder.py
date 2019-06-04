from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class Compression3DTestContactBuilder(BaseBuilder):
    def __init__(self):
        super(Compression3DTestContactBuilder, self).__init__()
        self._required_arguments = [
            FRICTION_COEFFICIENT,
            MODEL_NAME
        ]
        self._provided_arguments = []

    def _build(self, **kwargs):
        friction_coefficient = kwargs[FRICTION_COEFFICIENT]
        model_name = kwargs[MODEL_NAME]
        contact_properties = 'Contact_Properties'
        contact_definition = 'Contact_Definition'
        initial_step = 'Initial'
        mdb.models[model_name].ContactProperty(contact_properties)
        mdb.models[model_name].interactionProperties[contact_properties].TangentialBehavior(
            formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF,
            pressureDependency=OFF, temperatureDependency=OFF, dependencies=0,
            table=((friction_coefficient,),), shearStressLimit=None, maximumElasticSlip=FRACTION,
            fraction=0.005, elasticSlipStiffness=None)
        mdb.models[model_name].ContactExp(name=contact_definition, createStepName=initial_step)
        mdb.models[model_name].interactions[contact_definition].includedPairs.setValuesInStep(
            stepName=initial_step, useAllstar=ON)
        mdb.models[model_name].interactions[contact_definition].contactPropertyAssignments.appendInStep(
            stepName=initial_step, assignments=((GLOBAL, SELF, contact_properties),))

