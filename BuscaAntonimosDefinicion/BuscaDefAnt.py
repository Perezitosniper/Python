import mechanicalsoup
# para buscar dentro de string
import re


def obtenerAntonimo(palabra):
    url_diccionario = "http://www.antonimos.net/?termino={0}".format(palabra)
    browser = mechanicalsoup.StatefulBrowser()  # preparo el navegador
    pagina = browser.open(url_diccionario)  # descargo la web
    return pagina  # devuelvo un objeto BeautifulSoup


def obtenerDef(palabra):
    url_def = "https://www.wordreference.com/definicion/{0}".format(palabra)
    browser = mechanicalsoup.StatefulBrowser()  # preparo el navegador
    paginade = browser.open(url_def)  # descargo la web
    return paginade  # devuelvo un objeto BeautifulSoup


def buscaAntonimos(palabra):  # hay que buscar todos los tr  y en el primer ed es el antonimo

    palabra = palabra.lower()
    # obtengo la pagina
    pagina = obtenerAntonimo(palabra)
    # ahora navego por las etiquedas buscado
    # en este caso todos los <table>
    tags = pagina.soup.find_all('table')
    # si encuentra alguna
    print(len(tags))
    if tags is not None and len(tags) > 2:
        # del primer div que encuentra busco dentro todos los elementos <td> para coger el texto de dentro de la etiqueta
        los = []
        lis = tags[2].find_all('tr')
        for x in lis:
            los.append(x.find('a').get_text())
            # print(los)

        # fallo al rellenar y recorrer la lista
        finalstring = ""
        for tod in los:
            finalstring += tod + ", "

        finalstring = finalstring[:len(finalstring) - 2]
        # cad = "" # para el primer <td> busco si contiene la cadena la cadena que contiene# for contenido in los:# if not re.match(contenido.text):# si lo encuentro me lo quedo#cad += " " + (contenido.text.replace(",", " "))# puede darse el caso que se repita alguna asi# que por seguridad# quitar repetidas#final = []# divido la cadena en palabras y las repaso todas # for x in cad.split(): # if x not in final and x != palabra: # añado cualquier palabra que no sea la que estoy buscando y# que no este añadida ya# final.append(x) # devuelto la lista convertida en string
        #print(finalstring)
        return str(finalstring)
    else:
        # si no encuentro nada
        return "No se encuentran Antonimos"


def buscadefinicion(palabra):
    palabra = palabra.lower()
    paginaf = obtenerDef(palabra)
    tags = paginaf.soup.find_all('ol', {'class': 'entry'})  # hasta aqui bien
    # print(len(tags))
    # si encuentra alguna
    if tags is not None and len(tags) > 0:
        los = []
        una=""
        Conjunto = ""
        for x in tags:
            lis = x.find_all('li')
            #print(lis)
            for li in lis:
                los.append(li.text)
                #print(li.get_text())
                una = li.get_text()
                #print(una)
                Conjunto += "\n\t" + una

            #return(Conjunto)
        if len(Conjunto) != 0:
            return Conjunto
        else:
            return "No se encuentra definicion."


def antonimo(pablabraDefyAnto):

    pablabraDefyAnto = pablabraDefyAnto.lower()
    antonimoEncontrado = buscaAntonimos(pablabraDefyAnto)
    definicion = buscadefinicion(pablabraDefyAnto)

    print("Antonimo de esta palabra: \n\t" + antonimoEncontrado + "\nDefinicion de la palabra " + str(pablabraDefyAnto) + ":\n\t" + str(definicion))


pablabraDefyAnto = input(
    "Introduce palabra a buscar definicion y antonimo: \n")
antonimo(pablabraDefyAnto)
