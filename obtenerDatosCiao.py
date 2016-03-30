#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, re, urllib.request

ventajas = ""
desventajas = ""
try:
    for i in range(15,1000,15):
        num = str(i)
        sock = urllib.request.urlopen("http://www.ciao.es/Opiniones/Positivas__320425/Start/"+num)
        htmlSource = sock.read()
        ##Ventajas
        pat = re.compile('<span>Ventajas</span><strong>[^<]*</strong>')
        li = pat.findall(str(htmlSource))
        pat = re.compile('<strong>(?P<descr>[^<]*)</strong>')
        for k in li:
            opiniones = pat.search(k).group('descr')
            ventajas += "\n"+opiniones
            print(opiniones)

        ##Desventajas
        
        pat = re.compile('<span>Desventajas</span><strong>[^<]*</strong>')
        li = pat.findall(str(htmlSource))
        pat = re.compile('<strong>(?P<descr>[^<]*)</strong>')
        for k in li:
            opiniones = pat.search(k).group('descr')
            desventajas += "\n"+opiniones
            print(opiniones)
finally:
    print("Finalizada la descarga de opiniones")
print("|||||||||||||Ventajas:||||||||||||||")
print(ventajas)
archivo = open("positivo.txt",'w')
archivo.write(ventajas)
archivo.close()

print("|||||||||||||Desventajas:|||||||||||")
print(desventajas)
archivo = open("negativo.txt",'w')
archivo.write(desventajas)
archivo.close()
