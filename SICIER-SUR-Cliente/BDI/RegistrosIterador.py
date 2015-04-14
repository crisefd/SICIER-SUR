from abc import *
class RegistrosIterador():
	__metaclass__ = ABCMeta	
	@abstractmethod
	def hasNext(self):
		pass
	@abstractmethod
	def next(self):
		pass
	@abstractmethod
	def first(self):
		pass
	@abstractmethod
	def getLength(self):
		pass
