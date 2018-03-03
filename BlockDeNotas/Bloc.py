import ges_fichero
# Menu Principal


def primermenu():
    print("\n\n\t-----Menu-----")
    print("\t1)Listar notas")
    print("\t2)Crear notas")
    print("\t3)Cambiar estado notas")
    print("\t4)Borrar notas")
    print("\t5)Salir")
    print("\t---------------\n\n")
# menu secundario que sae cuando le damos a listar notas


def menuSecundario():
    print("\n\n\t-----Menu-----")
    print("\t|1)Todas")
    print("\t|2)Realizadas")
    print("\t|3)Por hacer")
    print("\t---------------\n\n")


num = -1
num2 = -1
nota = []
totalNotas = []
ges_fichero.lectura(nota, totalNotas)

while True:
    while(num < 1 or num > 5):
        primermenu()
        try:
            num = int(input("Introduzca opcion: "))
            if num<1 or num>5:
                    print("------opcion no valida------")
        except ValueError:
            print("Introduzca numero, no letras")
            num = -2
    if num == 1:
        while num2 < 1 or num2 > 3:
            menuSecundario()
            try:
                num2 = int(input("Introduce opcion: "))
                if num2<1 or num2>3:
                    print("------opcion no valida------")
            except ValueError:
                print("Introduzca numero, no letras")
                num2 = -2

        if num2 == 1:
            ges_fichero.todo(totalNotas)
            num = -1
            num2 = -1
        elif num2 == 2:
            ges_fichero.tareashechas(totalNotas)
            num = -1
            num2 = -1
        else:
            ges_fichero.tareasSinHacer(totalNotas)
            num = -1
            num2 = -1

    elif num == 2:
        ges_fichero.crear(totalNotas)
        num = -1

    elif num == 3:
        ges_fichero.cambia(totalNotas)
        num = -1
    elif num == 4:
        ges_fichero.borrar(totalNotas)
        num = -1
    elif num == 5:
        ges_fichero.fin(totalNotas)
