from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class Compression3DTestAssemblyBuilder(BaseBuilder):
    def __init__(self):
        super(Compression3DTestAssemblyBuilder, self).__init__()
        self._required_arguments = [
            PART_NAME,
            TOOL_PART_NAME,
            SPECIMEN_LENGTH,
            MODEL_NAME
        ]
        self._provided_arguments = [
            ASSEMBLY_NAME,
            TOOL_LOWER_INSTANCE_NAME,
            TOOL_UPPER_INSTANCE_NAME
        ]

    def _build(self, **kwargs):
        specimen_name = 'Assembly_%s' % kwargs[PART_NAME]
        upper_tool_name = 'Upper_%s' % kwargs[TOOL_PART_NAME]
        lower_tool_name = 'Lower_%s' % kwargs[TOOL_PART_NAME]
        model_name = kwargs[MODEL_NAME]
        specimen_part_name = kwargs[PART_NAME]
        specimen_lenght = kwargs[SPECIMEN_LENGTH]
        tool_part_name = kwargs[TOOL_PART_NAME]
        self.__create_assembly_instances(specimen_name, lower_tool_name, model_name, specimen_lenght,
                                         specimen_part_name, tool_part_name, upper_tool_name)
        self._provided_arguments_dict = {
            ASSEMBLY_NAME: specimen_name,
            TOOL_UPPER_INSTANCE_NAME: upper_tool_name,
            TOOL_LOWER_INSTANCE_NAME: lower_tool_name
        }

    @staticmethod
    def __create_assembly_instances(assembly_name, lower_tool_name, model_name, specimen_lenght,
                                    specimen_part_name, tool_part_name, upper_tool_name):
        root_assembly = mdb.models[model_name].rootAssembly
        root_assembly.DatumCsysByDefault(CARTESIAN)
        specimen = mdb.models[model_name].parts[specimen_part_name]
        tool = mdb.models[model_name].parts[tool_part_name]
        root_assembly.Instance(name=assembly_name, part=specimen, dependent=ON)
        root_assembly.Instance(name=upper_tool_name, part=tool, dependent=ON)
        root_assembly.Instance(name=lower_tool_name, part=tool, dependent=ON)
        root_assembly.translate(instanceList=(upper_tool_name,), vector=(0.0, specimen_lenght, 0.0))
