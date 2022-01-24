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

    def longitud( self ):
        aux = self.head
        cont = 0
        while aux != None:
            cont += 1
            aux = aux.next
        return cont

    def insertaNodoEnPosicion( self, nuevoNodo, indice ):
        if indice <= self.longitud():
            if indice == 0:
                nuevoNodo.next = self.head
                self.head = nuevoNodo
            else:
                aux = self.head
                prev = aux
                x = 0
                while x < indice:
                    prev = aux
                    aux = aux.next
                    x += 1
                prev.next = nuevoNodo
                nuevoNodo.next = aux
        else:
            return "Indice inválido."
    
    def esListaCircular( self ):
        if self.head == None:
            return False
        else:
            aux1 = self.head
            aux2 = self.head
            while aux2.next != None:
                aux1 = aux1.next
                aux2 = aux2.next.next
                if aux1 == aux2:
                    return True   
                if aux2 == None:
                    return False
            return False
                

