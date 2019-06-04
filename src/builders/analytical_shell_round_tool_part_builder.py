from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class AnalyticalShellRoundToolPartBuilder(BaseBuilder):
    def __init__(self):
        super(AnalyticalShellRoundToolPartBuilder, self).__init__()
        self._required_arguments = [
            TOOL_RADIUS,
            MODEL_NAME
        ]
        self._provided_arguments = [
            TOOL_PART_NAME
        ]

    def _build(self, **kwargs):
        tool_radius = kwargs[TOOL_RADIUS]
        model_name = kwargs[MODEL_NAME]
        part_name = "Tool"
        sketch_name = "Tool_sketch"
        self.__create_sketch(model_name, sketch_name, tool_radius)
        self.__create_part(model_name, sketch_name, part_name)

        self._provided_arguments_dict = {
            TOOL_PART_NAME: part_name
        }

    @staticmethod
    def __create_sketch(model_name, sketch_name, tool_radius):
        sketch = mdb.models[model_name].ConstrainedSketch(name=sketch_name, sheetSize=0.1)
        geometry, vertices = sketch.geometry, sketch.vertices
        sketch.sketchOptions.setValues(decimalPlaces=3)
        sketch.setPrimaryObject(option=STANDALONE)
        sketch.ConstructionLine(point1=(0.0, -0.05), point2=(0.0, 0.05))
        sketch.FixedConstraint(entity=geometry[2])
        sketch.Line(point1=(0.0, 0.0), point2=(tool_radius, 0.0))
        sketch.HorizontalConstraint(entity=geometry[3], addUndoState=False)
        sketch.PerpendicularConstraint(entity1=geometry[2], entity2=geometry[3], addUndoState=False)
        sketch.CoincidentConstraint(entity1=vertices[0], entity2=geometry[2], addUndoState=False)

    @staticmethod
    def __create_part(model_name, sketch_name, part_name):
        sketch = mdb.models[model_name].sketches[sketch_name]
        part = mdb.models[model_name].Part(name=part_name, dimensionality=THREE_D, type=ANALYTIC_RIGID_SURFACE)
        part.AnalyticRigidSurfRevolve(sketch=sketch)
        part = mdb.models[model_name].parts[part_name]
        vertices = part.vertices
        part.ReferencePoint(point=vertices[1])
        del mdb.models[model_name].sketches[sketch_name]
