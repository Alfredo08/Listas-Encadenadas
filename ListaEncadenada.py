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
        if self.head == None:
            return "La lista está vacía, no se puede eliminar algún nodo."
        aux = self.head
        if self.head.getId() == id:
            self.head = self.head.next
            aux.next = None
            return "Nodo eliminado exitosamente."
        else:
            prevAux = aux
            while aux.next != None:
                prevAux = aux
                aux = aux.next
                if aux.getId() == id:
                    prevAux.next = aux.next
                    aux.next = None
                    return "Nodo eliminado exitosamente."

    def buscaNodo( self, id ):
        aux = self.head
        while aux != None:
            if aux.getId() == id:
                return aux
            aux = aux.next
        return None

    def insertaNodoEnPosicion( self, nuevoNodo, indice ):
        pass
        # Hacer un conteo de los nodo actuales en la lista
        # Validar el índice contra el conteo. 
        # En caso en el que el índice es mayor al conteo, retorno None
        # De lo contrario insertar el nodo y retornar un mensaje de éxito
