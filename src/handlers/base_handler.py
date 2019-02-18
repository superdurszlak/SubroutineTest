import abc


class BaseHandler:
    """
    Abstract class for specific frame handlers
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, frame):
        """
        Accepts single Tkinter.Frame object
        :param frame: Frame object to which UI controls will be bound
        """
        self.frame = frame
        self._configure()

    @abc.abstractmethod
    def _configure(self):
        """
        Configure UI controls for handler
        :return: None
        """
        pass
