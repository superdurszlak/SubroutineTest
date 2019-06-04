from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class Compression3DTestSurfacesBuilder(BaseBuilder):
    def __init__(self):
        super(Compression3DTestSurfacesBuilder, self).__init__()
        self._required_arguments = [
            MODEL_NAME,
            TOOL_LOWER_INSTANCE_NAME,
            TOOL_UPPER_INSTANCE_NAME
        ]
        self._provided_arguments = [
            LOWER_TOOL_SURFACE,
            UPPER_TOOL_SURFACE
        ]

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME]
        tool_lower_instance_name = kwargs[TOOL_LOWER_INSTANCE_NAME]
        tool_upper_instance_name = kwargs[TOOL_UPPER_INSTANCE_NAME]
        upper_tool_surface = 'Surface_%s' % tool_upper_instance_name
        lower_tool_surface = 'Surface_%s' % tool_lower_instance_name

        root_assembly = mdb.models[model_name].rootAssembly
        lower_tool_face = root_assembly.instances[tool_lower_instance_name].faces.getSequenceFromMask(mask=('[#1 ]',), )
        root_assembly.Surface(side1Faces=lower_tool_face, name=lower_tool_surface)
        root_assembly = mdb.models[model_name].rootAssembly
        upper_tool_face = root_assembly.instances[tool_upper_instance_name].faces.getSequenceFromMask(mask=('[#1 ]',), )
        root_assembly.Surface(side2Faces=upper_tool_face, name=upper_tool_surface)

        self._provided_arguments_dict = {
            LOWER_TOOL_SURFACE: lower_tool_surface,
            UPPER_TOOL_SURFACE: upper_tool_surface
        }

