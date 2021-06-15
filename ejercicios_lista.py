from lista_tda import Lista,insertar,eliminar,buscar,lista_vacia,tamanio,barrido_lista,criterio
from listadelista_tda import Lista, insertar, eliminar,barrido_con_sublista, tamanio, lista_vacia, criterio,buscar_sublista
from random import randint
from clases import Superheroe,Cancion,StarWars,Entrenador,Pokemon,Proyecto,Tarea,Vuelo,Clase,Estacion,Medicion,Pelicula,InfoPelicula
import random

# no hacer 8 12 13 14 


def contar_nodos(): #1
    lista = Lista()
    c_nodos = 0
    for x in range(10):
        insertar(lista, random.randint(0,50))
    barrido_lista(lista)
    nodo = lista.inicio
    while nodo is not None:
        c_nodos = c_nodos+1
        nodo = nodo.sig # actualizamos la posicion del nodo al siguiente
    print('la cantidad de nodos es', c_nodos)

def vocales():  #2
    letras = Lista()
    for x in range(100):
        insertar(letras,chr(randint(65,90)))
    barrido_lista(letras)
    letra = eliminar(letras,'A')
    while letra is not None:
        letra= eliminar(letras,'A')
    letra = eliminar(letras,'E')
    while letra is not None:
        letra= eliminar(letras,'E')
    letra = eliminar(letras,'I')
    while letra is not None:
        letra= eliminar(letras,'I')
    letra = eliminar(letras,'O')
    while letra is not None:
        letra= eliminar(letras,'O')
    letra = eliminar(letras,'U')
    while letra is not None:
        letra= eliminar(letras,'U')
    print('lista de letras sin vocales')
    barrido_lista(letras)

def par_impar(): #3
    numeros = Lista()
    pares = Lista()
    impares = Lista()
    for x in range(50):
        insertar(numeros,randint(0,100))
    print('lista de numeros')
    barrido_lista(numeros)

    while not lista_vacia(numeros):
        numero = eliminar(numeros,numeros.inicio.info) # elimina el numero que esta al inicio de la lista
        if numero % 2 == 0:
            insertar(pares,numero)
        else:
            insertar(impares,numero)
    print('lista de numeros pares')
    barrido_lista(pares)
    print('lista de numeros impares')
    barrido_lista(impares)


def superheroeDCMarvel():   #6
    superheroes = Lista()
    BMS = Lista()
    c_dc = 0
    c_marvel = 0
    
    personaje = Superheroe('Batman',1939,'DC','El caballero de la noche')
    insertar(superheroes,personaje,'nombre')
    personaje = Superheroe('Linterna Verde',1940,'DC','La luz de Linterna Verde')
    insertar(superheroes, personaje,'nombre')
    personaje = Superheroe('Wolverine',1974,'Marvel','Arma x')
    insertar(superheroes, personaje,'nombre')
    personaje = Superheroe('Flash',1940,'DC','El corredor escarlata')
    insertar(superheroes, personaje,'nombre')
    personaje = Superheroe('Doctor Strange',1963,'DC','Hechicero supremo')
    insertar(superheroes, personaje,'nombre')
    personaje = Superheroe('Capitana Marvel',1968,'Marvel','Ms. Marvel')
    insertar(superheroes, personaje,'nombre')
    personaje = Superheroe('Star-Lord', 1976, 'Marvel', 'Tirador experto con armadura')
    insertar(superheroes, personaje, 'nombre')
    personaje = Superheroe('Mujer Maravilla', 1941, 'DC', 'Diosa de la guerra traje')
    insertar(superheroes, personaje, 'nombre')

    print('lista de superheroes')
    barrido_lista(superheroes)
    #eliminando info de linterna verde
    print('')
    eliminado = eliminar(superheroes, 'Linterna Verde', 'nombre')
    print('personaje eliminado', eliminado.nombre)
    print('ahora la lista es..')
    barrido_lista(superheroes)
    print('')
    # anio aparicion wolverine
    wolv=buscar(superheroes, 'Wolverine', 'nombre')
    if wolv is not None:
        print('primera aparicion de Wolverine',wolv.info.anio)
    else:
        print('Wolverine no esta en la lista')
    print('')
    # cambiar la casa de dr strange a Marvel
    drstrange = buscar(superheroes, 'Doctor Strange', 'nombre') 
    if drstrange is not None:
        drstrange.info.casa = 'Marvel'
    else:
        print('Doctor Strange no esta en la lista')
    print('ahora Doctor Strange esta en Marvel')
    barrido_lista(superheroes)
    # superheroes con traje o armadura en bio
    print('')
    aux = superheroes.inicio
    while aux is not None:
        if 'traje' in aux.info.bio or 'armadura' in aux.info.bio:
            print('traje o armadura en la biografia',aux.info.nombre)
        aux = aux.sig
    print('')
    # aparicion menor a 1963
    aux = superheroes.inicio
    while aux is not None:
        if aux.info.anio< 1963:
            print('aparicion menor a 1963', aux.info.nombre, aux.info.casa,'en',aux.info.anio)
        aux = aux.sig
    print('')
    # info de mujer maravilla y capitana marvel
    busc1 = buscar(superheroes,'Mujer Maravilla','nombre') 
    busc2 = buscar(superheroes,'Capitana Marvel','nombre')  
    if busc1 is not None and busc2 is not None:
        print('la casa de',busc1.info.nombre,'es',busc1.info.casa)
        print('la casa de',busc2.info.nombre,'es',busc2.info.casa)
    print('')
    #info de flash y star lord
    flash = buscar(superheroes,'Flash','nombre')
    Sl = buscar(superheroes, 'Star-Lord','nombre')
    if flash is not None and Sl is not None:
        print('info de',flash.info.nombre,'',flash.info)
        print('info de',Sl.info.nombre,'',Sl.info)
    # superheroes con letra BMS
    print('')
    nodo = superheroes.inicio
    while nodo is not None:
        if nodo.info.nombre[0] == 'B' or nodo.info.nombre[0] == 'M' or nodo.info.nombre[0] == 'S':
            insertar(BMS, nodo.info.nombre)
        nodo = nodo.sig
    print('superheroes que empiezan con la letra B,M o S')
    barrido_lista(BMS)
    print('')
    # cantidad de superheroes por casa
    nodo = superheroes.inicio
    while nodo is not None:
        if nodo.info.casa == 'DC':
            c_dc +=1
            nodo = nodo.sig
        else:
            c_marvel+=1
            nodo = nodo.sig

    print('cantidad superheroes DC', c_dc)
    print('cantidad superheroes Marvel', c_marvel)


def interseccion(): #7
    lista_1 = Lista()
    lista_2 = Lista()

    for x in range(10):
        insertar(lista_1, randint(0,10))
    for x in range(15):
        insertar(lista_2, randint(0,10))

    print('lista 1')
    barrido_lista(lista_1)
    print('lista 2')
    barrido_lista(lista_2)
    
    # punto a


    # punto c
    indice = lista_1.inicio

    while indice is not None:
        buscado = buscar(lista_2,indice.info)
        if buscado is not None:
            print('aparece en ambas listas',indice.info)
        indice = indice.sig


def spotify():
    # no hacer B
    playlist = Lista()
    palabra = Lista()

    cancion = Cancion('Do i wanna know?','Artic Monkeys',4.31,4565654)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('Pices','Sum 41',2.53,2332423)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('Like a Stone','Audioslave',4.32,51646775)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('Exercises in Futility IV','Mgla',8.45,123345)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('Goner','Twenty one Pistols',3.35,34556567)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('Godzilla','Eminem',4.25,1490234532)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('Be yourself','Audioslave',4.15,154565654)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('First Date','Blink 182',3.33,150564654)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('A rose for Epona','Eluveitie',14.12,2267334)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('Disgraced','Cairiss',9.21,145235)
    insertar(playlist,cancion,'duracion')
    cancion = Cancion('R U Mine?','Artic Monkeys',3.35,62568924)
    insertar(playlist,cancion,'duracion')
    

    print('mis canciones')
    barrido_lista(playlist)
    #punto A
    print('')
    nodo = playlist.inicio
    mayor = nodo.info.duracion
    while nodo.sig is not None:
        nodo = nodo.sig
        if nodo.info.duracion > mayor:
            mayor  = nodo.info.duracion
    print('cancion de mayor duracion ',nodo.info.nombre,'con',mayor,)
    # punto C
    print('')
    am = playlist.inicio
    while am is not None:
        if am.info.artista == 'Artic Monkeys':
            print(am.info.nombre, 'es de', am.info.artista)
        am = am.sig
    print('')
    # punto D
    nodo = playlist.inicio
    while nodo is not None:
        if len(nodo.info.artista.split()) == 1:
            insertar(palabra, nodo.info.artista)
        nodo = nodo.sig
    print('artistas o bandas cuyos nombres son solo una palabra')
    barrido_lista(palabra)


def starwars():
    personajes = Lista()
    femeninos = Lista()
    droides = Lista()
    episodios = Lista()
    halderaan = Lista()
    edades = Lista()

    personaje = StarWars('Chewbacca',2.25,900,'m','wookiee','Kashyyyk',['II','III','IV','V','VI'])
    insertar(personajes,personaje,'nombre')
    personaje = StarWars('C3PO',1.75,400,'m','droide','Tatooine',['I','II','III','IV','V','VI'])
    insertar(personajes,personaje,'nombre')    
    personaje = StarWars('Leila Organa',1.55,560,'f','humano','Alderaan',['I','II','III','IV','V','VI','VII'])
    insertar(personajes,personaje,'nombre')  
    personaje = StarWars('Luke Skywalker',1.72,860,'m','humano','Tatooine',['I','II','III','IV','V','VI','VII','VIII'])
    insertar(personajes,personaje,'nombre')
    personaje = StarWars('Han Solo',1.80,870,'m','humano','Corellia',['II','III','IV','V','VI','VII','VIII'])
    insertar(personajes,personaje,'nombre')  
    personaje = StarWars('Darth Vader',2.3,775,'m','humano','Tatooine',['I','II','III','IV','V','VI','VII','VII'])
    insertar(personajes,personaje,'nombre')
    personaje = StarWars('RD2D',0.52,450,'m','droide','Tatooine',['I','II','III','IV','V','VI'])
    insertar(personajes,personaje,'nombre')
    personaje = StarWars('Ahsoka Tano',1.88,250,'f','togruta','Shili',['IV','V','VI'])
    insertar(personajes, personaje, 'nombre')
   

    print('personajes de StarWars')
    barrido_lista(personajes)

    # punto A
    print('')
    femenino = personajes.inicio
    while femenino is not None:
        if femenino.info.genero =='f':
            insertar(femeninos,femenino.info.nombre)
        femenino = femenino.sig
    print('personajes femeninos')
    barrido_lista(femeninos)
    # punto B
    print('')
    nodo = personajes.inicio
    while nodo is not None:
        if nodo.info.especie == 'droide' and len(nodo.info.especie) >= 6:
            insertar(droides, nodo.info.nombre)
        nodo = nodo.sig
    print('droides que aparecen en los primeros 6 episodios')
    barrido_lista(droides)
    # punto C
    print('')
    han = buscar(personajes, 'Han Solo', 'nombre') 
    dv = buscar(personajes, 'Darth Vader','nombre')
    if han is not None and dv is not None:
        print('Han Solo ',han.info)
        print('Darth Vader ',dv.info)
    # punto D
    print('')
    nodo = personajes.inicio
    while nodo is not None:
        if 'IV' in nodo.info.episodios and 'V' in nodo.info.episodios and 'VI' in nodo.info.episodios and 'VII' in nodo.info.episodios:
            insertar(episodios, nodo.info.nombre)
        nodo = nodo.sig
    print('aparecen en el episodio VII y los tres anteriores')
    barrido_lista(episodios)
    # punto E
    print('')
    nodo = personajes.inicio
    mayor = nodo.info.edad
    while nodo.sig is not None:
        nodo = nodo.sig
        if nodo.info.edad > 850:
            print('personaje con mas de 850 años',nodo.info.nombre,'con',nodo.info.edad)
        if nodo.info.edad > 850 and nodo.info.edad > mayor:
            mayor = nodo.info.edad
            print('el mas viejo es ',nodo.info.nombre,'con',nodo.info.edad)
    # punto F
    print('')
    eliminado = eliminar(personajes,['IV','V','VI'],'episodios')
    print('personaje eliminado', eliminado)
    print('la lista ahora es .. ')
    barrido_lista(personajes)
    # punto G
    print('')
    nodo = personajes.inicio
    while  nodo is not None:
        if nodo.info.especie == 'humano' and nodo.info.planeta == 'Alderaan':
            insertar(halderaan, nodo.info.nombre)
        nodo = nodo.sig
    print('personajes de raza humana natales de Alderaan')
    barrido_lista(halderaan)
    # punto H
    print('')
    altura = personajes.inicio
    while altura is not None:
        if altura.info.altura < 0.70:
            print('personaje con altura menor a 70 cm', altura.info)
        altura = altura.sig
    #punto I
    print('')
    nodo = buscar(personajes,'Chewbacca','nombre')
    if nodo is not None:
        print('episodios en los que aparece',nodo.info.nombre,'',nodo.info.episodios)
        print('informacion de',nodo.info.nombre,'',nodo.info)
    nodo = nodo.sig


def pokemon():  #15
    entrenadores = Lista()
    torneos = Lista()
    tipo_sub = Lista()

    #nombre torneos ganados batallas perdidas y ganadas
    print('entrenadores de pokemons')
    for x in range(1):
        nombre = input('nombre del entrenador ')
        tg = int(input('torneos ganados '))
        bp = int(input('batallas perdidas '))
        bg = int(input('batallas ganadas '))
        
        entrenador = Entrenador(nombre,tg,bp,bg)
        insertar(entrenadores,entrenador,'nombre')
        
    # nombre nivel tipo subtipo
    print('')
    
    nombre = input('nombre del entrenador de los pokemons ')
    while nombre != '':
        nodo = buscar(entrenadores,nombre,'nombre')
        if nodo is not None:
            nombre = input('nombre del pokemon ')
            nivel = int(input('nivel del pokemon '))
            tipo = input('tipo del pokemon ')
            subtipo = input('subtipo del pokemon ')
            pokemon = Pokemon(nombre,nivel,tipo,subtipo)
            insertar(nodo.sublista, pokemon, 'nombre')
        nombre = input('nombre del entrenador de los pokemons ')

    print('lista de entrenadores con sus pokemons')
    barrido_con_sublista(entrenadores)
    
    # punto a
    # cantidad de pokemons de un determinado entrenador
    count = 0
    nodo = entrenadores.inicio
    while nodo is not None:
        entrenador = input('nombre del entrenador para ver cantidad de pokemons ')
        entrenador = buscar(entrenadores, entrenador, 'nombre')
        pokemons = nodo.sublista.inicio
        while pokemons is not None:
            if entrenador is not None:
                count += 1
                print('cantidad de pokemons',count)
            pokemons = pokemons.sig
        nodo = nodo.sig

    #punto b
    nodo = entrenadores.inicio
    while nodo is not None:
        if nodo.info.tg > 3:
            insertar(torneos, nodo.info.nombre)
        nodo = nodo.sig
    print('entrenadores con mas de 3 torneos ganados')
    barrido_lista(torneos)

    #punto c
    

    # punto d 
    nodo = entrenadores.inicio
    while nodo is not None:
        entrenador = input('ingrese nombre del entrenador para ver su info y la de sus pokemons ')
        entrenador = buscar(entrenadores, entrenador, 'nombre')
        pokemons = nodo.sublista.inicio
        while pokemons is not None:
            if entrenador is not None:
                print('info del entrenador',nodo.info.nombre,'',nodo.info)
                print('info del pokemon',pokemons.info.nombre,'',pokemons.info)
            pokemons = pokemons.sig
        nodo = nodo.sig

    # punto e
    print('')
    nodo = entrenadores.inicio
    while nodo is not None:
        ganadas = 0
        perdidas = 0
        porcent = 0
        if nodo is not None:
                pass
        ganadas += nodo.info.bg
        perdidas += nodo.info.bp
        total = ganadas + perdidas
        porcent = ganadas*100/total
        if porcent > 79:
            print('porcentaje de victorias mayor a 79 ',nodo.info.nombre)        
        else:
            print('el porcentaje de victorias de ',nodo.info.nombre,'es menor a 79')
        nodo = nodo.sig
    
    # punto f
    print('')
    nodo = entrenadores.inicio
    while nodo is not None:
        pokemon = nodo.sublista.inicio
        while pokemon is not None:
            if pokemon.info.tipo == 'fuego' and pokemon.info.subtipo == 'planta' or pokemon.info.subtipo == 'agua' and pokemon.info.subtipo == 'volador':
                print('tiene pokemons fuego/planta o agua/volador ',nodo.info.nombre,'',pokemon.info.nombre)
            pokemon = pokemon.sig
        nodo = nodo.sig
    
    # punto g
    print('')
    nodo = entrenadores.inicio
    while nodo is not None:
        entrenador = input('nombre del entrenador para ver pormedio de nivel de sus pokemons ')
        nivel_promedio = 0
        pokemon = nodo.sublista.inicio
        while pokemon is not None:
            if entrenador is not None:
                pass
            nivel_promedio += pokemon.info.nivel
            pokemon = pokemon.sig
        
        if tamanio(nodo.sublista) > 0:
            nivel_promedio = nivel_promedio / tamanio(nodo.sublista)
        print('promedio nivel de',nodo.info.nombre, 'sus pokemons ',nivel_promedio)
        nodo = nodo.sig
        
    # punto h
    count = 0
    nodo = entrenadores.inicio
    while nodo is not None:
        nombre = input('nombre del pokemon ') 
        pokemon = nodo.sublista.inicio
        while pokemon is not None:
            if nombre in pokemon.info.nombre:
                count +=1
            pokemon = pokemon.sig
        nodo = nodo.sig
    print('entrenadores que tienen a ese pokemon',count)
    #punto i
    count = 0
    nodo = entrenadores.inicio
    while nodo is not None:
        nombre = input('nombre del pokemon ')
        pokemon = nodo.sublista.inicio
        while pokemon is not None:
            if nombre in pokemon.info.nombre:
                count += 1
                if count > 2:
                    print('tiene pokemons repetidos',nodo.info.nombre)
            pokemon = pokemon.sig
        nodo = nodo.sig
    # punto j
    print('')
    nodo = entrenadores.inicio
    while nodo is not None:
        pokemon = nodo.sublista.inicio
        while  pokemon is not None:
            if pokemon.info.nombre == 'terrakion' or pokemon.info.nombre == 'tyrantrum' or pokemon.info.nombre == 'wingull':
                print('entrenador que tiene a Terrakion Tyrantrum o Wingull',nodo.info.nombre,'tiene a ',pokemon.info.nombre)
            pokemon = pokemon.sig
        nodo = nodo.sig
    
    # punto k
    print('verifique si un entrenador x tiene a un pokemon y')
    nodo = entrenadores.inicio
    while nodo is not None:
        entrenador = input('nombre del entrenador ')
        pokemon = input('nombre del pokemon ')
        pokemons = nodo.sublista.inicio
        while pokemons is not None:
            if entrenador in nodo.info.nombre and pokemon in pokemons.info.nombre:
                print('datos del entrenador ',nodo.info)
                print('datos del pokemon ',pokemons.info)
            pokemons = pokemons.sig
        nodo = nodo.sig

def proyecto(): #16
    proyectos = Lista()

    for x in range(1):
        proyecto = input('nombre del proyecto ')
        proyecto = Proyecto(proyecto)
        insertar(proyectos, proyecto,'proyecto')

    nombre = input('nombre del proyecto para ver sus tareas y personal a cargo ')
    while nombre != '':
        pos = buscar(proyectos, nombre, 'proyecto')
        if pos != None:
            print('---informacion de las tareas del proyecto---')
            persona = input('ingrese la persona a cargo ')
            costo = int(input('costo de la tarea ')) 
            tiempo = int(input('tiempo de ejecucion '))
            inicio = input('fecha de inicio ')
            estimada = input('fecha de fin estimada ')
            efectiva = input('fecha de fin efectiva ')
            
            tarea = Tarea(persona,costo,tiempo,inicio,estimada,efectiva)
            insertar(pos.sublista, tarea, 'persona')

        nombre = input('nombre del proyecto para ver sus tareas y personal a cargo ')

    print('lista de tareas del proyecto')
    barrido_con_sublista(proyectos)

    # punto a
    nodo = proyectos.inicio
    while nodo is not None:
        nombre = input('nombre del proyecto para ver su tiempo promedio de tareas ')
        tiempo_promedio = 0
        proyecto = nodo.sublista.inicio
        while proyecto is not None:
            if nombre in nodo.info.proyecto:
                pass
            tiempo_promedio += proyecto.info.tiempo
            proyecto = proyecto.sig
        

        if tamanio(nodo.sublista)>0:
            tiempo_promedio = tiempo_promedio / tamanio(nodo.sublista)
        print('tiempo promedio de las tareas del proyecto  ',nombre,'',tiempo_promedio)
        nodo = nodo.sig

    #punto b
    nodo = proyectos.inicio
    while nodo is not None:
        nombre = input('nombre del proyecto a ver costo total ')
        coste = 0
        proyecto = nodo.sublista.inicio
        while proyecto is not None:
            if nombre in nodo.info.proyecto:
                pass
            coste += proyecto.info.costo
            proyecto = proyecto.sig
        nodo = nodo.sig

    print('costo total del proyecto ',coste)

    # punto c
    # actividades realizadas por una persona
    nodo = proyectos.inicio
    while nodo is not None:
        persona = input('nombre de la persona para ver sus tareas ')
        tareas = nodo.sublista.inicio
        while tareas is not None:
            if persona != '' and persona in tareas.info.persona:
                print('tareas realizadas por:',persona,',',tareas.info)
            tareas = tareas.sig
        nodo = nodo.sig

    #faltan d e f

def aeropuerto():
    vuelos = Lista()
    destinos = Lista()


    for x in range(2):
        empresa = input('nombre de la empresa ')
        numero = input('numero de vuelo ')
        asientos = int(input('numero de asientos '))
        salida = input('fecha de salida ')
        destino = input('destino ')
        kms = int(input('kilometros a recorrer '))

        vuelo = Vuelo(empresa,numero,asientos,salida,destino,kms)
        insertar(vuelos, vuelo, 'empresa')
    

    numero =input('ingrese el numero de vuelo ')
    while numero != '':
        pos = buscar(vuelos,numero,'numero')
        if pos != None:
            print('datos de los asientos del vuelo por clase')
            clase = input('ingrese la clase (turista o primera) ')
        if clase == 'turista' or clase == 'primera':
            totales = int(input('total de asientos '))
            ocupados = int(input('asientos ocupados '))
            clases = Clase(clase,totales,ocupados)
            insertar(pos.sublista,clases,'clase')

        numero = input('ingrese el numero de vuelo ')
    
    print()
    print('datos del vuelo con los datos de asientos por clase')
    barrido_con_sublista(vuelos)

    # punto a
    print()
    nodo = vuelos.inicio
    while nodo is not None:
        destino = buscar(vuelos,'Atenas','destino')
        destino = buscar(vuelos,'Miconos','destino')
        destino = buscar(vuelos,'Rodas','destino')
        if destino is not None:
            insertar(destinos,nodo.info,'empresa')
        nodo = nodo.sig
    print('con destino Atenas Miconos Rodas')
    barrido_lista(destinos)
    

    #punto b
    print()
    nodo = vuelos.inicio
    while nodo is not None:
        numero = input('numero de vuelo ')
        totales = 0
        ocupados = 0
        disponibles = 0
        vuelo = nodo.sublista.inicio
        while vuelo is not None:
            if 'turista' in vuelo.info.clase:
                pass
            totales += vuelo.info.totales
            ocupados += vuelo.info.ocupados
            disponibles = totales-ocupados
            vuelo = vuelo.sig
        if disponibles > 0:
            print('vuelo con asientos en clase turista disponibles ',nodo.info, 'con',disponibles)
        else:
            print('el vuelo no tiene asientos en clase turista disponibles')
        nodo = nodo.sig


    #punto d
    print('')
    nodo = vuelos.inicio
    while nodo is not None:
        salida = input('ingrese la fecha de salida d/m/a ')
        fecha = buscar(vuelos,salida,'salida')
        if fecha is not None:
            print('vuelos para la fecha ',salida,'',nodo.info)
        nodo = nodo.sig


   # punto g
    print()
    nodo = vuelos.inicio
    while nodo is not None:
        if nodo.info.destino == 'Tailandia':
            print('empresa con destino Tailandia ',nodo.info.empresa,'kms a recorrer',nodo.info.kms)
        nodo = nodo.sig

def meteorologia():
    estaciones = Lista()
    
    
    print('ubicaion de las estaciones meteorologicas')
    for x in range(2):
        pais = input('pais origen de la estacion ')
        latitud = input('latitud ')
        longitud = input('longitud ')
        altitud = input('altitud ')
        
        estacion = Estacion(pais,latitud,longitud,altitud)
        insertar(estaciones,estacion,'pais')

    latitud = input('ingrese la latitud ')

    while latitud != '':
        pos = buscar(estaciones,latitud,'latitud')
        if pos != None:
            print('datos de medicion de las estaciones')
            temp = int(input('temperatura '))
            presion = int(input('presion '))
            humedad = int(input('humedad '))
            estado = input('estado climatico ')
            fecha = input('fecha de medicion (dd mm aa) ')
            hora = input('hora de medicion ')
            medicion = Medicion(temp,presion,humedad,estado,fecha,hora)
            insertar(pos.sublista,medicion,'temp')
            
        latitud = input('ingrese la latitud ')
        
    print('estaciones meteorologicas con sus datos de medicion y ubicacion ')
    print('')
    barrido_con_sublista(estaciones)


    # punto c
    nodo = estaciones.inicio
    while nodo is not None:
        mes = '5'
        t_promedio = 0
        h_promedio = 0
        temp = nodo.sublista.inicio
        humedad = nodo.sublista.inicio
        while temp is not None and humedad is not None:
            if mes in temp.info.fecha and mes in humedad.info.fecha:
                pass
            t_promedio += temp.info.temp
            h_promedio += humedad.info.humedad
            temp = temp.sig
            humedad = humedad.sig
        
        if tamanio(nodo.sublista) > 0:
            t_promedio = t_promedio / tamanio(nodo.sublista)
            h_promedio = h_promedio / tamanio(nodo.sublista)
        print('promedio de temperaturas registradas en mayo en ',nodo.info,t_promedio,'°C')
        print('promedio de la humedad registrada en mayo en',nodo.info,h_promedio)
        nodo = nodo.sig
                
        
    # punto d 
    nodo = estaciones.inicio
    while nodo is not None:
        medicion = nodo.sublista.inicio
        while medicion is not None:
            estado = buscar_sublista(nodo.sublista,'lluvioso','estado')
            clima = buscar_sublista(nodo.sublista,'nevando','estado')
            if estado is not None or clima is not None:
                print('ubicacion de las estaciones donde esta lloviendo o nevando ',nodo.info,'el dia',medicion.info.fecha)
            medicion = medicion.sig
        nodo = nodo.sig
        

    #punto e
    nodo = estaciones.inicio
    while nodo is not None:
        medicion = nodo.sublista.inicio
        while medicion is not None:
            tormenta = buscar_sublista(nodo.sublista,'tormenta electrica','estado')
            huracan = buscar_sublista(nodo.sublista,'huracan','estado')
            if tormenta is not None or huracan is not None:
                print('estaciones donde se registraron tormentas electricas o huracanes','ubicacion:',nodo.info,'medicion:',medicion.info)
            medicion = medicion.sig
        nodo = nodo.sig

meteorologia()

def movies():
    peliculas = Lista()
    peliculas_aux = Lista()

    for x in range(2):
        nombre = input('nombre de la pelicula ')
        pelicula = Pelicula(nombre)
        insertar(peliculas,pelicula,'nombre')

    nombre = input('ingrese el nombre de la pelicula ')
    while nombre != '':
        pos = buscar(peliculas,nombre,'nombre')
        if pos is not None:
            print('---datos de la pelicula---')
            valoracion = int(input('valoracion '))
            estreno = int(input('anio de estreno '))
            recaudacion = int(input('recaudacion total '))
            datos = InfoPelicula(valoracion,estreno,recaudacion)
            insertar(pos.sublista,datos,'valoracion')

        nombre = input('ingrese el nombre de la pelicula ')
    
    print('')
    print('---|pelicilas con sus datos|---')
    barrido_con_sublista(peliculas)

    #punto a
    print('')
    nodo = peliculas.inicio
    while nodo is not None:
        anio = int(input('ingrese el anio de estreno '))
        pelicula = buscar_sublista(nodo.sublista,anio,'estreno')
        if pelicula is not None:
            print('peliculas estrenadas en ',anio,'',nodo.info.nombre)
        nodo = nodo.sig
    
    #punto b
    nombre = ''
    mayor_recaudacion = 0
    nodo = peliculas.inicio
    while nodo is not None:
        pelicula = nodo.sublista.inicio
        recaudacion = 0
        while pelicula is not None:
            recaudacion += pelicula.info.recaudacion
            pelicula = pelicula.sig
        if recaudacion > mayor_recaudacion:
            nombre = nodo.info.nombre
        nodo = nodo.sig
    print('pelicula que mas recaudo ',nombre)



# EJ 15
class Entrenador():
    def __init__(self, entrandor, t_ganados, b_ganadas, b_perdidas):
        self.entrenador = entrandor
        self.t_ganados = t_ganados
        self.b_ganadas = b_ganadas
        self.b_perdidas = b_perdidas

    def __str__(self):
        return self.entrenador + ' | ' + str(self.t_ganados) + ' | ' + str(self.b_ganadas) + ' | ' + str(self.b_perdidas)


class Pokemon():
    def __init__(self, pokemon, nivel, tipo, subtipo):
        self.pokemon = pokemon
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return self.pokemon + ' | ' + str(self.nivel) + ' | ' + self.tipo + ' | ' + self.subtipo


def pokemon():
    lista = Lista()
    pokemon = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Spearow',
               'Dugtrio', 'Primeape', 'Terrakion', 'Tyrantrum', 'Wingull']
    tipo = ['Fuego', 'Agua', 'Electrico', 'Normal', 'Veneno']
    subtipo = ['Tierra', '-', 'Planta', 'Agua', '-', 'Volador']
    dato = Entrenador('Ranchero', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    dato = Entrenador('Alevin', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    dato = Entrenador('Pescador', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    for i in range(2):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Ranchero', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    for i in range(3):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Alevin', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    for i in range(4):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Pescador', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    # d
    print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
    barrido_lista(lista)
    print()
    aux = lista.inicio
    # barrido sublista
    while aux is not None:
        print('Entrenador:', aux.info.entrenador)
        print('NOMBRE | NIVEL | TIPO | SUBTIPO')
        barrido_sublista(aux.sublista)
        print()
        aux = aux.sig

    # a
    aux = lista.inicio
    print('Cantidad de Pokemons de un determinado entrenador')
    entr = input('Ingrese nombre del entrenador: ')
    while aux is not None:
        pos = busqueda_lista(lista, entr, 'entrenador')
        if pos is not None:
            print(aux.info.entrenador, 'posee', tamanio_lista(aux.sublista), 'pokemones')
        else:
            print('El entrenador no existe')
            break
        aux = aux.sig
    print()

    # b
    aux = lista.inicio
    print('Entrenadores que ganaron mas de 3 torneos')
    while aux is not None:
        if aux.info.t_ganados >= 3:
            print(aux.info.entrenador + ':', aux.info.t_ganados, 'torneos')
        aux = aux.sig
    print()

    # c
    aux = lista.inicio
    mg, mn = 0, 0
    while aux is not None:
        if aux.info.t_ganados > mg:
            mg = aux.info.t_ganados
            mas_ganador = aux.info.entrenador
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.nivel > mn:
                mn = sublista.info.nivel
                mayor_nivel = sublista.info.pokemon
            sublista = sublista.sig
        aux = aux.sig
    print('El entrenador mas ganador es', mas_ganador, 'con', mg, 'torneos')
    print('Su pokemon de mayor nivel es', mayor_nivel, 'con nivel', mn)
    print()

    # e
    aux = lista.inicio
    while aux is not None:
        batallas_totales = aux.info.b_ganadas + aux.info.b_perdidas
        porcentaje_batallas = (aux.info.b_ganadas * 100)/batallas_totales
        if porcentaje_batallas > 79:
            print(aux.info.entrenador, 'tiene un porcentaje de batalladas ganadas mayor a 79%')
        aux = aux.sig
    print()

    # f
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.tipo == 'Fuego' and sublista.info.subtipo == 'Planta':
                print(aux.info.entrenador, 'posee un pokemon tipo fuego y subtipo planta, llamado', sublista.info.pokemon)
            if sublista.info.tipo == 'Agua' and sublista.info.subtipo == 'Volador':
                print(aux.info.entrenador, 'posee un pokemon tipo agua y subtipo volador, llamado', sublista.info.pokemon)
            sublista = sublista.sig
        aux = aux.sig
    print()

    # g
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        cont_nivel = 0
        while sublista is not None:
            cont_nivel += sublista.info.nivel
            prom_nivel = cont_nivel / tamanio_lista(aux.sublista)
            sublista = sublista.sig
        # round redondea el valor prom_nivel a 2 digitos despues de la coma
        print(aux.info.entrenador + ', promedio de nivel de sus pokemons:', round(prom_nivel, 2))
        aux = aux.sig
    print()

    # h
    aux = lista.inicio
    cont = 0
    poke = input('Ingrese nombre de pokemon a buscar: ')
    while aux is not None:
        pos = busqueda_lista(aux.sublista, poke, 'pokemon')
        if pos is not None:
            cont += 1
        aux = aux.sig
    print(cont, 'entrenadores tienen al pokemon', poke)
    print()

    # j
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.pokemon == 'Tyrantrum' or sublista.info.pokemon == 'Terrakion' or sublista.info.pokemon == 'Wingull':
                print(aux.info.entrenador, 'tiene al pokemon', sublista.info.pokemon)
            sublista = sublista.sig
        aux = aux.sig
    print()

    # k
    aux = lista.inicio
    print('Busca un entrenador y sus pokemones')
    entr = input('Ingrese nombre de entrenador a buscar: ')
    poke = input('Ingrese nombre de pokemon a buscar: ')
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if entr == aux.info.entrenador and poke == sublista.info.pokemon:
                print()
                print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
                print(aux.info)
                print()
                print('NOMBRE | NIVEL | TIPO | SUBTIPO')
                print(sublista.info)
            sublista = sublista.sig
        aux = aux.sig


# EJ 16
def proyecto_software():
    '''Actividades de un proyecto de software'''
    lista, en_tiempo, fuera_tiempo = Lista(), Lista(), Lista()
    persona = ['Gerardo', 'Martina', 'Lucia', 'Geovanni', 'Jessica', 'Laura']
    prom_tareas, costo_total = 0, 0
    df = ''
    for i in range(5):
        costo = randint(0, 50000)
        tde = randint(1, 10)
        fdi = [2020, randint(1, 12), randint(1, 31)]
        fdfest = [2020, randint(1, 12), randint(1, 31)]
        fdfefc = [2020, randint(1, 12), randint(1, 31)]
        pac = choice(persona)
        tarea = [costo, tde, fdi, fdfest, fdfefc, pac]
        insertar(lista, tarea)
    print('Costo | Tiempo de ejec. | Fecha de inicio | Fecha de fin estimada | Fecha de fin efectiva | Persona a cargo')
    barrido_lista(lista)
    print()
    aux = lista.inicio
    while aux is not None:
        dato = aux.info
        # a
        prom_tareas += dato[1]
        # b
        costo_total += dato[0]
        # c
        if dato[5]:
            print()
            print('Persona:', dato[5])
            print('Actividades que realiza:')
            print('Coste de la actividad:', dato[0], 'ARS')
            print('Tiempo de ejecucion:', dato[1])
        # d
        if dato[2][1] > 5 and dato[3][1] > 5:
            df = [dato[0], dato[1], dato[2], dato[3]]
        # e
        if dato[3][0] > dato[4][0] and dato[3][1] > dato[4][1]:
            insertar(fuera_tiempo, [dato[0], dato[1], dato[5]])
        else:
            insertar(en_tiempo, [dato[0], dato[1], dato[5]])
        aux = aux.sig
    prom_tareas = prom_tareas / tamanio_lista(lista)
    print()
    print('Tiempo promedio de tareas', prom_tareas)
    print('Costo total del proyecto', costo_total, 'ARS')
    print('Tareas a realizar entre dos fechas dadas(a partir de Junio):')
    print(df)
    print()
    print('Tareas finalizadas en tiempo estipulado')
    barrido_lista(en_tiempo)
    print()
    if not lista_vacia(fuera_tiempo):
        print('Tareas fuera de tiempo')
        barrido_lista(fuera_tiempo)
    else:
        print('No hay tareas fuera de tiempo')


# EJ 17
def aeropuerto_creta():
    '''Vuelos del aeropuerto de Heraklion en Creta'''
    vuelos, vuelos_destinos, turista_disponible = Lista(), Lista(), Lista()
    monto_vuelos, vuelos_junio, lista_aux = Lista(), Lista(), Lista()
    nom_empr = ['Qatar Airways', 'Singapore Airlines', 'Fly Emirates',
                'Iberia', 'Turkish Airlines']
    ciudad_dest = ['Atenas', 'Miconos', 'Rodas', 'Tailandia', 'Nicosia',
                   'Ulan Bator', 'Yakarta', 'El Brillante']
    estado = ['Ocupado', 'Desocupado']
    clase = ['Primera Clase', 'Turista']
    nro = 1
    for i in range(len(nom_empr)):
        empresa = nom_empr[i]
        num_vuelo = randint(1000, 10000)
        asientos = randint(40, 80)
        fds = [2020, randint(1, 12), randint(1, 31)]
        destino = choice(ciudad_dest)
        kms_vuelo = randint(400, 5000)
        datos_avion = [empresa, num_vuelo, asientos, fds, destino, kms_vuelo]
        insertar(vuelos, datos_avion)
        for j in range(asientos):
            as_avion = busqueda_lista_vec(vuelos, empresa, 0)
            if as_avion is not None:
                as_nro = nro
                nro += 1
                as_estado = choice(estado)
                as_clase = choice(clase)
                datos_asientos = [as_nro, as_estado, as_clase]
                insertar(as_avion.sublista, datos_asientos)
    print('EMPRESA | NUM. VUELO | ASIENTOS | FECHA DE SALIDA | DESTINO | KMS. VUELO')
    barrido_lista(vuelos)
    print()
    aux = vuelos.inicio
    km = aux.info[5]
    monto_turista, monto_pc = 0, 0
    while aux is not None:
        print('Datos de asientos:', aux.info[0])
        print('Cantidad de asientos:', tamanio_lista(aux.sublista))
        # print('ASIENTOS TOTALES | ESTADO | CLASE')
        # barrido_sublista(aux.sublista)
        print()
        # a
        if aux.info[4] == 'Atenas' or aux.info[4] == 'Miconos' or aux.info[4] == 'Rodas':
            insertar(vuelos_destinos, aux.info)
        # d
        # vuelos disponibles desde junio en adelante
        if aux.info[3][1] >= 6:
            insertar(vuelos_junio, aux.info)
        # b
        avion = aux.sublista.inicio
        while avion is not None:
            if avion.info[1] == 'Desocupado' and avion.info[2] == 'Turista':
                insertar(turista_disponible, aux.info)
                break
        # c
            if avion.info[1] == 'Ocupado':
                if avion.info[2] == 'Turista':
                    monto_turista += (75*km)
                else:
                    monto_pc += (203*km)
            avion = avion.sig
        montos = [aux.info[0], aux.info[1], monto_turista, monto_pc]
        insertar(monto_vuelos, montos)
        aux = aux.sig
    # e
    nro_vuelo = int(input('Ingrese el numero de vuelo: '))
    nro_as = int(input('Ingrese el numero del asiento: '))
    clase = input('Ingrese la clase: ')
    estado_asiento = 'Ocupado'
    datos_venta_pasaje = [nro_as, estado_asiento, clase]
    pos = busqueda_lista_vec(vuelos, nro_vuelo, 1)
    if pos is None:
        print('El vuelo no existe')
    else:
        aux = vuelos.inicio
        insertar(as_avion.sublista, datos_venta_pasaje)
        print('**** Se ha vendido el pasaje ****')
        print('N°Vuelo | N°Asiento | Clase')
        print(datos_venta_pasaje)
        print()
        aux = aux.sig
    # f
    eliminar_vuelo = int(input('Ingrese el numero de vuelo que desea eliminar: '))
    pos = busqueda_lista_vec(vuelos, eliminar_vuelo, 1)
    if pos is None:
        print('El vuelo no existe')
    else:
        aux = vuelos.inicio
        eliminar(vuelos, eliminar_vuelo, 1)
        lista_aux = as_avion.sublista
        print('Vuelo eliminado')
        aux = aux.sig
    print()
    print('Vuelos con destino a Atenas, Miconos o Rodas:')
    barrido_lista(vuelos_destinos)
    print()
    print('Vuelos con asientos clase turista disponible:')
    barrido_lista(turista_disponible)
    print()
    print('Recaudado por cada vuelo, turista $75 x km y primera clase $203 x km')
    print('EMPRESA | NUM. VUELO | $ TURISTA | $ PRIMERA CLASE')
    barrido_lista(monto_vuelos)
    print()
    print('Vuelos disponibles entre junio y diciembre:')
    barrido_lista(vuelos_junio)
    print()
    print('Se elimino el vuelo', eliminar_vuelo)
    print('Pasajeros del vuelo eliminado:')
    barrido_lista(lista_aux)
    print()


# EJ 18
class Usuario():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Commit():
    def __init__(self, archivo, timestamp, mensaje, cant_lineas):
        self.archivo = archivo
        self.timestamp = timestamp
        self.mensaje = mensaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        return self.archivo + ' | ' + self.timestamp + ' | ' + self.mensaje + ' | ' + str(self.cant_lineas)


def github():
    repositorio = Lista()
    user = Usuario('elchiche32')
    insertar(repositorio, user, 'nombre')
    user = Usuario('taunus99')
    insertar(repositorio, user, 'nombre')
    user = Usuario('rickyfort')
    insertar(repositorio, user, 'nombre')
    user = Usuario('oktubr3')
    insertar(repositorio, user, 'nombre')
    commit = Commit('test.py', '11-11-20 19:00', 'testeo de la app', 46)
    pos = busqueda_lista(repositorio, 'elchiche32', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('data.py', '11-11-20 19:00', 'correccion error', 120)
    pos = busqueda_lista(repositorio, 'elchiche32', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('object.java', '11-11-20 19:00', 'modelado del objeto', 0)
    pos = busqueda_lista(repositorio, 'taunus99', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('app.py', '11-11-20 19:00', 'basta chicos', -34)
    pos = busqueda_lista(repositorio, 'rickyfort', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('front.html', '11-11-20 19:00', 'update', 87)
    pos = busqueda_lista(repositorio, 'oktubr3', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('vista.css', '11-11-20 19:00', 'update', -2)
    pos = busqueda_lista(repositorio, 'oktubr3', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    # barrido lista
    print('COLABORADORES')
    barrido_lista(repositorio)
    print()
    aux = repositorio.inicio
    # barrido sublista
    while aux is not None:
        print('Colaborador:', aux.info)
        print('ARCHIVO | TIMESTAMP | COMENTARIO | LINEAS MODIFICADAS')
        barrido_sublista(aux.sublista)
        print()
        aux = aux.sig

    # a
    aux = repositorio.inicio
    mayor_commit = 0
    while aux is not None:
        if tamanio_lista(aux.sublista) > mayor_commit:
            mayor_commit = tamanio_lista(aux.sublista)
        aux = aux.sig
    aux = repositorio.inicio
    while aux is not None:
        if tamanio_lista(aux.sublista) == mayor_commit:
            print('Colaborador con mayor cantidad de commits:', aux.info)
            print('Cantidad de commits:', mayor_commit)
        aux = aux.sig
    print()

    # b
    mayor = 0
    usuario_mayor = ''
    aux = repositorio.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        mayor_aux = 0
        while sublista is not None:
            mayor_aux += sublista.info.cant_lineas
            sublista = sublista.sig
        if mayor_aux > mayor:
            mayor = mayor_aux
            usuario_mayor = aux.info.nombre
        aux = aux.sig
    print('El usuario', usuario_mayor, 'agrego la mayor cantidad de lineas:', mayor)

    menor = 0
    usuario_menor = ''
    aux = repositorio.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        menor_aux = 0
        while sublista is not None:
            menor_aux += sublista.info.cant_lineas
            sublista = sublista.sig
        if menor_aux < menor:
            menor = menor_aux
            usuario_menor = aux.info.nombre
        aux = aux.sig
    print('El usuario', usuario_menor, 'elimino la mayor cantidad de lineas:', menor)

    # c
    aux = repositorio.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista, 'test.py', 'archivo')
        if pos is not None:
            print('El usuario', aux.info, 'realizo cambios en test.py')
        aux = aux.sig

    # d
    aux = repositorio.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista, 0, 'cant_lineas')
        if pos is not None:
            print('El usuario', aux.info, 'realizo un commit con 0 lineas')
        aux = aux.sig
    print()

    # e
    aux = repositorio.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista, 'app.py', 'archivo')
        if pos is not None:
            print('El usuario', aux.info, 'realizo cambios en app.py')
            print('ARCHIVO | TIMESTAMP | COMENTARIO | LINEAS MODIFICADAS')
            barrido_sublista(aux.sublista)
        aux = aux.sig


# EJ 19
class Ventas_Naves():
    def __init__(self, codigo, producto, precio, reciclado, cliente):
        self.codigo = codigo
        self.producto = producto
        self.precio = precio
        self.reciclado = reciclado
        self.cliente = cliente

    def __str__(self):
        return str(self.codigo) + ' ; ' + self.producto + ' ; ' + str(self.precio) + ' ; ' + str(self.reciclado) + ' ; ' + self.cliente


def astillero():
    lista, lista_clientes, lista_anonimos = Lista(), Lista(), Lista()
    nombre_clientes = Lista()
    producto = ['Caza TIE', 'Destructor Estelar', 'Transporte Acorazado AT-AT',
                'Transporte de Exploración AT-ST', 'Ejecutor Táctico AT-TE']
    reciclado = [True, False]
    comprador = ['Darth Vader', 'Lando Calrissian', 'Boba Fett',
                 'Flia. Organa', 'Han Solo', 'Desconocido']
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    # a
    print('LISTA PRINCIPAL')
    print('CODIGO | PRODUCTO | PRECIO | RECIADO(V/F) | COMPRADOR')
    barrido_lista(lista)
    print()

    # b
    aux = lista.inicio
    while aux is not None:
        if aux.info.cliente == 'Desconocido':
            insertar(lista_anonimos, aux.info, 'codigo')
        else:
            insertar(lista_clientes, aux.info, 'codigo')
        aux = aux.sig
    print('Ventas a clientes habituales')
    barrido_lista(lista_clientes)
    print()
    print('Ventas a clientes desconocidos')
    if not lista_vacia(lista_anonimos):
        barrido_lista(lista_anonimos)
    else:
        print('No hay compradores anonimos')
    print()

    # c pendiente

    # d
    aux = lista.inicio
    total_ingresos = 0
    while aux is not None:
        total_ingresos += aux.info.precio
        aux = aux.sig
    print('Cantidad de unidades vendidas:', tamanio_lista(lista))
    print('Ingresos totales:', total_ingresos, 'creditos galácticos')
    print()

    # e
    aux = lista.inicio
    while aux is not None:
        nombre = aux.info.cliente
        pos = busqueda_lista(nombre_clientes, nombre)
        if pos is None:
            insertar(nombre_clientes, nombre)
        aux = aux.sig
    print('Listado de clientes:')
    barrido_lista(nombre_clientes)
    print()

    # f
    aux = lista.inicio
    print('Compras realizadas por Darth Vader')
    while aux is not None:
        if aux.info.cliente == 'Darth Vader':
            print(aux.info)
        aux = aux.sig
    print()

    # g
    aux = lista.inicio
    print('Descuento del 15% a los clientes que compraron naves con partes recicladas')
    while aux is not None:
        if aux.info.reciclado is True:
            descuento = aux.info.precio * 15 / 100
            print('Al cliente', aux.info.cliente, 'se le deben reintegrar', descuento, 'creditos')
        aux = aux.sig
    print()

    # h
    aux = lista.inicio
    ingresos_at = 0
    while aux is not None:
        pos = busqueda_lista(lista, 'AT', 'producto')
        if pos is None:
            ingresos_at += aux.info.precio
        aux = aux.sig
    print('La venta de naves modelo AT generó', ingresos_at, 'creditos')


# EJ 20
class Estacion():
    def __init__(self, estacion, pais, latitud, longitud, altitud):
        self.estacion = estacion
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def __str__(self):
        return self.estacion + '  |  ' + self.pais + '  |  ' + str(self.latitud) + '  |  ' + str(self.longitud) + '  |  ' + str(self.altitud)


class Medicion():
    def __init__(self, temperatura, presion, humedad, estado, fecha, hora):
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
        self.estado = estado
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return str(self.temperatura) + '  |  ' + str(self.presion) + '  |  ' + str(self.humedad) + ' | ' + self.estado + ' | ' + str(self.fecha) + ' | ' + str(self.hora)


def empresa_meteorologica():
    lista = Lista()
    paises = ['Myanmar', 'Laos', 'Vietnam', 'Indonesia', 'Malasia',
              'Singapur', 'Brunei', 'Sri Lanka']
    estado = ['soleado', 'nublado', 'lloviendo', 'nevando', 'tormenta eléctrica', 'huracanes']
    datos = Estacion('Invierno', choice(paises), randint(-90, 90), randint(-180, 180), randint(0, 2000))
    insertar(lista, datos, 'estacion')
    datos = Estacion('Otoño', choice(paises), randint(-90, 90), randint(-180, 180), randint(0, 2000))
    insertar(lista, datos, 'estacion')
    datos = Estacion('Primavera', choice(paises), randint(-90, 90), randint(-180, 180), randint(0, 2000))
    insertar(lista, datos, 'estacion')
    datos = Estacion('Verano', choice(paises), randint(-90, 90), randint(-180, 180), randint(0, 2000))
    insertar(lista, datos, 'estacion')
    for i in range(1):
        datos = Medicion(randint(0, 10), randint(700, 800), randint(0, 100), choice(estado), date(2020, randint(1, 12), randint(1, 30)), time((randint(00, 23)), (randint(00, 59))))
        pos = busqueda_lista(lista, 'Invierno', 'estacion')
        insertar(pos.sublista, datos, 'estacion')
    for i in range(1):
        datos = Medicion(randint(10, 25), randint(700, 800), randint(0, 100), choice(estado), date(2020, randint(1, 12), randint(1, 30)), time((randint(00, 23)), (randint(00, 59))))
        pos = busqueda_lista(lista, 'Otoño', 'estacion')
        insertar(pos.sublista, datos, 'estacion')
    for i in range(1):
        datos = Medicion(randint(15, 30), randint(700, 800), randint(0, 100), choice(estado), date(2020, randint(1, 12), randint(1, 30)), time((randint(00, 23)), (randint(00, 59))))
        pos = busqueda_lista(lista, 'Primavera', 'estacion')
        insertar(pos.sublista, datos, 'estacion')
    for i in range(1):
        datos = Medicion(randint(20, 40), randint(700, 800), randint(0, 100), choice(estado), date(2020, randint(1, 12), randint(1, 30)), time((randint(00, 23)), (randint(00, 59))))
        pos = busqueda_lista(lista, 'Verano', 'estacion')
        insertar(pos.sublista, datos, 'estacion')
    # a
    print(' ESTACION | PAIS | LATITUD | LONGUITD | ALTITUD')
    barrido_lista(lista)
    print()

    # b
    aux = lista.inicio
    while aux is not None:
        print('Estacion:', aux.info.estacion)
        print('Pais:', aux.info.pais)
        print('TEMP. | PRESION | HUMEDAD | ESTADO |   FECHA   |   HORA   ')
        barrido_sublista(aux.sublista)
        print()
        aux = aux.sig
    print()

    # c
    aux = lista.inicio
    prom_temperatura = 0
    prom_humedad = 0
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            prom_temperatura += sublista.info.temperatura
            prom_humedad += sublista.info.humedad
            sublista = sublista.sig
        aux = aux.sig
    print('Promedio de temperatura:', prom_temperatura / tamanio_lista(lista))
    print('Promedio de humedad:', prom_humedad / tamanio_lista(lista))
    print()

    # d
    aux = lista.inicio
    while aux is not None:
        lluvia = busqueda_lista(aux.sublista, 'lloviendo', 'estado')
        if lluvia is not None:
            print('En', aux.info.pais, 'esta lloviendo')
        nieve = busqueda_lista(aux.sublista, 'nevando', 'estado')
        if nieve is not None:
            print('En', aux.info.pais, 'esta nevando')
        aux = aux.sig
    print()

    # e
    aux = lista.inicio
    while aux is not None:
        tormenta = busqueda_lista(aux.sublista, 'tormenta eléctrica', 'estado')
        if tormenta is not None:
            print(' ESTACION | PAIS | LATITUD | LONGUITD | ALTITUD')
            print(aux.info, ', se registraron tormentas eléctricas')
            print()
        huracan = busqueda_lista(aux.sublista, 'huracanes', 'estado')
        if huracan is not None:
            print(' ESTACION | PAIS | LATITUD | LONGUITD | ALTITUD')
            print(aux.info, ' , se registraron huracanes')
            print()
        aux = aux.sig
    print()


# EJ 21
class Peliculas():
    def __init__(self, nombre, valoracion, año_estreno, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.año_estreno = año_estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return self.nombre + '  |  ' + str(self.valoracion) + '  |  ' + str(self.año_estreno) + ' | ' + str(self.recaudacion)


def lista_peliculas():
    lista, lista_ranking = Lista(), Lista()
    datos = Peliculas('El Padrino', randint(0, 10), 1972, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('Goodfellas', randint(0, 10), 1990, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('El Irlandés', randint(0, 10), 2019, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('Casino', randint(0, 10), 1995, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('Sicario', randint(0, 10), 2015, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    print('   NOMBRE   |  VALORACION(0-10) |  AÑO DE ESTRENO | RECAUDACION(USD)')
    barrido_lista(lista)
    print()

    # a
    aux = lista.inicio
    buscado = int(input('Ingrese un año de estreno: '))
    while aux is not None:
        if buscado == aux.info.año_estreno:
            print(aux.info.nombre, 'se estreno en el año', buscado)
        aux = aux.sig
    print()

    # b
    mas_recuadacion = 0
    mayor_peli = ''
    aux = lista.inicio
    while aux is not None:
        if aux.info.recaudacion > mas_recuadacion:
            mayor_peli = aux.info
        aux = aux.sig
    print('Pelicula que mas recaudo y sus datos')
    print(' NOMBRE  | VALORACION(0-10)| AÑO DE ESTRENO | RECAUDACION(USD)')
    print(mayor_peli)
    print()

    # c
    aux = lista.inicio
    mas_valor = 0
    while aux is not None:
        if aux.info.valoracion > mas_valor:
            mas_valor = aux.info.valoracion
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if aux.info.valoracion == mas_valor:
            print(aux.info.nombre, 'tiene la valoracion mas alta,', mas_valor, 'puntos')
        aux = aux.sig
    print()

    # d
    print('Ingrese criterio de orden: ')
    print('* nombre')
    print('* valoracion')
    print('* año_estreno')
    print('* recaudacion')
    criterio = input()
    aux = lista.inicio
    while aux is not None:
        insertar(lista_ranking, aux.info, criterio)
        aux = aux.sig
    print()
    if criterio == 'nombre':
        print('Lista ordenada por nombre:')
        barrido_lista(lista_ranking)
    elif criterio == 'valoracion':
        print('Lista ordenada por valoracion:')
        barrido_lista(lista_ranking)
    elif criterio == 'año_estreno':
        print('Lista ordenada por año de estreno:')
        barrido_lista(lista_ranking)
    elif criterio == 'recaudacion':
        print('Lista ordenada por recaudacion:')
        barrido_lista(lista_ranking)