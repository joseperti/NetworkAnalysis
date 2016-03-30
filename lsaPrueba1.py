# -*- coding: utf-8 -*-
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
import math
import copy
import re
'''Parámetros de entrada
Conjunto: palabras admitidas = [ p1 , p2 , p3 ,...]
Documentos: conjunto de documentos y su puntuación = [[doc,puntuacion],...]
Frase a analizar = doc
'''

class vectorLSA():

    def __init__(self,i,j,valor):
        self.i = i
        self.j = j
        self.valor = valor

    def setValor(self,valor):
        self.valor = valor
        
    def geti(self):
        return self.i

    def getj(self):
        return self.j

    def modulo(self):
        return math.sqrt(self.i**2 + self.j**2)

    def producto(self,iIn,jIn):
        return (self.i*iIn + self.j*jIn)

    def distanciaCoseno(self,vector):
        i1 = vector.geti()
        j1 = vector.getj()
        print("Evaluando distancia coseno: ",self.producto(i1,j1)," / ",vector.modulo()," * ",self.modulo())
        return (self.producto(i1,j1) / (vector.modulo() * self.modulo()))
        
    def __repr__(self):
        return self.valor
    
def punto(x,y,symb):
    plt.plot(x,y,symb)

def texto(x,y,texto):
    plt.text(x,y,texto)

def flecha(dx,dy):
    plt.arrow(0,0,dx,dy)

def mostrarPlot():
    plt.ion()
    plt.xlim([-2,2])
    plt.ylim([-2,2])
    plt.show()
    
def traspuesta(matriz):
    matrizAux = [[0 for i in matriz] for i in matriz[0]]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matrizAux[j][i] = matriz[i][j]
    return matrizAux
    

def limpiador(frase):
    caracteres = [":",",","’s",'"',"'","´´","``","”"]
    for c in caracteres:
        frase = frase.replace(c,"")
    caracteresExtranos = [["\xc2\xa1",""],["\xc2\xa2",""],["\xc2\xa3",""],["\xc2\xa4",""],["\xc2\xa5",""],["\xc2\xa6",""],["\xc2\xa7",""],["\xc2\xa8",""],["\xc2\xa9",""],
    ["\xc2\xaa",""],["\xc2\xab",""],["\xc2\xac",""],["\xc2\xad",""],["\xc2\xae",""],["\xc2\xaf",""],["\xc2\xb0",""],["\xc2\xb1",""],["\xc2\xb2",""],
    ["\xc2\xb3",""],["\xc2\xb4",""],["\xc2\xb5",""],["\xc2\xb6",""],["\xc2\xb7",""],["\xc2\xb8",""],["\xc2\xb9",""],["\xc2\xba",""],["\xc2\xbb",""],
    ["\xc2\xbc",""],["\xc2\xbd",""],["\xc2\xbe",""],["\xc2\xbf",""],["\xc3\x80","A"],["\xc3\x81","A"],["\xc3\x82","A"],["\xc3\x83","A"],["\xc3\x84","A"],
    ["\xc3\x85","A"],["\xc3\x86","A"],["\xc3\x87","C"],["\xc3\x88","E"],["\xc3\x89","E"],["\xc3\x8a","E"],["\xc3\x8b","E"],["\xc3\x8c","I"],["\xc3\x8d","I"],
    ["\xc3\x8e","I"],["\xc3\x8f","I"],["\xc3\x90","D"],["\xc3\x91","N"],["\xc3\x92","O"],["\xc3\x93","O"],["\xc3\x94","O"],["\xc3\x95","O"],["\xc3\x96","O"],
    ["\xc3\x97","x"],["\xc3\x98","O"],["\xc3\x99","U"],["\xc3\x9a","U"],["\xc3\x9b","U"],["\xc3\x9c","U"],["\xc3\x9d","Y"],["\xc3\x9e",""],["\xc3\x9f",""],
    ["\xc3\xa0","a"],["\xc3\xa1","a"],["\xc3\xa2","a"],["\xc3\xa3","a"],["\xc3\xa4","a"],["\xc3\xa5","a"],["\xc3\xa6","a"],["\xc3\xa7","c"],["\xc3\xa8","e"],
    ["\xc3\xa9","e"],["\xc3\xaa","e"],["\xc3\xab","e"],["\xc3\xac","i"],["\xc3\xad","i"],["\xc3\xae","i"],["\xc3\xaf","i"],["\xc3\xb0","d"],["\xc3\xb1","n"],
    ["\xc3\xb2","o"],["\xc3\xb3","o"],["\xc3\xb4","o"],["\xc3\xb5","o"],["\xc3\xb6","o"],["\xc3\xb7",""],["\xc3\xb8",""],["\xc3\xb9","u"],["\xc3\xba","u"],
    ["\xc3\xbb","u"],["\xc3\xbc","u"],["\xc3\xbd","y"],["\xc3\xbe",""],["\xc3\xbf","y"]]
    for c in caracteres:
        frase = frase.replace(c,"")
    return frase.lower().split(" ")
    
def imprimirMatriz(matriz):
    for k in matriz:
        texto = ''
        for i in k:
            texto += str(i)+" "
        print(texto)
        
def imprimirSalto():
    print()

def clasificador(palabras,documentos):
    terminosOut = []
    documentosOut = []
##    print("Datos de entrada:")
##    print("Palabras admitidas")
##    print(palabras)
##    print("Documentos")
##    print(documentos)
    numeroDocs = len(documentos)
    print("Documentos: ",documentos)
    print("Palabras: ",palabras)
    matriz = [[i.count(j) for i in documentos] for j in palabras]
    print("Matriz de conteo:")
##    for k in range(len(matriz)):
##        matriz[k].append(palabras[k])
    imprimirMatriz(matriz)
    imprimirSalto()
    A = np.array(matriz)
    print(A)
    At = np.transpose(A)
    print(At)
    B = np.dot(At,A)
    print(B)
    C = np.dot(A,At)
    print(C)
    v , U = la.eig(C)
    v , S = la.eig(B)
    print("S:")
    print(S)
    print("U:")
    print(U)
    print("-----")
    sigma = np.sqrt(v)
    matrizAux = np.eye(2)
    for k in range(2):
        matrizAux[k][k] = sigma[k]
    sigmak2 = matrizAux
    #print(sigmak2)
    cont = 0
    for k in range(len(palabras)):
        Uk2Temp = U[k][0:2]
        #Chapuza
        Uk2Temp[1] = - Uk2Temp[1]
        #print(Uk2Temp)
        #print(sigmak2)
        #print("####")
        vector = np.dot(Uk2Temp,sigmak2)
        #print("vector: ",vector)
        flecha(vector[0],vector[1])
        punto(vector[0],vector[1],"o")
        texto(vector[0],vector[1]," - "+palabras[k])
        terminosOut.append(vectorLSA(vector[0],vector[1],palabras[k]))
    #print("Documentos:")
    #Documentos:
    for k in range(len(documentos)):
        Sk2Temp = S[k][0:2]
        #Chapuza
        Sk2Temp[0] = - Sk2Temp[0]
        #print(Sk2Temp)
        vector = np.dot(Sk2Temp,sigmak2)
        #print("vector: ",vector)
        flecha(vector[0],vector[1])
        punto(vector[0],vector[1],"x")
        texto(vector[0],vector[1]," - documento "+str(k+1))
        documentosOut.append(vectorLSA(vector[0],vector[1],str(k+1)))
    mostrarPlot()

    return terminosOut,documentosOut

def analisisCercania(terminos,documentos,puntuaciones):
    minimoSensibilidad = 0.5
##    print("Vectores de terminos: ")
##    print(terminos)
##    print("Vectores de documentos: ")
##    print(documentos)
    n = len(terminos)
    m = len(documentos)
    puntuacionesOut = [[],[]]
    for c in range(len(puntuaciones)):
        for k in range(n):
            listaAux = []
            sumaDistancias = 0
            for l in range(m):
                distancia = abs(documentos[l].distanciaCoseno(terminos[k]))
                #print("Termino: ",terminos[k]," documento: ",str(l+1)," distancia: ",distancia)
                if distancia > minimoSensibilidad:
                    listaAux.append([distancia,puntuaciones[c][l]])
                    sumaDistancias += distancia
            puntuacion = 0
            for d in listaAux:
                puntuacion += d[1]*(d[0]/sumaDistancias)
            puntuacionesOut[c].append(puntuacion)
    return puntuacionesOut

def limpiarTexto(texto):
    textoAux = copy.copy(texto)
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
    ["\n"," "],["\t"," "],["\b"," "],["*"," "],[" - "," "],["+"," "],
    ["("," "],[")"," "],["{"," "],["}"," "],["?"," "],["¿"," "],[";"," "],[":"," "]]
    for c in caracteresExtranos:
        textoAux = textoAux.replace(c[0],c[1])
    caracteres = [":",",",'.',"_","’s",'"',"'","´´","``","”"]
    for c in caracteres:
        textoAux = textoAux.replace(c," ")
    #eliminamos los espacioes en blanco sobrantes
    textoAux = textoAux.replace("  "," ")
    return textoAux
        
def leerTextoPositivo(nombre):
    file = open(nombre,'r')
    lineas = file.readlines()
    puntuacion = [[],[]]
    for k in range(len(lineas)):
##        print("Limpiando frase:", lineas[k])
        lineas[k] = limpiarTexto(lineas[k])
##        print("Resultado: ",lineas[k])
        puntuacion[0].append(0)
        puntuacion[1].append(1)
    return [lineas,puntuacion]
def leerTextoNegativo(nombre):
    file = open(nombre,'r')
    lineas = file.readlines()
    puntuacion = [[],[]]
    for k in range(len(lineas)):
##        print("Limpiando frase:", lineas[k])
        lineas[k] = limpiarTexto(lineas[k])
##        print("Resultado: ",lineas[k])
        puntuacion[0].append(0)
        puntuacion[1].append(1)
    
    return [lineas, puntuacion]
        
##frases = ['Romeo and Juliet',
##    'Juliet: O happy dagger',
##    'Romeo die by dagger',
##    '"Live free or die”, that is the New-Hampshire motto',
##    'Did you know, New-Hampshire is in New-England']

##frasesPuntuaciones = [[0,0,0,0,1],[0,0,1,0,0]]

##keywords = ['romeo', 'juliet','happy','dagger','live','die','free','new-hampshire']

vector = leerTextoPositivo("pruebaPositivo.txt")
frases = vector[0]
print(frases)
frasesPuntuaciones = vector[1] 
keywords = ['disfrutar','todas']

frasesLimpias = []

for k in frases:
    frasesLimpias.append(limpiador(k))



terminosVect , documentosVect = clasificador(keywords,frasesLimpias)

puntuacionesTerminos = analisisCercania(terminosVect,documentosVect,frasesPuntuaciones)

for k in range(len(keywords)):
    print("Término: ",str(keywords[k])," puntuacion positiva: ",str(puntuacionesTerminos[0][k])," puntuacion negativa: ",str(puntuacionesTerminos[1][k]))
