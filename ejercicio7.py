""" Implementar los algoritmos necesarios para resolver las siguientes tareas:
a. concatenar dos listas, una atrás de la otra;
b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;[113]
d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido """

from lista import Lista
from random import randint
lista_uno = Lista()
lista_dos = Lista()
lista_concatenada = Lista()

for i in range(5):
    lista_uno.insertar(i) #cargamos las dos listas
    lista_dos.insertar(randint(1,10))

print('lista uno')
lista_uno.barrido()
print()

print('lista dos')
lista_dos.barrido()
print()

cont_repetidos = 0

for i in range(lista_uno.tamanio()): #puntoA
    numero = (lista_dos.obtener_elemento(i)) 
    lista_uno.insertar(numero)


print('listas concatenadas una atras de la otra')
lista_uno.barrido()
print()

for i in range(lista_uno.tamanio()):#puntob
    numero = (lista_uno.obtener_elemento(i)) 
    lista_concatenada.insertar(numero)
    
print ('las dos listas concatenadas en una')
lista_concatenada.barrido()
print()

#for i in range(lista_dos.tamanio()): 
#    num = lista_dos.obtener_elemento(i)
#    if(lista_uno.busqueda(num) == -1):
       # lista_uno.insertar(num)
  #      cont_repetidos =+1 #puntoC

                
for i in range(lista_uno.tamanio()):
	num=lista_uno.obtener_elemento(i)
	pos = lista_dos.busqueda(num)
	if (pos != -1):
		cont_repetidos =+1
    	
while(lista_uno.tamanio()>0):#puntoD
    numero = (lista_uno.obtener_elemento(0)) 
    print('numero eliminado: ',numero)
    aux=lista_uno.eliminar(numero)
    
# lista_uno.barrido_eliminando(numero)
   
print('la cantidad de elementos repetidos son: ', cont_repetidos)
print('lista concatenada sin repetir')

lista_uno.barrido()    

# print('lista concatenada')
# lista_concatenada.barrido()    



    

   