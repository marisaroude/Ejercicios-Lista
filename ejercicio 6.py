
from lista import Lista

lista_superheroes = Lista()

superheroes = [
                {'nombre': 'Linterna Verde','aparicion': 1999 ,'casa': 'DC' ,'biografia':'espada'},
                {'nombre': 'Wolverine','aparicion': 1974 ,'casa': 'Marvel' ,'biografia':'traje'},
                {'nombre': 'Deadpool','aparicion': 1960 ,'casa': 'Marvel' ,'biografia':'espada'},
                {'nombre': 'Dr Strange','aparicion': 1962 ,'casa': 'DC' ,'biografia':'armadura'},
                {'nombre': 'Capitana Marvel','aparicion': 1998 ,'casa': 'Marvel' ,'biografia':'armadura'},
                {'nombre': 'Mujer Maravilla','aparicion': 1979 ,'casa': 'DC' ,'biografia':'espada'},
                {'nombre': 'Flash','aparicion': 1980 ,'casa': 'DC' ,'biografia':'espada'},
                {'nombre': 'Star-Lord','aparicion': 1961,'casa': 'Marvel' ,'biografia':'traje'}
            ]

for superheroe in superheroes:
    lista_superheroes.insertar(superheroe, 'nombre')

lista_superheroes.barrido()
print()
#Punto A
lista_superheroes.eliminar('Linterna Verde','nombre')

#Punto B
pos = lista_superheroes.busqueda('Wolverine','nombre')
if (pos > -1 ):
    print('El año de aparicion de Wolverine es ',lista_superheroes.obtener_elemento(pos)['aparicion'])

#Punto C . cambiar la casa de Dr. Strange a Marvel;
pos = lista_superheroes.busqueda('Dr Strange','nombre')
if (pos > -1 ):
    lista_superheroes.obtener_elemento(pos)['casa'] = 'Marvel'


cont_traje = ''
cont_armadura = ''
cont_marvel = 0
cont_dc = 0
cont_s = ''
cont_b = ''
cont_m = ''

for i in range(lista_superheroes.tamanio()):
    pos = lista_superheroes.obtener_elemento(i)
    #Punto D
    if (pos['biografia'] == 'traje'):
        cont_traje +=(pos['nombre']+ '  ' )
    elif (pos['biografia'] == 'armadura'):
        cont_armadura +=(pos['nombre']+'  ')
    
    #Punto E
    if (pos ['aparicion'] < 1963):
        print ('Superheroe cuya fecha de aparicion es anterior a 1963: ', pos['nombre'],'del comic: ',pos['casa'])

    #Punto I
    if (pos['casa'] == 'Marvel'):
        cont_marvel += 1  
    else:
        cont_dc += 1

    #Punto F
    if (pos['nombre'][0] == 'S'):
        cont_s += (pos['nombre']+'  ')
    elif (pos['nombre'][0] == 'B'):
        cont_b += (pos['nombre']+'  ')
    elif(pos['nombre'][0] == 'M'):
        cont_m += (pos['nombre']+'  ')


#Punto F
pos = lista_superheroes.busqueda('Capitana Marvel','nombre')
if (pos > -1 ):
    print('La casa a la que pertenece Capìtana Marvel es ',lista_superheroes.obtener_elemento(pos)['casa'])
pos = lista_superheroes.busqueda('Mujer Maravilla','nombre')
if (pos > -1 ):
    print('La casa a la que pertenece Mujer Maravilla es ',lista_superheroes.obtener_elemento(pos)['casa'])

#Punto G
pos = lista_superheroes.busqueda('Flash','nombre')
if (pos > -1 ):
    print('Informacion de flash: ',lista_superheroes.obtener_elemento(pos))

pos = lista_superheroes.busqueda('Star-Lord','nombre')
if (pos > -1 ):
    print('Informacion de Star-Lord: ',lista_superheroes.obtener_elemento(pos))


print('La cantidad de super heroes que hay en el comic  Marvel son : ',cont_marvel)
print('La cantidad de super heroes que hay en el comic dc son : ', cont_dc)
print('*Sin contar a linterna verde porque se elimino*')
print('Los personajes que en su biografia figura la palabra traje son: ',cont_traje)
print('Los personajes que en su biografia figura la palabra armadura son: ',cont_armadura)
print('Superheroes cuyo nombre empiezan con S: ',cont_s)
print('Superheroes cuyo nombre empiezan con M: ',cont_m)
print('Superheroes cuyo nombre empiezan con B: ',cont_b)
print()


lista_superheroes.barrido()
