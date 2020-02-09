from sys import exit #seimporto el módulo de salida de sys, para poder escribir el nombre del archivo desde el teclado
#importamos la funcion shutil para realizar operaciones con archivos y/o directorios como copiar, mover entre otras.
import shutil,os

class Archivo: #creamos nuestra clase
    def __init__(self, nombre): #inicializamos los atributos del objeto que creamos
        try: #abrimos un try para una excepcion
            # abrimos un archivo pero con los argumentos nombre para obtener el nombre del archivo desde el teclado y la
            #'r' es para leer el archivo
            self.f = open(nombre, 'r')
            self.nombre = nombre
        except: #se crea una excepcion para en caso de no poder abrir el archivo y con el exit() se termina el programa
            print("No se puede abrir el archivo", nombre)
            exit()

    def muestra(self): # creamos nuestro metodo muestra para imprimir lo que contiene el archivo
        i = 1 #inicializamos i en 1
        #utilizamos el for para recorrer y contar cuantas lineas tiene el archivo y se utiliza como  self.f para el fin
        #del archivp y mostrar su contenido
        for linea in self.f:
            # imprimimos cada linea del texto y tambien imprimimos i que indica el numero de lineas
            print("{:3} {}".format(i, linea))
            i += 1 #se incremente i
        # establece la posición actual del archivo en el desplazamiento.donde su valor predeterminado es 0,
        # lo que significa el posicionamiento absoluto del archivo.
        self.f.seek(0)

    def cuentaVocales(self): #creamos nuestro metodo para contar las vocales que contiene el archivo
        s = self.f.read() #Leemos nuestro archivo y lo colocamos en la variable s
        contador = 0 #inicializamos nuestro contador en 0
        #se crea el for para recorrer la cadena s que es donde se guardo lo que contiene el archivo
        for i in range(len(s)):
            # comparamos cada caracter del archivo con el conjunto para saber cuantas vocales hay en el archivo
            if s[i] in set("aeiouáéíóú"):
                contador += 1 #en caso de que si se aumenta el contador
        self.f.seek(0)
        print("La cantidad de vocales son:", contador)#imprimimos el resultado de cuantas vocales se encuentran en el archivo

    def cuentaConsonantes(self):#creamos nuestro metodo para contar las consonantes que contiene el archivo
        cadena2 = self.f.read() #Leemos nuestro archivo y lo guardamos en la variable cadena2
        contador1 = 0 #inicializamos nuestro contador1
        # se crea el for para recorrer la cadena2 que es donde se guardo lo que contiene el archivo
        for i in range(len(cadena2)):
            # comparamos cada caracter del archivo con el conjunto para saber cuantas consonantes hay en el archivo
            # utiliaamos lower para convertir la cadena en minusculas
            if cadena2[i].lower() in set("b,c,d,f,g,h,j,k,l,m,n,ñ,p,q,r,s,t,v,x,y,z"):
                contador1 += 1#incrementamos nuestro contador1
        self.f.seek(0)
        print("La cantidad de consonantes son:", contador1)#imprimimos el resultado de cuantas vocales se encuentran en el archivo

    def cuentaPalabras(self):
        cadena = self.f.read()#Leemos nuestro archivo y lo guardamos en la variable cadena
        # utilizamos la funcion split para que divida una cadena en una lista donde cada palabra es un elemento de
        #la lista, y se guarda en la variable np
        np = cadena.split()
        npalabras = len(np)#utilizamos len para obtener la longitud de la lista o cadena.
        self.f.seek(0)
        print("Cantidad de palabras son:", npalabras)#imprimimos el resultado de cuantas vocales se encuentran en el archivo

    def cuentaSPuntuacion(self):
        s = self.f.read()#Leemos nuestro archivo y lo guardamos en la variable s
        contador2 = 0 #inicializamos nuestro contador en 0
        # se crea el for para recorrer la cadena s que es donde se guardo lo que contiene el archivo
        for i in range(len(s)):
            # comparamos cada caracter con el conjunto para saber cuantos signos de puntuacion hay en el archivo
            if s[i] in set(":,;,,,.,¿,?,...,¡,!,(,),[,],"",-,/,*,¨"):
                # si hay un signo de puntuacion aumentamos nuestro contador2 en caso de que no solo se aumenta i en el for
                contador2 += 1
        self.f.seek(0)
        # imprimimos el resultado de cuantos signos de puntuacion se encuentran en el archivo
        print("La cantidad de signos de puntuacion son:", contador2)

    def cuentaEspacio(self):
        s = self.f.read()#Leemos nuestro archivo y lo guardamos en la variable s
        contador3 = 0
        # se crea el for para recorrer la cadena s que es donde se guardo lo que contiene el archivo
        for i in range(len(s)):
            # comparamos cada caracter con el conjunto para saber cuantos espacios hay en el archivo
            if s[i].lower() in set(" "):
                # si hay un espacio aumentamos nuestro contador3 en caso de que no solo se aumenta i en el for
                contador3 += 1
                self.f.seek(0)
                # imprimimos el resultado de cuantos espacios se encuentran en el archivo
        print("La cantidad de espacios son:", contador3)

    def cuentaMayusculas(self):
        s = self.f.read()#Leemos nuestro archivo y lo guardamos en la variable s
        conta = 0
        # se crea el for para recorrer la cadena s que es donde se guardo lo que contiene el archivo
        for i in range(len(s)):
            # comparamos automaticamente cada caracter del arhcivo para saber si es mayuscula con la funcion isupper()
            if s[i].isupper():
                # si hay una letra en mayuscula aumentamos nuestro conta en caso de que no solo se aumenta i en el for
                conta += 1
                self.f.seek(0)

        print("La cantidad de mayusculas son:", conta)

    def cuentaMinusculas(self):
        s = self.f.read()#Leemos nuestro archivo y lo guardamos en la variable s
        contador3 = 0
        # se crea el for para recorrer la cadena s que es donde se guardo lo que contiene el archivo
        for i in range(len(s)):
            # comparamos automaticamente cada caracter del archivo para si es minuscula con la funcion islowe()
            if s[i].islower():
                # si hay letra en minuscula aumentamos nuestro contador3 en caso de que no solo se aumenta i en el for
                contador3 += 1
                self.f.seek(0)
        print("La cantidad de minusculas son:", contador3)

    def Mayusculas(self):
        s = self.f.read()#Leemos nuestro archivo y lo guardamos en la variable s
        print("Texto convertido a mayusculas\n")#solo se imprime el texto dentro de las comillas con un salto de linea\n
        print(s.upper()) #convertimos el texto del archivo a mayusculas con la funcions upper() y lo imprmimos
        self.f.seek(0)

    def Minusculas(self):
        s = self.f.read()#Leemos nuestro archivo y lo guardamos en la variable s
        print("Texto convertido a minusculas\n")#solo se imprime el texto dentro de las comillas con un salto de linea\n
        print(s.lower())#convertimos el texto del archivo a minusculas conla funcion lower() y lo imprimimos
        self.f.seek(0)

    def Hexadecimal(self):
        s = self.f.read()#Leemos nuestro archivo y lo guardamos en la variable s
        print("Texto convertido a hexadecimal\n")#solo se imprime el texto dentro de las comillas con un salto de linea\n
        for i in range(len(s)):
            #primero convertimos nuesta cada caracter del archivo a un numero entero con la funcion ord()
            # y posteriormente lo convertimos a hexadecimal
            print(hex(ord(s[i])))

    def Copiar(self):
        #definimos os como objeto de shutil para poder mandar a llamar las funciones getcdw() para
        #devolver el directorio de trabajo actual de un proceso y la funcion sep solo indica el separador entre
        #partes de la ruta y se guarda en la variable ruta
        ruta = os.getcwd() + os.sep
        #creamos nuestra variable origen con la ruta especificada anteriormente con el simbolo  + y
        #el nombre del archivo a copiar
        origen = ruta + 'Prueba.txt'
        #creamos nuestra variable destino con la ruta especificada en la variable con el simbolo + el nuevo
        #nombre de archivo, esto es para copiarlo en el mismo destinatario
        destino = ruta + 'Texto.txt'
        # utilizamos path.exists para ver si la ruta se refiere a una ruta existente en caso de ser cierto y en caso
        # contrario devuelve False para enlaces simbólicos rotos.
        if os.path.exists(origen):
            # abrimos el direcotorio del archivo origen, donde
            # rb abre un archivo para leer solo en formato binario.
            with open(origen, 'rb') as forigen:
                # abrimos el direcotorio del archivo destino, donde
                # wb abre un archivo para escribir solo en formato binario.
                with open(destino, 'wb') as fdestino:
                    #con la funcion shutil.copyfile copeamos el archivo de acuerdo con los parametros de origen del archivo
                    # a copiar y el destino hacia donde sera copeado
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")

    def cuentaLineas(self):
        self.f.seek(0)
        # utilizamos len para obtener la longitud de lineas del archivo donde ocupamos la funcion readlines()
        # para contar el numero de lineas
        print("\nLa cantidad de lineas son :", len(self.f.readlines()))

nomb = input("Nombre del Archivo: ")#leemos desde teclado el nombre del archivo y se guarda en nomb
archivo = Archivo(nomb)#creamos nuestro objeto archivo de la clase con el argumento nomb que guarda el nombre del archivo
archivo.muestra()#utilizamos el obejeto archivo para llamar a nuestro metodo
archivo.cuentaVocales()
archivo.cuentaConsonantes()
archivo.cuentaPalabras()
archivo.cuentaSPuntuacion()
archivo.cuentaEspacio()
archivo.cuentaMayusculas()
archivo.cuentaMinusculas()
archivo.Mayusculas()
archivo.Minusculas()
archivo.Hexadecimal()
archivo.Copiar()
archivo.cuentaLineas()
