#Dada una lista de números enteros, implementar un algoritmo para dividir 
# dicha lista en dos, una que contenga los números pares y otra para los números impares.

from lista import Lista
from random import randint

lista_num = Lista()
lista_par = Lista()
lista_impar = Lista()

for i in range(50): #la cargamos
    num = (randint(1,100))
    lista_num.insertar(num)

print('lista original')
lista_num.barrido()

for i in range(lista_num.tamanio()):
    numero = (lista_num.obtener_elemento(i))
    if (numero % 2 == 0):
        lista_par.insertar(numero)
    else:
        lista_impar.insertar(numero)

print('lista de pares')
lista_par.barrido()

print('lista de impares')
lista_impar.barrido()
