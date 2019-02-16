import abc

from src.utils import is_positive_float


class BaseSimulationHandler:
    """
    Base class for all simulation handlers
    """

    def __init__(self):
        self._validator = None

    def populate(self, frame):
        """
        Clear frame object and populate it with handler's controls

        :param frame: Frame object to which UI controls will be bound
        :return: None
        """
        for child in frame.winfo_children():
            child.destroy()
        self._validator = frame.register(is_positive_float)
        self._populate(frame)

    @abc.abstractmethod
    def _populate(self, frame):
        """
        Class-specific inner implementation of populate method

        :param frame: Frame object to which UI controls will be bound
        :return: None
        """
        pass

    @abc.abstractproperty
    def parameters(self):
        """
        Dictionary of parameters relevant for this handler and possibly nested handlers
        :return: dictionary of parameters
        """
        pass

    @abc.abstractproperty
    def builders(self):
        """
        Get all builders relevant for this handler and possibly nested handlers
        :return: list of builders, with each builder tied to previous one as 'next_builder'
        """
        pass
