#Diseñar un algoritmo que elimine todas las vocales que se encuentren en una 
# lista de caracteres.

from lista import Lista
from random import randint 


lista_vocales = Lista()

for i in range(50):
    vocal = chr(randint(65, 90))
    lista_vocales.insertar(vocal)

lista_vocales.barrido()
print()
vocales = ['A', 'E', 'I', 'O', 'U']
lista_vocales.barrido_eliminando(vocales)

for vocal in vocales:
    while(lista_vocales.eliminar(vocal)is not None): #vamos a eliminar hasta que la funcion eliminar devuelva NONE
        continue

print('sin vocales')

lista_vocales.barrido()

