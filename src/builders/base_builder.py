import abc


class BaseBuilder:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._next_builder = None
        self._required_arguments = []
        self._provided_arguments = []
        self._provided_arguments_dict = {}

    @property
    def required_arguments(self):
        subsequent_required = self.next_builder.required_arguments if self.next_builder is not None else []
        not_provided = [arg for arg in subsequent_required if arg not in self._provided_arguments]
        return self._required_arguments + not_provided

    @property
    def next_builder(self):
        """
        Next builder getter

        :return: Next builder
        """
        return self._next_builder

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
        missing_arguments = [arg for arg in self.required_arguments if arg not in kwargs.keys()]
        if len(missing_arguments) > 0:
            raise KeyError("Missing required arguments: %s" % missing_arguments)
        self._build(**kwargs)
        kwargs = dict(kwargs, **self._provided_arguments_dict)
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
