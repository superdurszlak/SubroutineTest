import os
import tkFileDialog
from Tkinter import LabelFrame, Button, Frame, BOTTOM, LEFT, X

import config
from src.handlers.material_list.material_list import MaterialList
from src.templates.user_model_template import UserModelTemplate


class MaterialListLabelFrame(LabelFrame, MaterialList):
    def __init__(self, **kw):
        self.choice_options = []
        super(MaterialListLabelFrame, self).__init__(**kw)
        self._buttons_frame = Frame(self)
        self._buttons_frame.pack(side=BOTTOM, padx=config.FRAME_PADDING, pady=config.FRAME_PADDING, fill=X, expand=1)
        self._import_button = Button(self._buttons_frame, text="Import", command=self.__import)
        self._import_button.pack(side=LEFT, padx=config.ELEMENT_PADDING)
        self._export_button = Button(self._buttons_frame, text="Export all", command=self.__export)
        self._export_button.pack(side=LEFT, padx=config.ELEMENT_PADDING)

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

    def __import(self):
        files_to_import = tkFileDialog.askopenfilenames(
            parent=self,
            title='Choose files to import',
            initialdir=config.HOME_DIR,
            filetypes=(('JSON files', '*.json'),)
        )
        file_paths = self.tk.splitlist(files_to_import)
        for file_path in file_paths:
            UserModelTemplate.from_json(self, file_path)

    def __export(self):
        directory_to_export = tkFileDialog.askdirectory(
            parent=self,
            title='Choose target directory',
            initialdir=config.HOME_DIR
        )
        for name in self.options():
            file_name = '%s.json' % name
            file_path = os.path.join(directory_to_export, file_name)
            template = self.find(name)
            template.to_json(file_path)
