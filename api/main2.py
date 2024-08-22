
datosAves = [
    {#Informacion de caracteristicas objetos dentro de una lista
        #un diccionario con listas
        "nombre": "Condor Andino",
        "descripcion": {
            "ubicacion" : "Parque Nacional Natural Los Nevados, Páramo de San Lorenzo, el Páramo de la Cumbre y el Páramo de Sabana Rubia. Paramo del Almorzadero (santander)",
            "caracteristica": "Manchas blancas en sus ojos",
            "datoCurioso": "Puede alcanzar más de 140 centímetros de altura y más de 300 centímetros de envergadura.",
            "nombreCientifico": "Vultur gryphus"
        },#con multimedia es un objeto donde cada atributo tiene listas
        #un objeto que contiene listas
        "multimedia": {
            "fotos": ["img/huella.png", "ruta/foto2.jpg"]
        },#una lista donde contiene objetos
        "reservaciones": [
            {"fecha": "2024-08-02", "lugar": "Parque Nacional Natural Los Nevados", "costo": 120000},
            {"fecha": "2024-08-10", "lugar": "Paramo del Almorzadero (santander)", "costo": 100000}
        ]

    },
    #Colibri Esmeralda
    {
        "nombre": "Colibri Esmeralda",
        "descripcion": {
            "ubicacion" : "Jardin Encantado San Francisco (San Francisco, Cundinamarca). Jardín Botánico José Celestino Mutis, (Bogotá). Jardin Botanico del Quindio (Calarca). Jardin Botanico Joaquin Antonio Uribe (Medellin).",
            "caracteristica": "Su tamaño es de entre 9 y 10 centímetros.",
            "datoCurioso": "Como la mayoría de colibríes, su color depende de las condiciones luminícas del entorno.",
            "nombreCientifico": "Amacilia Luciae"
        },
        "multimedia": {
            "fotos": ["img/huella.png", "ruta/foto2.jpg"]
        },
        "reservaciones": [
            {"fecha": "2024-07-22", "lugar": "ardin Encantado San Francisco (San Francisco, Cundinamarca)", "costo": 140000},
            {"fecha": "2024-07-16", "lugar": "Jardin Botanico Joaquin Antonio Uribe (Medellin)", "costo": 95000}
        ]

    },
    #Aguila de montaña
    {
        "nombre": "Aguila de Montaña",
        "descripcion": {
            "ubicacion" : "Parque natural Regional Paramo de las Oseras (Huila). Páramo Mamapacha Bijagua (Altiplano Cundiboyacense).",
            "caracteristica": "Es la tercer águila más grande de Colombia, midiendo entre 60 y 80 cm.",
            "datoCurioso": "El Águila Real puede alcanzar velocidades impresionantes mientras caza, llegando a alcanzar los 240 km/h.",
            "nombreCientifico": "Spizaetus isidori"
        },
        "multimedia": {
            "fotos": ["img/huella.png", "ruta/foto2.jpg"]
        },
        "reservaciones": [
            {"fecha": "2024-06-12", "lugar": "Páramo Mamapacha Bijagua (Altiplano Cundiboyacense).", "costo": 150000},
            {"fecha": "2024-06-30", "lugar": "Parque natural Regional Paramo de las Oseras (Huila)", "costo": 130000}
        ]

    },
    #Carpintero Dorado
    {
        "nombre": "Carpintero Dorado",
        "descripcion": {
            "ubicacion" : "Cascada de Los Caballeros (Santander Suaita). Reserva Natural El Dorado y San Lorenzo.",
            "caracteristica": "Son aves trepadoras de árboles y por picotear sus cortezas.",
            "datoCurioso": " Los machos tienen plumaje rojo en la cabeza, mientras que las hembras varían entre verde oliva y amarillo.",
            "nombreCientifico": "Piculus chrysochloros"
        },
        "multimedia": {
            "fotos": ["img/huella.png", "ruta/foto2.jpg"]
        },
        "reservaciones": [
            {"fecha": "2024-10-02", "lugar": "Cascada de Los Caballeros (Santander Suaita).", "costo": 350000},
            {"fecha": "2024-08-19", "lugar": "Reserva Natural El Dorado y San Lorenzo.", "costo": 130000}
        ]

    },
]

def mostrarAves():
    print("Mostrar Aves")
    print(datosAves)

def agregarAves():
    print("Agrergar Aves")
    #es un objeto
    nuevaAve = {}

    nombre = input("Ingrese el nombre del Ave: ")

    descripcion = {}
    descripcion["ubicacion"] = input("Ingrese la nueva ubicacion: ")
    descripcion["caracteristica"] = input("Ingrese la caracteristica principal: ")
    descripcion["datoCurioso"] = input("Ingrese un datos curioso: ")
    descripcion["nombreCientifico"] = input("Ingrese el nombre cientifico: ")

    nuevaAve["nombre"] = nombre
    nuevaAve["descripcion"] = descripcion

    multimedia = {} #se usa .split funcion parar separa elementos y crear una lista 
    multimedia["fotos"] = input("ingrese las rutas de las fotos, separadas por comas: ").split(",")
    nuevaAve["multimedia"] = multimedia

    reservaciones = []
    #para guardar onservaciones se necita un bucle
    while True:
        res = input("¿Desea agregar otra reservacion?: \n1. si \n2. no:")
        if res == "2":
            break

        reservacion = {}
        reservacion["fecha"] = input("Ingrese la fecha de reservacion (YYYY-MM-DD): ")
        reservacion["lugar"] = input("Ingrese el lugar de reservacion: ")
        reservacion["costo"] = int(input("Ingrese el costo de la reserva o preuspuesto: "))

        reservaciones.append(reservacion)
    nuevaAve["reservaciones"] = reservaciones

    datosAves.append(nuevaAve)

    print("Ave agreagada. ")
   
def actualizarAve():
    print("Actualizar aves")
    nombre = input("Ingrese el nombre común: ")
    #bandera en vez de contador 0 un verdadero o un falso
    aveEncontrada = False

    for ave in datosAves:
        if ave["nombreComun"] == nombre:
            aveEncontrada = True
            print("Seleccione el campo que desea actualizar: ")
            print("1. Descripcción")
            print("2. Multimedia")
            print("3. Reservacion")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                descripcion = {}
                descripcion["ubicacion"] = input("Ingrese la nueva ubicacion: ")
                descripcion["caracteristica"] = input("Ingrese la caracteristica principal: ")
                descripcion["datoCurioso"] = input("Ingrese un datos curioso: ")
                descripcion["nombreCientifico"] = input("Ingrese el nombre cientifico: ")
                ave["descripcion"] = descripcion

            elif opcion == "2":
                multimedia = {} #se usa .split funcion parar separa elementos y crear una lista 
                multimedia["fotos"] = input("ingrese las rutas de las fotos, separadas por comas: ").split(",")
                ave["multimedia"] = multimedia

            elif opcion == "3":
                reservaciones = []
                #para guardar onservaciones se necita un bucle
                while True:
                    res = input("¿Desea agregar otra observacion?: \n1. si \n2. no:")
                    if res == "2":
                        break

                    reservacion = {}
                    reservacion["fecha"] = input("Ingrese la fecha de reservacion (YYYY-MM-DD): ")
                    reservacion["lugar"] = input("Ingrese el lugar de observacion: ")
                    reservacion["costo"] = int(input("Ingrese el numero de avisatmientos: "))
                    
                    reservaciones.append(reservacion)
                ave["observaciones"] = reservaciones
                print("Ave actualizada")
    #si se niega se convierte en verdadera
    if not aveEncontrada: 
        print("Nombre no encontrado. ")


def eliminarAve():
    print("Eliminar Aves")

    nombre = input("Ingrese el nombre del ave que desea eliminar: ")
    longitudAnterior = len(datosAves)
    #operacion ternario
    datosAves[:] = [ave for ave in datosAves if ave["nombre"] != nombre]
    if len(datosAves) < longitudAnterior:
        print("Ave eliminada.")
    else:
        print("Nombre de ave no encontrado. ")
#funcion menu
def menu():
    while True:
            
        print("\nMenu de gestion de Aves:")
        print("1. Ver todas las Aves")
        print("2. Agregar nueva Ave")
        print("3. Actualizar datos de un Ave")
        print("4. Eliminar un Ave")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrarAves()

        elif opcion == "2":
            agregarAves()

        elif opcion == "3":
            actualizarAve()
        
        elif opcion == "4":
            eliminarAve()
        
        elif opcion == "5":
            print("Salir")
            break
        else:
            print("Opción no valida.")

menu()
        