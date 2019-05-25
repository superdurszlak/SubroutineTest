from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class CylindricalSpecimenSketchBuilder(BaseBuilder):
    def __init__(self):
        super(CylindricalSpecimenSketchBuilder, self).__init__()
        self._required_arguments = [
            SPECIMEN_BASE_RADIUS,
            SPECIMEN_LENGTH,
            MODEL_NAME,
        ]
        self._provided_arguments = [
            SKETCH_NAME
        ]

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME]
        specimen_length = kwargs[SPECIMEN_LENGTH]
        specimen_radius = kwargs[SPECIMEN_BASE_RADIUS]
        sketch_name = 'Specimen_Sketch'
        self.__create_sketch(model_name, specimen_length, specimen_radius, sketch_name)
        self._provided_arguments_dict[SKETCH_NAME] = sketch_name

    def __create_sketch(self, model_name, specimen_length, specimen_radius, sketch_name):
        sketch = mdb.models[model_name].ConstrainedSketch(name=sketch_name, sheetSize=0.2)
        self.__create_rectangle(sketch)
        self.__create_dimensions(sketch, specimen_length, specimen_radius)

    @staticmethod
    def __create_rectangle(sketch):
        geometry = sketch.geometry
        vertices = sketch.vertices
        sketch.ConstructionLine(point1=(0.0, 0.0), angle=90.0)
        sketch.VerticalConstraint(entity=geometry[2], addUndoState=False)
        sketch.rectangle(point1=(0.0, 0.0), point2=(0.01, 0.01))
        sketch.CoincidentConstraint(entity1=vertices[0], entity2=geometry[2], addUndoState=False)

    @staticmethod
    def __create_dimensions(sketch, specimen_length, specimen_radius):
        vertices = sketch.vertices
        sketch.ObliqueDimension(vertex1=vertices[1], vertex2=vertices[2], textPoint=(0.04, 0.03), value=specimen_radius)
        sketch.ObliqueDimension(vertex1=vertices[2], vertex2=vertices[3], textPoint=(0.04, 0.05), value=specimen_length)


