
class Node:
    def __init__( self, nombre, apellido, id ):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.next = None
    
    def getId( self ):
        return self.id

    def imprimeDatos( self ):
        print( self.nombre, self.apellido, self.id )