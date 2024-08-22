import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#contador cada vez que se agregue un ave tenga un identificador unico
id = 1

datosAves = [
    {#Informacion de caracteristicas objetos dentro de una lista
        #un diccionario con listas
        "id": id,
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
        "id": id,
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
        "id": id,
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
        "id": id,
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
    #se crea una lista vacia de diccionarios, para guardar informacion
    datos= []
    #es necesario organizar la data en diccionarios para que el dataframe lo reconcosxa
    for ave in datosAves:
        #recorrer una lista porque es una lsita se recorre con bucle
        # cada resevacionn es un diccionarios se especifica la fecha para que lo haga en lista de fechas
        rsvFecha = [rsv["fecha"] for rsv in ave["reservaciones"]]
        rsvLugar = [rsv["lugar"] for rsv in ave["reservaciones"]]
        rsvCosto = [rsv["costo"] for rsv in ave["reservaciones"]]
        #almacenamos los diccionarios
        datos.append({
            #las claves son las columnas
            "ID": ave["id"],
            "Nombre": ave["nombre"],
            "Ubicacion": ave["descripcion"]["ubicacion"],
            "Caracteristica": ave["descripcion"]["caracteristica"],
            "DatoCurioso": ave["descripcion"]["datoCurioso"],
            "NombreCientifico": ave["descripcion"]["nombreCientifico"],
            "Fotos": ", ".join(ave["multimedia"]["fotos"]),
            #map convierte la lista para que la concatenacion se correcta
            #convertir los tipos de datos de cada unos de los elementos de la lista#son map
            "Fecha": ", ".join(map(str, rsvFecha)),
            "Lugar": ", ".join(map(str, rsvLugar)),
            "Costo": ", ".join(map(str, rsvCosto)),
        })
        
    df = pd.DataFrame(datos)
    pd.set_option("display.max_columns", None)
    print(df)

def agregarAves():
    #es un objeto
    #para trabajar con una variable global no local
    global id
    #incremento 
    id += 1

    nombre = input("Ingrese el nombre del Ave: ")

    descripcion = {}
    descripcion["ubicacion"] = input("Ingrese la nueva ubicacion: ")
    descripcion["caracteristica"] = input("Ingrese la caracteristica principal: ")
    descripcion["datoCurioso"] = input("Ingrese un dato curioso: ")
    descripcion["nombreCientifico"] = input("Ingrese el nombre cientifico: ")

    multimedia = {} #se usa .split funcion parar separa elementos y crear una lista 
    multimedia["fotos"] = input("ingrese las rutas de las fotos, separadas por comas: ").split(",")
    #Lista vacia
    reservaciones = []
    #para guardar reservaciones se necita un bucle
    while True:
        reservacion = {}
        reservacion["fecha"] = input("Ingrese la fecha de reservacion (YYYY-MM-DD) o 'fin' para terminar: ")

        if reservacion["fecha"].lower() == "fin":
            break

        reservacion["lugar"] = input("Ingrese el lugar de reservacion: ")
        reservacion["costo"] = int(input("Ingrese el costo de la reserva o preuspuesto: "))
    
        reservaciones.append(reservacion)
    #Diccionario para reemplazar su contenido
    # nuevaAve = {"id": id, }
    # nuevaAve["nombre"] = nombre
    # nuevaAve["descripcion"] = descripcion
    # nuevaAve["multimedia"] = multimedia
    # nuevaAve["reservaciones"] = reservaciones

    #se agrega directamente a la funcion
    datosAves.append({
        "id": id,
        "nombre": nombre,
        "descripcion": descripcion,
        "multimedia": multimedia,
        "reservaciones": reservaciones,
    })

    print("Ave agreagada exitosamente. ")

def actualizarAve():
    
    idAve = int(input("Ingrese el ID de la ave que desea actualizar: "))
    #bandera en vez de contador 0 un verdadero o un falso
    aveEncontrada = False

    for ave in datosAves:
        if ave["id"] == idAve:
            aveEncontrada = True

            print("Seleccione el campo que desea actualizar: ")
            print("1. Descripción")
            print("2. Multimedia")
            print("3. Reservaciones")

            opcion = input("Inrese una de las opciones: ")

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
                    reservacion = {}
                    reservacion["fecha"] = input("Ingrese la nueva fecha de reservacion (YYYY-MM-DD) o 'fin' para terminar: ")

                    if reservacion["fecha"].lower() == "fin":
                        break

                    reservacion["lugar"] = input("Ingrese el nuevo lugar de reservacion: ")
                    reservacion["costo"] = int(input("Ingrese el nuevo costo de la reserva o preuspuesto: "))
                    
                    reservaciones.append(reservacion)

                ave["reservaciones"] = reservaciones

            print("Datos del Ave actualizada existosamente.")

            return
    #si se niega se convierte en verdadera
    if not aveEncontrada: 
        print("Ave no encontrado. ")

def eliminarAve():
    idAve = int(input("Ingrese el ID del ave que desea eliminar: "))

    longitudAnterior = len(datosAves)
    #operacion ternario
    datosAves[:] = [ave for ave in datosAves if ave["id"] != idAve]

    if len(datosAves) < longitudAnterior:
        print("Ave eliminada.")
    else:
        print("Ave no encontrada. ")

def analisisDatos():
    reservaciones = []

    for ave in datosAves:
        for rsv in ave["reservaciones"]:
            reservaciones.append({
                "Nombre": ave["nombre"],
                "Fecha": rsv["fecha"],
                "Lugar": rsv["lugar"],
                "Costo": rsv["costo"]
            })
    
    df = pd.DataFrame(reservaciones)
    
    if df.empty:
        print("No hay datos disponibles para un analisis.")
        return
    
    print("\nAnalisis de datos.")
    print("\nEstadisticas descriptivas: (antes de la limpieza)")

    #funcion para analizar la data
    print(df.describe(include="all"))
    #eliminar datos duplicados
    df = df.drop_duplicates()
    #filas con valores nulos
    df = df.dropna(subset=["Fecha", "Nombre"])
    #llene los nulos con la media
    df["Costo"] = df["Costo"].fillna(df["Costo"].median())
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    #Filtrar el dataframe 
    df = df[(df["Costo"] > 0) & (df["Costo"] <= 10000000)]

    print("\nEstadisticas descriptivas: (despues de la limpieza)")
    print(df.describe(include="all"))
#id sera nuestra fecha
    df.set_index("Fecha", inplace = True)
    
#sumar el datos por el mes
    print("\nTendencias a lo largo del tiempo por mes: ")
    tendencias = df.resample("ME").sum(numeric_only = True)
    print(tendencias)

#agrupamiento por lugar
    print("\nDistribucion de costos por lugar: ")
    lugar = df.groupby("Lugar").sum(numeric_only = True)
    print(lugar)

#agrupamiento por nombre
    print("\nCostos promedios por mes: ")
    nombre = df.groupby("Nombre").mean(numeric_only = True)
    print(nombre)

#Figuras 
    print("Creando figura...")
    fig = plt.figure(figsize=(14, 10))
    fig.canvas.manager.set_window_title("Analisis de datos ZooTourist")

    plt.subplot(2, 2, 1)

    tendencias["Costo"].plot(kind="line", color="purple", marker="o", alpha=0.7)

    plt.title("Tendencias a lo largo del tiempo por mes: ")
    plt.xlabel("Lugar")
    plt.ylabel("Costo")

    plt.subplot(2, 2, 2)

    lugar["Costo"].plot(kind="bar", color="blue")

    plt.title("Distribucion de costos por lugar: ")
    plt.xlabel("Lugar")
    plt.ylabel("Costo")

    plt.subplot(2, 2, 3)

    nombre["Costo"].plot(kind="hist", color="red", alpha=0.7, bins= 10)
    plt.title("Costos promedios por mes: ")
    plt.xlabel("costo promedio")
    plt.ylabel("Costo")

    plt.subplot(2, 2, 4)

    nombre["Costo"].plot(kind="pie", color="red", startangle=90)
    colores = plt.cm.Paired(np.arange(len(nombre))) 
    plt.title("Costos promedios por especie: ")
    plt.ylabel("Costo")

    plt.tight_layout()
    manager = plt.get_current_fig_manager()
    manager.window.state("zoomed")
    plt.show()

def cargarDatosCSV():
    #Variables globales
    global id, datosAves
    #Lectura del archivo CSV
    try:
        df = pd.read_csv("datos_aves.csv")

        datosAves = []
        aves = {}

        for _, row in df.iterrows():
            idAve = row["ID"]

            if idAve not in aves:

                aves[idAve] = {             
                    "id": idAve,
                    "nombre": row["Nombre"],
                    "descripcion": {
                        "ubicacion" : row["Ubicacion"],
                        "caracteristica": row["Caracteristica"],
                        "datoCurioso": row["DatoCurioso"],
                        "nombreCientifico": row["NombreCientifico"]
                    },#con multimedia es un objeto donde cada atributo tiene listas
                    #un objeto que contiene listas
                    "multimedia": {
                        "fotos": row["Fotos"].split(", ")
                    },#una lista vacia
                    "reservaciones": []
                
                }
                #Colibri Esmeralda
                {   
                    "id": idAve,
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

                }
                #Aguila de montaña
                {   
                    "id": id,
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

                }
                #Carpintero Dorado
                {   
                    "id": id,
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

                }
                

                
            aves[idAve]["reservaciones"].append({
                    "fecha": row["Fecha"], 
                    "lugar": row["Lugar"],
                    "costo": row["Costo"],
                })
            
        datosAves = list(aves.values())
        id = max(aves.keys())

        print("Datos guardados desde csv")

    except FileNotFoundError:
        print("Archivo 'datos_aves.csv' no encontrado. Generando nuevos datos.")
                        #generarDatos(datosAves, 5)

def guardarDatos():
    datos = []

    for ave in datosAves:
        for rsv in ave["reservaciones"]:
            datos.append({
                "ID": ave["id"],
                "Nombre": ave["nombre"],
                "Ubicacion": ave["descripcion"]["ubicacion"],
                "Caracteristica": ave["descripcion"]["caracteristica"],
                "DatoCurioso": ave["descripcion"]["datoCurioso"],
                "NombreCientifico": ave["descripcion"]["nombreCientifico"],
                "Fotos": ", ".join(ave["multimedia"]["fotos"]),            #convertir los tipos de datos de cada unos de los elementos de la lista#son map
                "Fecha": rsv["fecha"],
                "Lugar": rsv["lugar"],
                "Costo": rsv["costo"],
            })
    df = pd.DataFrame(datos)
    df.to_csv("datos_aves.csv", index=False)

    print("datos guardados en 'datos_aves.csv' exitosamente. ")

def menu():
    cargarDatosCSV()

    while True:
            
        print("\nMenu de gestion de Aves:")
        print("1. Ver todas las Aves")
        print("2. Agregar nueva Ave")
        print("3. Actualizar datos de un Ave")
        print("4. Eliminar un Ave")
        print("5. Analisis de datos")
        print("6. Guardar datoss")
        print("7. Salir")

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
            analisisDatos()
        
        elif opcion == "6":
            guardarDatos()

        elif opcion == "7":
            print("Salir")
            break
        else:
            print("Opción no valida.")

menu()
