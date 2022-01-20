from Node import Node
from ListaEncadenada import ListaEncadenada

listaPersonas = ListaEncadenada()

persona1 = Node( "Alex", "Martinez", 123 )
persona2 = Node( "Martha", "Sanchez", 456 )
persona3 = Node( "Miguel", "Lopez", 789 )

listaPersonas.insertarNodo( persona1 )
listaPersonas.insertarNodo( persona2 )
listaPersonas.insertarNodo( persona3 )

listaPersonas.imprimeLista()
