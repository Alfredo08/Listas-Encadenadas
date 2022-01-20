from Node import Node

class ListaEncadenada:
    def __init__( self ):
        self.head = None
    
    def insertarNodo( self, nuevoNodo ):
        if self.head == None:
            self.head = nuevoNodo
        else:
            aux = self.head
            while aux.next != None:
                aux = aux.next
            aux.next = nuevoNodo
    
    def imprimeLista( self ):
        aux = self.head
        while aux != None:
            print( aux.nombre, aux.apellido, str(aux.id) )
            aux = aux.next
    
    def eliminaNodo( self, id ):
        pass
