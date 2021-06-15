#Dada una lista de números enteros eliminar de estas los números primos

from lista import Lista
from random import randint

lista_num = Lista()

for i in range(10): #la cargamos
    num = (randint(1,10))
    lista_num.insertar(num)

def es_primo(numero): #funcion para saber si un numero es primo
    cantidad = 0 
    for i in range(1, numero+1):
        if (numero % i == 0 ):
            cantidad +=1
    return cantidad ==2   

print('lista original')
lista_num.barrido()

for i in range(lista_num.tamanio()):
    numero = (lista_num.obtener_elemento(i))
    if (es_primo(numero)):
        lista_num.eliminar(numero)

aux = []
tamanio_lista = lista_num.tamanio()
i = 0

while(i < tamanio_lista):
    numero = lista_num.obtener_elemento(i)
    if (es_primo(numero)): 
        lista_num.eliminar(numero)
        tamanio_lista -=1  
    else:
        i += 1 

print('lista sin primos', aux)
 

""" from lista import Lista
from random import randint

lista = Lista()

for i in range(5):
    lista.insertar(randint(1, 50))
    
lista.barrido()
print()

for i in range(lista.tamanio()):
    cantidad = 0
    if (i < lista.tamanio()):
        num = lista.obtener_elemento(i)
        if (num ==1):
            lista.eliminar(num)
        for j in range (2, num+1):
            if (num % j == 0):
                cantidad +=1
        if (cantidad == 1):
            lista.eliminar(num)


lista.barrido()
 """