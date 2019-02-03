import abc
from Tkinter import Frame


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
        if not isinstance(frame, Frame):
            raise TypeError('frame argument must be of type Tkinter.Frame, but %s was found' % type(frame))
        self.frame = frame
        self._configure()

    @abc.abstractmethod
    def _configure(self):
        """
        Configure UI controls for handler
        :return: None
        """
        pass
