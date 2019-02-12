import abc


class BaseBuilder:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._next_builder = None
        self._required_arguments = []

    @property
    def required_arguments(self):
        subsequent_required = self.next_builder.required_arguments if self.next_builder is not None else []
        return self._required_arguments + subsequent_required

    @property
    def next_builder(self):
        """
        Next builder getter

        :return: Next builder
        """
        return self.next_builder

    @next_builder.setter
    def next_builder(self, builder):
        builder_type = type(builder)
        if not issubclass(builder_type, BaseBuilder):
            raise TypeError("Builder must be subtype of BaseBuilder")
        self._next_builder = builder

    def build(self, **kwargs):
        """
        Wrapper for class-specific _build method

        :param kwargs: keyword arguments. These may be specific to both current builder or its subsequent builders.
        :return: None
        """
        self._build(**kwargs)
        missing_arguments = [arg for arg in self.required_arguments if arg not in kwargs.keys()]
        if len(missing_arguments) > 0:
            raise KeyError("Missing required arguments: %s" % missing_arguments)
        if self.next_builder is not None:
            self.next_builder.build(**kwargs)

    @abc.abstractmethod
    def _build(self, **kwargs):
        """
        Class-specific method for building specific part of Abaqus model

        :param kwargs: custom parameters as keyword arguments
        :return:
        """
        pass
