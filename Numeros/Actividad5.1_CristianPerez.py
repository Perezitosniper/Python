def calculo(numero,resultado):
        numerost=str(numero)#numero=str(numero) numero=int(numero)        
        lon=len(numerost)        
        if lon==5 and numero==10000:
            resultado=diccionariounidades[10]+" "+diccionariomiles[1]
        elif lon==4:
            miraMiles(numerost, resultado)
        elif lon==3:
            miraCientos(numerost, resultado)
        elif lon==2:
            miraResto(numerost, resultado)
        else:
            resultado=resultado+" "+diccionariounidades[int(numerost)]
            print(resultado)

def miraMiles(numerost, resultado):
        miles=numerost[0:1]
        if int(miles)!=1:
            resultado=diccionariounidades[int(miles)]+" "+diccionariomiles[1]
        else:
            resultado=diccionariomiles[int(miles)]
        numero=int(numerost[1:4])
        calculo(numero,resultado)

def miraCientos(numerost, resultado):
        centenas=numerost[0:1]
        decenas=numerost[1:2]
        unidades=numerost[2:3]
        if int(centenas)==1 and int(decenas)==0 and int(unidades)==0:
            resultado=resultado+" cien"
        elif int(centenas)>1 and int(decenas)==0 and int(unidades)==0:
            resultado=resultado+" "+diccionariocentenas[int(centenas)]
            print(resultado)
        else:
            resultado=resultado+" "+diccionariocentenas[int(centenas)]
            numero=numerost[1:3]
            calculo(numero,resultado)

def miraResto( numerost,resultado):
        decenas=numerost[0:1]
        unidades=numerost[1:2]
        if int(numerost)<21:
            resultado=resultado+" "+diccionariounidades[int(numerost)]
            print(resultado)
        elif int(numerost)<30:
            resultado=resultado+" "+diccionariodecenas[int(decenas)]+diccionariounidades[int(unidades)]
            print(resultado)
        elif int(unidades)!=0:
            resultado=resultado+" "+diccionariodecenas[int(decenas)]+" y "+diccionariounidades[int(unidades)]
            print(resultado)
        else:
            resultado=resultado+" "+diccionariodecenas[int(decenas)]
            print(resultado)

diccionariounidades={0:"cero", 1:"uno", 2:"dos", 3:"tres", 4:"cuatro",5:"cinco", 6:"seis", 7:"siete", 8:"ocho", 9:"nueve",10:"diez", 11:"once", 12:"doce", 13:"trece", 14:"catorce",15:"quince", 16:"dieciseis", 17:"diecisiete", 18:"dieciocho", 19:"diecinueve", 20:"veinte"}
diccionariodecenas={2:"veinti",3:"treinta",4:"cuarenta",5:"cincuenta",6:"sesenta",7:"setenta",8:"ochenta",9:"noventa"}
diccionariocentenas={1:"ciento",2:"doscientos",3:"trescientos",4:"cuatrocientos",5:"quinientos",6:"seiscientos",7:"setecientos",8:"ochocientos",9:"novecientos"}
diccionariomiles={1:"mil"}
numero=-1
resultado=""
while numero<0 or numero>10000:
    numero=int(input("Ingresa numero"))

if numero==0:
    print("Cero")
else:
    calculo(numero,resultado)
