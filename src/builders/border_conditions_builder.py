from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class BorderConditionsBuilder(BaseBuilder):
    def __init__(self):
        super(BorderConditionsBuilder, self).__init__()
        self._required_arguments = [
            FIXED_GRIP_SET,
            MOVABLE_GRIP_SET,
            MODEL_NAME,
            ASSEMBLY_NAME,
            STEP_NAME,
            GRIP_DISPLACEMENT
        ]
        self._provided_arguments = [
            ENCASTRE_BC,
            DISPLACEMENT_BC
        ]

    def _build(self, **kwargs):
        encastre_bc = 'Encastre_BC'
        displacement_bc = 'Displacement_BC'
        model_name = kwargs[MODEL_NAME]
        assembly_name = kwargs[ASSEMBLY_NAME]
        fixed_grip_set = kwargs[FIXED_GRIP_SET]
        movable_grip_set = kwargs[MOVABLE_GRIP_SET]
        step_name = kwargs[STEP_NAME]
        grip_displacement = kwargs[GRIP_DISPLACEMENT]

        self.__create_encastre_bc(model_name, assembly_name, fixed_grip_set, encastre_bc)
        self.__create_displacement_bc(model_name, assembly_name, movable_grip_set, displacement_bc, grip_displacement,
                                      step_name)

        self._provided_arguments_dict = {
            ENCASTRE_BC: encastre_bc,
            DISPLACEMENT_BC: displacement_bc
        }

    @staticmethod
    def __create_encastre_bc(model_name, assembly_name, fixed_grip_set, encastre_bc):
        root_assembly = mdb.models[model_name].rootAssembly
        region = root_assembly.instances[assembly_name].sets[fixed_grip_set]
        mdb.models[model_name].EncastreBC(name=encastre_bc, createStepName=INITIAL_STEP, region=region, localCsys=None)

    @staticmethod
    def __create_displacement_bc(model_name, assembly_name, movable_grip_set, displacement_bc, grip_displacement,
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
                                                                                   u2=grip_displacement)
