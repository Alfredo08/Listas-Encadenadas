from Node import Node
from ListaEncadenada import ListaEncadenada

listaPersonas = ListaEncadenada()

persona1 = Node( "Alex", "Martinez", 123 )
persona2 = Node( "Martha", "Sanchez", 456 )
persona3 = Node( "Miguel", "Lopez", 789 )
persona4 = Node( "Alan", "Morales", 555 )

listaPersonas.insertarNodo( persona1 )
listaPersonas.insertarNodo( persona2 )
listaPersonas.insertarNodo( persona3 )
listaPersonas.insertarNodo( persona4 )

print( listaPersonas.eliminaNodo( 123 ) )

listaPersonas.imprimeLista()

#resultado = listaPersonas.buscaNodo( 555 )

#if resultado != None:
#    resultado.imprimeDatos()
#else:
#    print( "No se encontró ese id en la lista" )
