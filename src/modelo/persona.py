import datetime

class Persona:

   def __init__(self, nombre, edad):
       self.__nombre = nombre
       self.__edad = edad


   def asignar_edad(self, edad):
       #Prueba de comentario
       self.__edad = edad

   def asignar_nombre(self, nombre):
       # Prueba de comentario
       self.__nombre = nombre

   def dar_edad(self):
       # Prueba de comentario
       return(self.__edad)

   def dar_nombre(self):
       return(self.__nombre)

   def calcular_anio_nacimiento(self, ya_cumplio_anios):
       anio_actual = datetime.datetime.now().year
       if ya_cumplio_anios:
           return (anio_actual - self.__edad)
       else:
           return (anio_actual - self.__edad + 1)