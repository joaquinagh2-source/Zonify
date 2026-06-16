from flask import Flask, render_template, redirect, url_for #El flask es lo que deja crear el servidor web, el render template es lo que comina los archivos html y combinarlos con los datos que recibe python para mostrarlos bien al usuario y el redirect y el urlfor sirven para que si pasa un evento, lo mande rapido a la pagina.
from services.cosevi_service import obtener_eventos_cosevi #esta linea hace que del codigo de cosevi service, generado junto al api publico de cosevi y ayuda de ia, jale la definicion que se usa para otener los datos de la api 

app = Flask(__name__) #basicamente esta linea sirve para que el servidor web exista
eventos_cache = [] #Es una lista vacia en la RAM que es para guardar datos temporalmente y hacer la web mas rapida

