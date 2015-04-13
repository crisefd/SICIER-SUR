import server.py
import cliente.py
from multiprocessing import Process


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None 

    def __call__(cls,*args,**kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance

class main(object):
	
	__metaclass__ = Singleton	
	
	Pserver = Process(target = server)
	Pserver.start()
	
	
	
	#Pcliente = Process(target = cliente)
	
	#Pcliente.start()
	
	
	
