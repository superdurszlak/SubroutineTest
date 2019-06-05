from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_border_conditions_builder import BaseBorderConditionsBuilder


class Compression3DBorderConditionsBuilder(BaseBorderConditionsBuilder):
    def __init__(self):
        super(Compression3DBorderConditionsBuilder, self).__init__()
        self._required_arguments = [
            FIXED_SET,
            MOVABLE_SET,
            MODEL_NAME,
            TOOL_LOWER_INSTANCE_NAME,
            TOOL_UPPER_INSTANCE_NAME,
            STEP_NAME,
            TOOL_DISPLACEMENT,
            SPECIMEN_TEMPERATURE
        ]
        self._provided_arguments = [
            ENCASTRE_BC,
            DISPLACEMENT_BC
        ]

    def _build(self, **kwargs):
        encastre_bc = 'Encastre_BC'
        displacement_bc = 'Displacement_BC'
        upper_tool_temp_bc = 'Upper_Tool_Temp_BC'
        lower_tool_temp_bc = 'Lower_Tool_Temp_BC'
        temperature = kwargs[SPECIMEN_TEMPERATURE]
        model_name = kwargs[MODEL_NAME]
        upper_tool_name = kwargs[TOOL_UPPER_INSTANCE_NAME]
        lower_tool_name = kwargs[TOOL_LOWER_INSTANCE_NAME]
        fixed_grip_set = kwargs[FIXED_SET]
        movable_grip_set = kwargs[MOVABLE_SET]
        step_name = kwargs[STEP_NAME]
        grip_displacement = kwargs[TOOL_DISPLACEMENT]

        self._create_encastre_bc(model_name, lower_tool_name, fixed_grip_set, encastre_bc)
        self._create_displacement_bc(model_name, upper_tool_name, movable_grip_set, displacement_bc, grip_displacement,
                                     step_name)
        self._create_temperature_bc(model_name, upper_tool_name, movable_grip_set, upper_tool_temp_bc, temperature,
                                    step_name)
        self._create_temperature_bc(model_name, lower_tool_name, fixed_grip_set, lower_tool_temp_bc, temperature,
                                    step_name)

        self._provided_arguments_dict = {
            ENCASTRE_BC: encastre_bc,
            DISPLACEMENT_BC: displacement_bc
        }

    @staticmethod
    def _create_temperature_bc(model_name, tool_name, set_name, bc_name, tool_temperature,
                               step_name):
        root_assembly = mdb.models[model_name].rootAssembly
        region = root_assembly.instances[tool_name].sets[set_name]
        mdb.models[model_name].TemperatureBC(name=bc_name, createStepName=step_name, region=region, fixed=OFF,
                                             distributionType=UNIFORM, fieldName='', magnitude=tool_temperature,
                                             amplitude=UNSET)
