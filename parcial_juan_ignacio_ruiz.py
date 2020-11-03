import csv
import os

def pedirNombre():
    while True:
        nombre = input("Se creará un archivo \n\tingrese nombre del archivo que desea crear:  ")
        try:
            return str(f"{nombre}.csv")
        except ValueError:
            print("error al nombrar archivo")


def cargardatos(archivo,campos):
    guardar = "si"
    filasCarga = []
    while guardar == "si":
        empleado = {}

        for campo in campos:
            empleado[campo] = input(f"Ingrese {campo} del Empleado: ")
        filasCarga.append(empleado)
        guardar = input("Desea seguir agregando empleados? Si/No")

    try:
        # nombreArchivo = pedirNombre()
        hayAlgunArchivo = os.path.isfile(archivo)
        with open(archivo, 'w+', newline='') as file:
            archivoAGrabar = csv.DictWriter(file, fieldnames=campos)

            if not hayAlgunArchivo:
                archivoAGrabar.writeheader()

            archivoAGrabar.writerows(filasCarga)
            print("Empleado Cargado Exitosamente!")
            return
    except IOError:
        print("no se reconoce el archivo.")

def recuperarVacacionesPendientes(archivo, legajos):
    archivoLegajos = "legajo.csv"

    archivoLegajos = open(archivoLegajos)
    archivo = open(archivo)
    archivoLegajosCSV = csv.reader(archivoLegajos, delimiter=",")
    archivo1CSV = csv.reader(archivo)


    next(archivoLegajosCSV)
    next(archivo1CSV)

    busqueda = input("ingrese numero de legajo a buscar: ")

    empleado = next(archivo1CSV, None)
    legajo = next(archivoLegajosCSV, None)
    while (empleado):
        diasRestantes = 0
        contador = 0
        numLegajo = empleado[0]
        apellidoEmple = empleado[1]
        nombreEmple = empleado[2]
        totalVacaciones = empleado[3]

        # print(f"{empleado}")
        # print(f"{legajo}")
        print(f"legajo Nro: {empleado[0]} ,empleado: {empleado[1]}, {empleado[2]}")
        # if empleado or legajo != empleado[0]:

        restante = 0
        for linea in legajo:
            if busqueda in linea:

                contador+=1
                restante = int(totalVacaciones)-contador
            linea = linea.rstrip('\n')
            print(f"\ttiene {totalVacaciones} dias de Vacaciones en total, debe {restante}")
            print("**************************************************************************")


        legajo = next(archivoLegajosCSV, None)
        empleado = next(archivo1CSV, None)

    archivoLegajos.close()
    archivo.close()
# cantodad de veces que aparece menos los dias

def main():

    LEGAJOS= "legajo.csv"
    CAMPOS = ['Legajo','Apellido','Nombre','Total Vacaciones']
    CAMPOSLEGAJOS = ['Legajo','Fecha']
    while  True:
        print("Elija una opcion:\n 1.Cargar datos de Empleados \n 2.Consulta dias de VacacionesPendientes\n 3.Salir")
        opcion = input("")


        if opcion == "1":

            archivo = pedirNombre()
            cargardatos(archivo, CAMPOS)
            return archivo
            return
        if opcion == "2":

            archivo = input("ingrese nombre del archivo a recuperar")
            recuperarVacacionesPendientes(f"{archivo}.csv",LEGAJOS)
        if opcion == "3":
            exit()
        else:
            print("elija una opcion valida")
main()
