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
