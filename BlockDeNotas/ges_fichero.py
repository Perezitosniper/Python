import sys
from clase_nota import nota


def lectura(lista, totalNotas):
    try:
        archivo = open("archivo.txt")
        for linea2 in archivo.readlines():
            # procesar línea
            lista.append(linea2[:len(linea2) - 1])

        for x in lista:

            partes = x.split("&")
            notacreada = nota(partes[0], partes[1], partes[2])
            totalNotas.append(notacreada)
            print(str(notacreada))

    except FileNotFoundError:
        print("Error, fichero no encontrado")


def escritura(totalNotas):
    archivo = open("archivo.txt", "w")
    for line in totalNotas:
        datosArr = str(line)
        archivo.write(datosArr + "\n")
    archivo.close()


def todo(totalNotas):
    for i in totalNotas:
        frases = str(i)
        frases = frases.split("&")
        frasesunida = " ".join(frases)
        print(frasesunida)


def tareashechas(totalNotas):
    for i in totalNotas:
        frases = str(i)
        frases = frases.split("&")
        if str(frases[1]) == "Realizada":
            frasesunida = " ".join(frases)
            print(frasesunida)


def tareasSinHacer(totalNotas):
    for i in totalNotas:
        frases = str(i)
        frases = frases.split("&")
        if str(frases[1]) == "No realizada":
            frasesunida = " ".join(frases)
            print(frasesunida)


def crear(totalNotas):
    notatext = input("Introduzca nota: ")
    estado = -1
    realono = "Realizada"
    while estado < 0 or estado > 1:
        try:
            estado = input("\nIntroduzca 0 para no realizada y 1 para realizada")
            estado = int(estado)

            if estado == 0:
                realono = "No realizada"
            else:
                realono = "Realizada"
            id = 0
        except ValueError:
            print("\nError de Introduccion de datos")
            estado = -1
    # print(len(totalNotas))
    if len(totalNotas) > 0:
        ultimo = str(totalNotas[(len(totalNotas) - 1)])
        ultimo = ultimo.split("&")
        id = (int(ultimo[0]) + 1)
    else:
        id = 1
    todo = str(id) + "&" + realono + "&" + notatext
    print("\n+-+-+-+ Nota introducida con exito +-+-+-+")

    totalNotas.append(nota(id, realono, notatext))

# por aqui


def cambia(totalNotas):
    idAcambiar = int(input("\nIntroduce id a cambiar estado"))
    for i in totalNotas:
        frases = str(i)
        frases = frases.split("&")
        if int(frases[0]) == idAcambiar:
            pos = totalNotas.index(i)

            if frases[1] == "No realizada":
                frases[1] = "Realizada"
            else:
                frases[1] = "No realizada"
                # va bien
            i = str(frases[0]) + "&" + \
                str(frases[1]) + "&" + frases[2]
            print("+-+-+-+Cambiado con exito el estado de la nota+-+-+-+")
            totalNotas[pos] = nota(frases[0], frases[1], frases[2])


def borrar(totalNotas):
    id = input("introduce id a borrar")
    for i in totalNotas:
        frases = str(i)
        frases = frases.split("&")
        if int(frases[0]) == int(id):
            totalNotas.remove(i)


def fin(totalNotas):
    escritura(totalNotas)
    sys.exit(0)
