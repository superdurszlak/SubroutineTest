import abc


class MaterialList:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def options(self):
        pass

    @abc.abstractmethod
    def subscribe(self, template):
        pass

    @abc.abstractmethod
    def remove(self, name):
        pass

    @abc.abstractmethod
    def find(self, name):
        pass
