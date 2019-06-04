from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_border_conditions_builder import BaseBorderConditionsBuilder


class FlatTensileBorderConditionsBuilder(BaseBorderConditionsBuilder):
    def __init__(self):
        super(FlatTensileBorderConditionsBuilder, self).__init__()
        self._required_arguments = [
            FIXED_SET,
            MOVABLE_SET,
            MODEL_NAME,
            ASSEMBLY_NAME,
            STEP_NAME,
            TOOL_DISPLACEMENT
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
        fixed_grip_set = kwargs[FIXED_SET]
        movable_grip_set = kwargs[MOVABLE_SET]
        step_name = kwargs[STEP_NAME]
        grip_displacement = kwargs[TOOL_DISPLACEMENT]

        self._create_encastre_bc(model_name, assembly_name, fixed_grip_set, encastre_bc)
        self._create_displacement_bc(model_name, assembly_name, movable_grip_set, displacement_bc, grip_displacement,
                                     step_name)

        self._provided_arguments_dict = {
            ENCASTRE_BC: encastre_bc,
            DISPLACEMENT_BC: displacement_bc
        }
