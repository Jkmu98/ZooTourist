
datosMamiferos = [
    #Informacion de caracteristicas de objetos dentro de una lista
    #un diccionario con listas
    {
        "nombre": "Oso de Anteojos",
        "descripcion": {
            "ubicacion" : "Bogotá, Sesquilé, Machetá, Guatavita, Parques Nacionales Naturales Chingaza y Sumapaz.",
            "caracteristica": "Manchas blancas en sus ojos",
            "datoCurioso": "Los machos adultos alcanzan un tamaño de entre 100 y 200 kilogramos, mientras que las hembras adultas pesan entre 30 y 85 kilogramos.",
            "nombreCientifico": "Tremarctos ornatus"
        },#con multimedia es un objeto donde cada atributo tiene listas
        #un objeto que contiene listas
        "multimedia": {
            "fotos": ["img/huella.png", "ruta/foto2.jpg"]
        },#una lista donde contien objetos
        "reservaciones": [
            {"fecha": "2024-08-02", "lugar": "Parque Nacional Chingaza", "costo": 50000},
            {"fecha": "2024-08-10", "lugar": "Cundinamarca", "costo": 30000}
        ]

    },
    #puma o puma concolor
    {
        "nombre": "Puma o Puma Concolor",
        "descripcion": {
            "ubicacion" : "Boyaca, las veredas Llanos, Cañadas, Barbosa, Fuguntá, Tenguavita y Gusvita en el municipio de Tibirita, en la región de Almeidas.",
            "caracteristica": "Pelaje dorado y garras retractiles.",
            "datoCurioso": "Realiza saltos verticales de hasta 5,4 metros y persecuciones de carreras cortas.",
            "nombreCientifico": "Puma concolor"
        },
        "multimedia": {
            "fotos": ["img/huella.png", "ruta/foto2.jpg"]
        },
        "reservaciones": [
            {"fecha": "2024-10-02", "lugar": "Tibirita", "costo": 70000},
            {"fecha": "2024-09-10", "lugar": "Altiplano Cundiboyacense", "costo": 50000}
        ]

    },
    #Venado de cola blanca
    {
        "nombre": "Venado de cola Blanca.",
        "descripcion": {
            "ubicacion" : "Parques Nacionales Naturales Chingaza y Sumapaz. Sur oriente de Boyáca.",
            "caracteristica": "Es reconocido por su cola blanca",
            "datoCurioso": "Los machos de venado cola blanca generalmente se encuentran solos, mientras que las hembras prefieren permanecer en pequeños rebaños",
            "nombreCientifico": "Odocoileus virginianus"
        },
        "multimedia": {
            "fotos": ["img/huella.png", "ruta/foto2.jpg"]
        },
        "reservaciones": [
            {"fecha": "2024-08-02", "lugar": "Tunja", "costo": 80000},
            {"fecha": "2024-08-10", "lugar": "Cundinamarca", "costo": 60000}
        ]

    },
    #Tapir andino
    {
        "nombre": "Tapir Andino",
        "descripcion": {
            "ubicacion" : "El tapir andino se encuentra en los bosques nubosos y páramos de las cordilleras oriental y central de Colombia.",
            "caracteristica": "El peso varía entre 90 y 180 kg, aunque los ejemplares más grandes pueden llegar a los 260 kg.",
            "datoCurioso": "Mide en promedio 180 cm de largo y entre 75 y 90 cm de alto. Las hembras son algo más grandes y pueden medir hasta 200 cm de largo y más de 90 cm de alto.",
            "nombreCientifico": "Tapirus pinchaque"
        },
        "multimedia": {
            "fotos": ["img/huella.png", "ruta/foto2.jpg"]
        },
        "reservaciones": [
            {"fecha": "2024-08-02", "lugar": "Coordillera Oriental", "costo": 90000},
            {"fecha": "2024-08-10", "lugar": "Parque Nacional Sumapaz", "costo": 100000}
        ]

    }
]

def mostrarMamifero():
    print("Mostrar Mamifero")
    print(datosMamiferos)

def agregarMamifero():
    print("Agregar Mamifero")
    #es un objeto
    nuevoMamifero = {}

    nombre = input("Ingrese el nombre del mamifero: ")

    descripcion = {}
    descripcion["ubicacion"] = input("Ingrese la nueva ubicacion: ")
    descripcion["caracteristica"] = input("Ingrese la caracteristica principal: ")
    descripcion["datoCurioso"] = input("Ingrese un datos curioso: ")
    descripcion["nombreCientifico"] = input("Ingrese el nombre cientifico: ")

    nuevoMamifero["nombre"] = nombre
    nuevoMamifero["descripcion"] = descripcion

    multimedia = {} #se usa .split funcion parar separa elementos y crear una lista 
    multimedia["fotos"] = input("ingrese las rutas de las fotos, separadas por comas: ").split(",")
    nuevoMamifero["multimedia"] = multimedia

    reservaciones = []
    #para guardar onservaciones se necita un bucle
    while True:
        res = input("¿Desea agregar otra reservacion?: \n1. si \n2. no:")
        if res == "2":
            break

        reservacion = {}
        reservacion["fecha"] = input("Ingrese la fecha de reservacion (YYYY-MM-DD): ")
        reservacion["lugar"] = input("Ingrese el lugar de reservacion: ")
        reservacion["costo"] = int(input("Ingrese el costo de la reservacion o el presupuesto: "))

        reservaciones.append(reservacion)

       
    nuevoMamifero["reservaciones"] = reservaciones

    datosMamiferos.append(nuevoMamifero)

    print("Mamifero Agregado. ")
   

def actualizarMamifero():
    print("Actualizar Mamifero")
    nombre = input("Ingrese el nombre: ")
    #bandera en vez de contador 0 un verdadero o un falso
    mamiferoEncontrado = False

    for mamifero in datosMamiferos:
        if mamifero["nombre"] == nombre:
            mamiferoEncontrado = True
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
                mamifero["descripcion"] = descripcion

            elif opcion == "2":
                multimedia = {} #se usa .split funcion parar separa elementos y crear una lista 
                multimedia["fotos"] = input("ingrese las rutas de las fotos, separadas por comas: ").split(",")
                mamifero["multimedia"] = multimedia

            elif opcion == "3":
                reservaciones = []
                #para guardar onservaciones se necita un bucle
                while True:
                    res = input("¿Desea agregar otra observacion?: \n1. si \n2. no:")
                    if res == "2":
                        break

                    reservacion = {}
                    reservacion["fecha"] = input("Ingrese la fecha de reservacion (YYYY-MM-DD): ")
                    reservacion["lugar"] = input("Ingrese el lugar de reservacion: ")
                    reservacion["costo"] = int(input("Ingrese el costo de la reservacion o el presupuesto: "))

                    reservaciones.append(reservacion)
                mamifero["observaciones"] = reservaciones


                print("Mamifero Actualizado")

    #si se niega se convierte en verdadera
    if not mamiferoEncontrado: 
        print("Nombre no encontrado. ")


def eliminarMamifero():
    print("Eliminar Mamifero")

    nombre = input("Ingrese el nombre del mamifero que desea eliminar: ")
    longitudAnterior = len(datosMamiferos)
    #operacion ternario
    datosMamiferos[:] = [mamifero for mamifero in datosMamiferos if mamifero["nombre"] != nombre]
    if len(datosMamiferos) < longitudAnterior:
        print("Mamifero eliminado.")
    else:
        print("Nombre del mamifero no encontrado. ")
#funcion menu
def menu():
    while True:
            
        print("\nMenu de gestion de Mamiferos:")
        print("1. Ver todas los mamiferos")
        print("2. Agregar un nuevo mamifero")
        print("3. Actualizar datos de un mamifero")
        print("4. Eliminar un mamifero")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrarMamifero()

        elif opcion == "2":
            agregarMamifero()

        elif opcion == "3":
            actualizarMamifero()
        
        elif opcion == "4":
            eliminarMamifero()
        
        elif opcion == "5":
            print("Salir")
            break
        else:
            print("Opción no valida.")

menu()
        