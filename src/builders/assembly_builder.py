from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class AssemblyBuilder(BaseBuilder):
    def __init__(self):
        super(AssemblyBuilder, self).__init__()
        self._required_arguments = [
            PART_NAME,
            MODEL_NAME
        ]
        self._provided_arguments = [
            ASSEMBLY_NAME
        ]

    def _build(self, **kwargs):
        assembly_name = 'Assembly_%s' % kwargs[PART_NAME]
        model_name = kwargs[MODEL_NAME]
        part_name = kwargs[PART_NAME]
        root_assembly = mdb.models[model_name].rootAssembly
        root_assembly.DatumCsysByDefault(CARTESIAN)
        part = mdb.models[model_name].parts[part_name]
        root_assembly.Instance(name=assembly_name, part=part, dependent=ON)
        self._provided_arguments_dict = {
            ASSEMBLY_NAME: assembly_name
        }
        pass
