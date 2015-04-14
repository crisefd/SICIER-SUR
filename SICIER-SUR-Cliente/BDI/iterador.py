#!/usr/bin/python

# iterator.py
import RegistrosIterador

class iterador(RegistrosIterador.RegistrosIterador):
   def __init__(self,registrosEntrantes):
      self.x = -1
      self.registros=registrosEntrantes

   def next(self):
      self.x += 1
      return self.registros[self.x]
   
   def hasNext(self):
	  if self.x+1<len(self.registros):
		  return True
	  return False

   def first(self):
	  if len(self.registros)>0:
		  return self.registros[0]
	  return 'vacio'		  

   def __iter__(self):
      return self
   def getLength(self):
	   return len(self.registros)
