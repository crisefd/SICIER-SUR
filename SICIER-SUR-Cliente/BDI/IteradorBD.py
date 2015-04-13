import RegistrosIterador
class Iterator(RegistrosIterador.RegistrosIterador):
        index = 0
        def __init__(self,registrosEntrantes):
            registros=registrosEntrantes;

        def hasNext():
            if(index < registros.length):
                return true
            return false

        def next():
            index=index+1
            return registros[index]
        def current():
            return registros[index]
        def first():
            return registros[0]

