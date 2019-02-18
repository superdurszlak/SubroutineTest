from src.builders.base_builder import BaseBuilder
from src.builders import *


class UserMaterialBuilder(BaseBuilder):
    def __init__(self):
        super(UserMaterialBuilder, self).__init__()
        self._required_arguments = [
            MATERIAL_TEMPLATE,
            MATERIAL_NAME,
            MODEL_NAME
        ]
        self._provided_arguments = []
        self._provided_arguments_dict = {}

    def _build(self, **kwargs):
        pass


