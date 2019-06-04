import mesh
from abaqus import *
from abaqusConstants import *

from src.builders import *
from src.builders.base_builder import BaseBuilder


class CylindricalSpecimenPartBuilder(BaseBuilder):
    def __init__(self):
        super(CylindricalSpecimenPartBuilder, self).__init__()
        self._required_arguments = [
            MODEL_NAME,
            SKETCH_NAME,
            TARGET_MATERIAL_NAME,
            MESH_EDGE_LENGTH
        ]
        self._provided_arguments = [
            FULL_VOLUME_SET,
            PART_NAME
        ]

    def _build(self, **kwargs):
        model_name = kwargs[MODEL_NAME]
        sketch_name = kwargs[SKETCH_NAME]
        material_name = kwargs[TARGET_MATERIAL_NAME]
        mesh_edge_length = kwargs[MESH_EDGE_LENGTH]
        part_name = 'Specimen'
        set_name = 'Specimen_Volume'
        section_name = 'Specimen_Section'
        self.__build_geometry(model_name, part_name, sketch_name)
        self.__assign_material(material_name, model_name, part_name, section_name, set_name)
        self.__create_mesh(mesh_edge_length, model_name, part_name)
        self.__create_reference_point(model_name, part_name)
        self._provided_arguments_dict[PART_NAME] = part_name
        self._provided_arguments_dict[FULL_VOLUME_SET] = set_name

    @staticmethod
    def __assign_material(material_name, model_name, part_name, section_name, set_name):
        mdb.models[model_name].HomogeneousSolidSection(
            name=section_name,
            material=material_name,
            thickness=None)
        part = mdb.models[model_name].parts[part_name]
        cells = part.cells.getSequenceFromMask(mask=('[#1 ]',), )
        region = part.Set(cells=cells, name=set_name)
        part.SectionAssignment(
            region=region,
            sectionName=section_name,
            offset=0.0,
            offsetType=MIDDLE_SURFACE,
            offsetField='',
            thicknessAssignment=FROM_SECTION)

    @staticmethod
    def __build_geometry(model_name, part_name, sketch_name):
        sketch = mdb.models[model_name].sketches[sketch_name]
        part = mdb.models[model_name].Part(name=part_name, dimensionality=THREE_D,
                                           type=DEFORMABLE_BODY)
        part.BaseSolidRevolve(sketch=sketch, angle=360.0, flipRevolveDirection=OFF)

    @staticmethod
    def __create_mesh(mesh_edge_length, model_name, part_name):
        part = mdb.models[model_name].parts[part_name]
        cells = part.cells.getSequenceFromMask(mask=('[#1 ]',), )
        regions = (cells,)
        part.seedPart(size=mesh_edge_length, minSizeFactor=0.1)
        elem_type_1 = mesh.ElemType(elemCode=C3D8T, elemLibrary=EXPLICIT,
                                    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
        elem_type_2 = mesh.ElemType(elemCode=C3D6T, elemLibrary=EXPLICIT,
                                    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
        elem_type_3 = mesh.ElemType(elemCode=C3D4T, elemLibrary=EXPLICIT,
                                    secondOrderAccuracy=OFF, distortionControl=DEFAULT)
        part.setElementType(
            regions=regions,
            elemTypes=(elem_type_1, elem_type_2, elem_type_3))
        part.generateMesh()

    @staticmethod
    def __create_reference_point(model_name, part_name):
        part = mdb.models[model_name].parts[part_name]
        edges = part.edges
        part.ReferencePoint(point=part.InterestingPoint(edge=edges[0], rule=CENTER))
