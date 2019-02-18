from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class FlatSpecimenSketchBuilder(BaseBuilder):
    def __init__(self):
        super(FlatSpecimenSketchBuilder, self).__init__()
        self._required_arguments = [
            GRIP_LENGTH,
            GRIP_WIDTH,
            TAPER_LENGTH,
            REDUCED_LENGTH,
            REDUCED_WIDTH,
            MODEL_NAME
        ]
        self._provided_arguments = [
            SKETCH_NAME
        ]

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME]
        grip_length = kwargs[GRIP_LENGTH]
        grip_width = kwargs[GRIP_WIDTH]
        reduced_length = kwargs[REDUCED_LENGTH]
        reduced_width = kwargs[REDUCED_WIDTH]
        taper_length = kwargs[TAPER_LENGTH]
        sketch_name = 'Specimen_Sketch'
        self.__create_sketch(model_name, grip_length, grip_width, taper_length, reduced_length, reduced_width,
                             sketch_name)
        self._provided_arguments_dict[SKETCH_NAME] = sketch_name

    def __create_sketch(self, model_name, grip_length, grip_width, taper_length, reduced_length, reduced_width,
                        sketch_name):
        sketch = mdb.models[model_name].ConstrainedSketch(name=sketch_name, sheetSize=0.2)
        self.__create_lines(sketch)
        self.__create_symmetry_constrains(sketch)
        self.__create_dimensions(sketch, grip_length, grip_width, taper_length, reduced_length,
                                 reduced_width)

    @staticmethod
    def __create_lines(sketch):
        geometry = sketch.geometry
        sketch.ConstructionLine(point1=(0.0, 0.0), angle=0.0)
        sketch.HorizontalConstraint(entity=geometry[2], addUndoState=False)
        sketch.ConstructionLine(point1=(0.0, 0.0), angle=90.0)
        sketch.VerticalConstraint(entity=geometry[3], addUndoState=False)
        sketch.Line(point1=(-1e-2, 2e-2), point2=(-1e-2, 3e-2))
        sketch.VerticalConstraint(entity=geometry[4], addUndoState=False)
        sketch.Line(point1=(-1e-2, 3e-2), point2=(1e-2, 3e-2))
        sketch.HorizontalConstraint(entity=geometry[5], addUndoState=False)
        sketch.PerpendicularConstraint(entity1=geometry[4], entity2=geometry[5], addUndoState=False)
        sketch.Line(point1=(1e-2, 3e-2), point2=(1e-2, 2e-2))
        sketch.VerticalConstraint(entity=geometry[6], addUndoState=False)
        sketch.PerpendicularConstraint(entity1=geometry[5], entity2=geometry[6], addUndoState=False)
        sketch.Line(point1=(-1e-2, -2e-2), point2=(-1e-2, -3e-2))
        sketch.VerticalConstraint(entity=geometry[7], addUndoState=False)
        sketch.Line(point1=(-1e-2, -3e-2), point2=(1e-2, -3e-2))
        sketch.HorizontalConstraint(entity=geometry[8], addUndoState=False)
        sketch.PerpendicularConstraint(entity1=geometry[7], entity2=geometry[8], addUndoState=False)
        sketch.Line(point1=(1e-2, -3e-2), point2=(1e-2, -2e-2))
        sketch.VerticalConstraint(entity=geometry[9], addUndoState=False)
        sketch.PerpendicularConstraint(entity1=geometry[8], entity2=geometry[9], addUndoState=False)
        sketch.Line(point1=(-5e-3, 1e-2), point2=(-5e-3, -1e-2))
        sketch.VerticalConstraint(entity=geometry[10], addUndoState=False)
        sketch.Line(point1=(5e-3, 1e-2), point2=(5e-3, -1e-2))
        sketch.VerticalConstraint(entity=geometry[11], addUndoState=False)
        sketch.ArcByStartEndTangent(point1=(-5e-3, -1e-2), point2=(-1e-2, -2e-2), entity=geometry[10])
        sketch.ArcByStartEndTangent(point1=(5e-3, -1e-2), point2=(1e-2, -2e-2), entity=geometry[11])
        sketch.ArcByStartEndTangent(point1=(5e-3, 1e-2), point2=(1e-2, 2e-2), entity=geometry[11])
        sketch.ArcByStartEndTangent(point1=(-5e-3, 1e-2), point2=(-1e-2, 2e-2), entity=geometry[10])

    @staticmethod
    def __create_symmetry_constrains(sketch):
        geometry, vertices = sketch.geometry, sketch.vertices
        sketch.SymmetryConstraint(entity1=vertices[12], entity2=vertices[15], symmetryAxis=geometry[2])
        sketch.SymmetryConstraint(entity1=vertices[13], entity2=vertices[14], symmetryAxis=geometry[2])
        sketch.SymmetryConstraint(entity1=vertices[11], entity2=vertices[10], symmetryAxis=geometry[2])
        sketch.SymmetryConstraint(entity1=vertices[9], entity2=vertices[8], symmetryAxis=geometry[2])
        sketch.SymmetryConstraint(entity1=vertices[4], entity2=vertices[0], symmetryAxis=geometry[2])
        sketch.SymmetryConstraint(entity1=vertices[7], entity2=vertices[3], symmetryAxis=geometry[2])
        sketch.SymmetryConstraint(entity1=vertices[5], entity2=vertices[1], symmetryAxis=geometry[2])
        sketch.SymmetryConstraint(entity1=vertices[6], entity2=vertices[2], symmetryAxis=geometry[2])
        sketch.SymmetryConstraint(entity1=vertices[13], entity2=vertices[12], symmetryAxis=geometry[3])
        sketch.SymmetryConstraint(entity1=vertices[14], entity2=vertices[15], symmetryAxis=geometry[3])
        sketch.SymmetryConstraint(entity1=vertices[11], entity2=vertices[9], symmetryAxis=geometry[3])
        sketch.SymmetryConstraint(entity1=vertices[10], entity2=vertices[8], symmetryAxis=geometry[3])
        sketch.SymmetryConstraint(entity1=vertices[7], entity2=vertices[4], symmetryAxis=geometry[3])
        sketch.SymmetryConstraint(entity1=vertices[3], entity2=vertices[0], symmetryAxis=geometry[3])
        sketch.SymmetryConstraint(entity1=vertices[6], entity2=vertices[5], symmetryAxis=geometry[3])
        sketch.SymmetryConstraint(entity1=vertices[2], entity2=vertices[1], symmetryAxis=geometry[3])
        pass

    @staticmethod
    def __create_dimensions(sketch, grip_length, grip_width, taper_length, reduced_length, reduced_width):
        vertices = sketch.vertices
        sketch.VerticalDimension(vertex1=vertices[3], vertex2=vertices[2], textPoint=(1.5e-2, 3e-2), value=grip_length)
        sketch.HorizontalDimension(vertex1=vertices[1], vertex2=vertices[2], textPoint=(5e-3, 3.5e-2), value=grip_width)
        sketch.VerticalDimension(vertex1=vertices[10], vertex2=vertices[11], textPoint=(1.5e-2, 5e-3),
                                 value=reduced_length)
        sketch.HorizontalDimension(vertex1=vertices[10], vertex2=vertices[8], textPoint=(0.0, 1.5e-2),
                                   value=reduced_width)
        sketch.VerticalDimension(vertex1=vertices[10], vertex2=vertices[2], textPoint=(1.5e-2, 1.5e-2),
                                 value=grip_length + taper_length)
