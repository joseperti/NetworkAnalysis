import copy
import json
import re

def eliminacionStopWords():
    None

def frecuenciaPalabras(nombre):
    file = open(nombre,'r')
    texto = file.read()
    textoAux = copy.copy(texto)
    conjuntoPalabras = set([])
    #Quitamos acentos y caracteres extraños
    
    caracteresExtranos = [["\\xc2\\xa1",""],["\\xc2\\xa2",""],["\\xc2\\xa3",""],["\\xc2\\xa4",""],["\\xc2\\xa5",""],["\\xc2\\xa6",""],["\\xc2\\xa7",""],["\\xc2\\xa8",""],["\\xc2\\xa9",""],
    ["\\xc2\\xaa",""],["\\xc2\\xab",""],["\\xc2\\xac",""],["\\xc2\\xad",""],["\\xc2\\xae",""],["\\xc2\\xaf",""],["\\xc2\\xb0",""],["\\xc2\\xb1",""],["\\xc2\\xb2",""],
    ["\\xc2\\xb3",""],["\\xc2\\xb4",""],["\\xc2\\xb5",""],["\\xc2\\xb6",""],["\\xc2\\xb7",""],["\\xc2\\xb8",""],["\\xc2\\xb9",""],["\\xc2\\xba",""],["\\xc2\\xbb",""],
    ["\\xc2\\xbc",""],["\\xc2\\xbd",""],["\\xc2\\xbe",""],["\\xc2\\xbf",""],["\\xc3\\x80","A"],["\\xc3\\x81","A"],["\\xc3\\x82","A"],["\\xc3\\x83","A"],["\\xc3\\x84","A"],
    ["\\xc3\\x85","A"],["\\xc3\\x86","A"],["\\xc3\\x87","C"],["\\xc3\\x88","E"],["\\xc3\\x89","E"],["\\xc3\\x8a","E"],["\\xc3\\x8b","E"],["\\xc3\\x8c","I"],["\\xc3\\x8d","I"],
    ["\\xc3\\x8e","I"],["\\xc3\\x8f","I"],["\\xc3\\x90","D"],["\\xc3\\x91","N"],["\\xc3\\x92","O"],["\\xc3\\x93","O"],["\\xc3\\x94","O"],["\\xc3\\x95","O"],["\\xc3\\x96","O"],
    ["\\xc3\\x97","x"],["\\xc3\\x98","O"],["\\xc3\\x99","U"],["\\xc3\\x9a","U"],["\\xc3\\x9b","U"],["\\xc3\\x9c","U"],["\\xc3\\x9d","Y"],["\\xc3\\x9e",""],["\\xc3\\x9f",""],
    ["\\xc3\\xa0","a"],["\\xc3\\xa1","a"],["\\xc3\\xa2","a"],["\\xc3\\xa3","a"],["\\xc3\\xa4","a"],["\\xc3\\xa5","a"],["\\xc3\\xa6","a"],["\\xc3\\xa7","c"],["\\xc3\\xa8","e"],
    ["\\xc3\\xa9","e"],["\\xc3\\xaa","e"],["\\xc3\\xab","e"],["\\xc3\\xac","i"],["\\xc3\\xad","i"],["\\xc3\\xae","i"],["\\xc3\\xaf","i"],["\\xc3\\xb0","d"],["\\xc3\\xb1","n"],
    ["\\xc3\\xb2","o"],["\\xc3\\xb3","o"],["\\xc3\\xb4","o"],["\\xc3\\xb5","o"],["\\xc3\\xb6","o"],["\\xc3\\xb7",""],["\\xc3\\xb8",""],["\\xc3\\xb9","u"],["\\xc3\\xba","u"],
    ["\\xc3\\xbb","u"],["\\xc3\\xbc","u"],["\\xc3\\xbd","y"],["\\xc3\\xbe",""],["\\xc3\\xbf","y"],
    ["\n"," "],["\t"," "],["\b"," "],["*"," "],["-"," "],["+"," "],
    ["("," "],[")"," "],["{"," "],["}"," "],["?"," "],["¿"," "],[";"," "],[":"," "]]
    for c in caracteresExtranos:
        textoAux = textoAux.replace(c[0],c[1])
    caracteres = [":",",",'.',"_","’s",'"',"'","´´","``","”"]
    for c in caracteres:
        textoAux = textoAux.replace(c," ")
    #eliminamos los espacioes en blanco sobrantes
    m = re.search("(\s+)",textoAux)
    for k in m.groups():
        textoAux = textoAux.replace(k," ")
    #eliminamos los caracteres repetidos mas de dos veces
    
    #print(textoAux)
    #Pasamos todo a lower
    textoAux = textoAux.lower()
    #Procedemos
    palabras = textoAux.split(' ')
    for k in palabras:
        conjuntoPalabras.add(k)
    #print(conjuntoPalabras)
    #print(len(conjuntoPalabras))
    frecuencia = dict()
    for k in conjuntoPalabras:
        frecuencia[k] = palabras.count(k)
    #print(frecuencia)
    return sorted(frecuencia.items(), key=lambda x: x[1],reverse = True)

def unirDiferenciacion(anterior,nuevo):
    datos = {}
    for key,value in anterior.items():
        datos[key] = value
    for key,value in nuevo.items():
        try:
            datos[key] += value
        except:
            datos[key] = value

def importarDatos():
    archivoFrecuencias = "frecuencias.json"
    archivoDiferenciador = "diferenciado.json"
    datosF = None
    datosDif = None
    file = open(archivoFrecuencias,"r")
    datosF = file.read()
    datosF = json.loads(datosF)
    file = open(archivoDiferenciador,"r")
    datosDif = file.read()
    datosDif = json.loads(datosDif)
    return datosF,datosDif

def diferenciadorPalabras(conjunto):
    diccs = dict()
    lista = conjunto
    texto = ""
    for k in range(len(lista)):
        texto += str(k)+".- "+lista[k]+"\n"
    for k in lista:
        diccs[k] = []
        
    destino = ""
    for k in conjunto:
        print(k)
        selecc = input(texto+"_")
        selecc = int(selecc)
        diccs[lista[selecc]].append(k)
        print("Añadido a: ",lista[selecc])

    return diccs
        

datos = frecuenciaPalabras(input("Inserta nombre de archivo:\n"))
print(datos)

'''datos = diferenciadorPalabras(["Hola","Adios","gato","es","bonito"])'''


