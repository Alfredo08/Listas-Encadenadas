from Node import Node
from ListaEncadenada import ListaEncadenada

listaPersonas = ListaEncadenada()

persona1 = Node( "Alex", "Martinez", 123 )
persona2 = Node( "Martha", "Sanchez", 456 )
persona3 = Node( "Miguel", "Lopez", 789 )
persona4 = Node( "Alan", "Morales", 555 )

persona5 = Node( "Julieta", "Rodriguez", 222 )

listaPersonas.insertarNodo( persona1 )
listaPersonas.insertarNodo( persona2 )
listaPersonas.insertarNodo( persona3 )
listaPersonas.insertarNodo( persona4 )

listaPersonas.insertaNodoEnPosicion( persona5, 4 )
persona5.next = persona5

print( listaPersonas.esListaCircular() )

listaPersonas.imprimeLista()
#resultado = listaPersonas.buscaNodo( 555 )

#if resultado != None:
#    resultado.imprimeDatos()
#else:
#    print( "No se encontró ese id en la lista" )
