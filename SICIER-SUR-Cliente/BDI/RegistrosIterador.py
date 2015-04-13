from abc import *
class RegistrosIterador():
    metaclass__ = ABCMeta
    @abstractmethod
    def hasNext():
        return
    @abstractmethod
    def next():
        return
    @abstractmethod
    def current():
        return
    @abstractmethod
    def first():
        return