import abc

from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class BaseBorderConditionsBuilder(BaseBuilder):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super(BaseBorderConditionsBuilder, self).__init__()

    @abc.abstractmethod
    def _build(self, **kwargs):
        pass

    @staticmethod
    def _create_encastre_bc(model_name, assembly_name, fixed_grip_set, encastre_bc):
        root_assembly = mdb.models[model_name].rootAssembly
        region = root_assembly.instances[assembly_name].sets[fixed_grip_set]
        mdb.models[model_name].EncastreBC(name=encastre_bc, createStepName=INITIAL_STEP, region=region, localCsys=None)

    @staticmethod
    def _create_displacement_bc(model_name, assembly_name, movable_grip_set, displacement_bc, grip_displacement,
                                 step_name):
        amplitude_name = 'Tabular_linear_amp'
        root_assembly = mdb.models[model_name].rootAssembly
        region = root_assembly.instances[assembly_name].sets[movable_grip_set]
        mdb.models[model_name].DisplacementBC(name=displacement_bc, createStepName=INITIAL_STEP,
                                              region=region, u1=SET, u2=SET, ur3=SET, amplitude=UNSET,
                                              distributionType=UNIFORM, fieldName='', localCsys=None)
        mdb.models[model_name].TabularAmplitude(name=amplitude_name, timeSpan=STEP,
                                                smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
        mdb.models[model_name].boundaryConditions[displacement_bc].setValuesInStep(stepName=step_name,
                                                                                   u1=0.0,
                                                                                   u2=grip_displacement,
                                                                                   u3=0.0,
                                                                                   ur1=0.0,
                                                                                   ur2=0.0,
                                                                                   ur3=0.0)
