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
