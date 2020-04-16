'''
Created on 15 abr. 2020

@author: Jesus
'''
import re

expresion_tipo = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9 ]{3,20}$"
expresion_nombre = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9 ]{2,40}$"
expresion_plataforma = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9 ]{2,20}$"
expresion_anio = "^[0-9]{4}$"
expresion_precio = "^[0-9,.]{1,5}$"

def validar_tipo(tipo):
    validador = re.compile(expresion_tipo)
    return validador.match(tipo)

def validar_nombre(nombre):
    validador= re.compile(expresion_nombre)
    return validador.match(nombre)

def validar_plataforma(plataforma):
    validador= re.compile(expresion_plataforma)
    return validador.match(plataforma)

def validar_anio(anio):
    validador= re.compile(expresion_anio)
    return validador.match(anio)

def validar_precio(precio):
    validador= re.compile(expresion_precio)
    return validador.match(precio)




