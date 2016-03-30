# -*- coding: utf-8 -*-
import tweepy
import json
from pymongo import *
from persistencia import *
import datetime

#####Clase para streaming
class MyStreamListener(tweepy.StreamListener):

    def setPersistencia(self,pers,identificador):
        self.persistencia = pers
        self.identificador = identificador
        self.contador = 0
        
    def on_status(self, status):
        try:
            '''print(status.text,status.created_at,
                                            status.user.id_str,status.id_str,
                                            status.in_reply_to_status_id_str,
                                            status.created_at.year,status.created_at.month,
                                            status.created_at.day,status.created_at.hour,
                                            status.created_at.minute)'''
            self.contador += 1
            print("Tweet: ",self.contador)
            self.persistencia.insertarTweet(status.text,status.user.id_str,status.id_str,
                                            status.in_reply_to_status_id_str,
                                            status.created_at.year,status.created_at.month,
                                            status.created_at.day,status.created_at.hour,
                                            status.created_at.minute,self.identificador)
        except:
            print("Fallo en el tweet!!!!")

###Mover a un archivo de configuración externo###

consumerKey = "MrOBuLfa1aJ4Yz7EpT4K650AZ"
consumerSecret = "psSONPQbnkRf331GWORgEFASc1u8zZ3jYOKNq5cxzFm6l4mbr1"

accessToken = "253145620-W7P74YI0ATn81s9w9SSBz7VD3GEcT3OLgW7toPvo"
accessTokenSecret = "qryUeBgU43YJ2etFqEA1QcpReZgg5CvwXr9aiRsrprEEv"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.secure = True
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

clienteMongo = MongoClient()
moduloPersistencia = Persistencia()

def buscarId(usuarios):
    for k in usuarios:
        results = api.get_user(screen_name=k)
        print(results.id)

def buscarTweetsBBDD():
    for k in db.tweet.find():
        print(k)

def buscarScreenName(usuarios):
    for k in usuarios:
        results = api.get_user(id=k)
        print(results.screen_name)

def buscarSeguidos(idUser = None, scrName = None):
    if idUser == None:
        results = api.friends_ids(id=idUser)
    else:
        results = api.friends_ids(screen_name=scrName)
    print(results)

def buscarReplicasTweet():
    idTweet = "699542997243969536"
    
    text = ""
    for tweet in tweepy.Cursor(api.search,
                           q="%40Pablo_Iglesias_",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="es").items():
        if (idTweet == str(tweet.in_reply_to_status_id)):
            print(str(tweet.text))
    #results = api.get_status(idTweet)
    file = open("archivo.txt",'w')
    file.write(str(text))
    file.close()

def crearStreaming():
    titulo = "#SoyNoticia"
    filtro = "#SoyNoticia"
    myStreamListener = MyStreamListener()
    myStreamListener.setPersistencia(moduloPersistencia,titulo)
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=[filtro])
    
print("1.- Buscar por texto")
print("2.- Seguidos por usuario")
print("3.- Info Usuario")
print("4.- Buscar replicas a tweet")
print("5.- Crear Streaming")
print("0.- Salir")
dato = input("Seleccion: ")
while (dato !="0"):          
    #Obtener búsqueda
    if dato == "1":
        results = api.search(q=input("Buscar: "),)
        for l in results:
            if input("Siguiente |_:. ")!="":
                break
            else:
                print(guardarTweet(l.user.screen_name,l.text))
    #Obtener seguidos por usuario
    elif dato == "2":
        followers = []
        results = api.friends_ids(screen_name=input("Usuario: "))
        print(results)
    elif dato == "3":
        results = api.get_user(screen_name=input("Usuario: "))
        print(results)
    elif dato == "4":
        buscarReplicasTweet()
    elif dato == "5":
        crearStreaming()
    dato = input("Seleccion: ")
