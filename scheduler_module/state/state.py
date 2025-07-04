from __future__ import annotations
from abc import ABC, abstractmethod
import pykka


def abstractfunc(func):
    func.__isabstract__ = True
    return func


class Interface(type):

    def __init__(self, name, bases, namespace):
        for base in bases:
            must_implement = getattr(base, 'abstract_methods', [])
            class_methods = getattr(self, 'all_methods', [])
            for method in must_implement:
                if method not in class_methods:
                    err_str = """Can't create abstract class {name}!
                    {name} must implement abstract method {method} of class {base_class}!""".format(name=name,
                                                                                                    method=method,
                                                                                                    base_class=base.__name__)
                    raise TypeError(err_str)

    def __new__(metaclass, name, bases, namespace):
        namespace['abstract_methods'] = Interface._get_abstract_methods(namespace)
        namespace['all_methods'] = Interface._get_all_methods(namespace)
        cls = super().__new__(metaclass, name, bases, namespace)
        return cls

    def _get_abstract_methods(namespace):
        return [name for name, val in namespace.items() if callable(val) and getattr(val, '__isabstract__', False)]

    def _get_all_methods(namespace):
        return [name for name, val in namespace.items() if callable(val)]


@pykka.traversable
class State(metaclass=Interface):
    """
        Represents the state of the rover. Pretends to follow the state design pattern.
    """

    def __init__(self, name):
        self.context = None
        self.__name__ = name

    @abstractmethod
    def add_time(self, cell_origin, cell_to):
        pass

    def context(self):
        return self.context

    def set_context(self, context):
        self.context = context

    @abstractmethod
    def move(self, cell):
        pass

    @abstractmethod
    def battery_discharge(self):
        pass
