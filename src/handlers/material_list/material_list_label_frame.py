from Tkinter import LabelFrame

from src.handlers.material_list.material_list import MaterialList
from src.templates.user_model_template import UserModelTemplate


class MaterialListLabelFrame(LabelFrame, MaterialList):
    def __init__(self, **kw):
        self.choice_options = []
        super(MaterialListLabelFrame, self).__init__(**kw)

    def options(self):
        return self.choice_options

    def subscribe(self, template):
        if template.name in self.choice_options:
            raise KeyError('Template named %s already exists' % template.name)
        self.choice_options.append(template.name)

    def remove(self, name):
        if name in self.choice_options:
            self.choice_options.remove(name)
            for item in filter(lambda m: isinstance(m, UserModelTemplate) and m.name == name, self.winfo_children()):
                item.destroy()

    def find(self, name):
        if name in self.choice_options:
            items = filter(lambda m: isinstance(m, UserModelTemplate) and m.name == name, self.winfo_children())
            if len(items) > 0:
                return items[0]
            else:
                return None
