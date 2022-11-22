# 1) Construya la clase Usuario y solicita la información básica de los usuario de una Biblioteca

# 2) Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar (ciudad y país) y fecha de edición (usa la clase Fecha). La clase debe proporcionar los siguientes servicios: accedentes y mutadores, (get y set) método para leer la información y método para mostrar la información. Este último método mostrará la información del libro con este formato:

# Título: Introduction to Java Programming
# 3a. edición
# Autor: Liang, Y. Daniel
# ISBN: 0-13-031997-X
# Prentice-Hall, New Jersey (USA), viernes 16 de noviembre de 2001
# 784 páginas

# 3) Aprovechando lo anterior construya una clase que me permita prestar un libro

import random; import platform; import os; import time; import datetime; from reportlab.pdfgen import canvas;
from reportlab.lib.pagesizes import letter; import qrcode  

Usuarios =[]
Libros = ["Python Fácil","Aprende Arduino y Python","Inteligencia Artificial con Python","Código facilito","Domótica"]; ISBN = ["N2480","JKLM121","1890ZJ","JAK12","2022JE"]; Paginas = [440,220,150,500,250]; Edicion = ["1a. edición","2a. edición", "3a. edición", "4a. edición", "5a. edición"];  Editorial = ["SOU-HALL","Premitier-sodomotik","Shesk-jack","Peptoyer-cloud","Piptime-condomer"]
Guardado = []

print("\tBiblioteca virtual MundoChimba\n")
print("Necesitarás crear una cuenta antes\n1.Si\n2.no")
s = input("Deseas comenzar? ")

# Limpiar terminal 
class Limpiar():

    def Limpiando(self):
        time.sleep(0.10)
        if platform.system() == 'Windows':
            time.sleep(0.40)
            os.system('cls')
        else:
            os.system('clear')
# 1 Creación de la clase Usuario
class Usuario (Limpiar):

    def __init__(self):
        self.contador = 3
        self.Nombre = " "
        self.CC = 0
        self.Password = 0
        self.Telefono = 0 
    
    def Solicitar_Datos(self):
        print("Ingresa Datos básicos: ")
        self.Nombre = input("Digita tu nombre: ")
        self.CC = int(input("Digita tú número de identificación: "))
        self.Telefono = int(input("Digita tú número de celular: "))
        self.Password = int(input("Digita una nueva clave: "))
        # Usuarios.append(self.CC)
        # Usuarios.append(self.Password)
        New_Usu = (self.CC, self.Password)
        Usuarios.append(New_Usu)
        print("Registro exitoso!!")
        super().Limpiando()
        self.Ingreso()
    
    def Ingreso(self):
        print("\tBiblioteca virtual MundoChimba\n")
        print("Iniciar sesión\n")
        self.CC = int(input("Digita tu cédula: "))
        self.Password = int(input("Digita la clave: "))

        if self.CC in Usuarios and self.Password in Usuarios:
                self.Limpiando()
                print("\tBiblioteca virtual MundoChimba te da la Bienvenido",self.Nombre,"\n")

        elif self.CC != Usuarios or self.Password != Usuarios:
            self.contador -=1 
            print("Error, vuelva a intentarlo!!")
            if self.contador == 0:
                print("Lo siento, se ha bloqueado el ingreso por unos segundos!!")
                self.Limpiando()
                self.Ingreso()
            self.Limpiando()
            self.Ingreso()

class Autor():

    def __init__(self):
        self.Nombre_Autor = " "

    def GetAutor(self):
        return self.Nombre_Autor
    def SetAutor(self, autor):  ###### Nombre 
        self.Nombre_Autor = autor

class Lugar():

    def __init__(self) -> None:
        self.Lugar = " "
    
    def GetLugar(self):
        return self.Lugar
    def SetLugar(self,lugar):  ###### Lugar 
        self.Lugar = lugar

class Fecha():

    def __init__(self):
        self.FechaEdi = " "
    
    def GetFecha(self):
        return self.FechaEdi
    def SetFecha(self, fecha):    ##### Fecha de edición 
        self.FechaEdi = fecha
# 3 Pedir un libro prestado
class Prestar(Limpiar, Autor, Lugar, Fecha):

    def __init__(self):
        self.contador = 1
        self.Prestar = " "
        self.lib = " "
        self.pre = 0
    
    def Pedir_prestado(self):
        #print("Nota: Estos libros tienen duración visible por 30 días\nLibros que está disponibles hasta ahora: \n")
        # for Lib in Libros:
        #     print(f"{self.contador} {Lib}")
        #     self.contador += 1 
        # self.pre = int(input("¿Digita la cantidad de libro que deseas tener por 30 días? "))
        # self.contador = 1
        print("Estás son las siguientes opcione: \n1.Ver libros disponibles\n2.Pedir prestado\n3.Salir\n")
        I = int(input("Ingrese la opción deseada: "))

        if I == 1:
            print("Nota: Estos libros tienen duración visible por 30 días\nLibros que está disponibles hasta ahora: \n")
            for Lib in Libros:
                print(f"{self.contador} {Lib}")
                self.contador += 1
            time.sleep(4)
            self.Limpiando()
            self.Pedir_prestado()

        elif I == 2:
            self.pre = int(input("¿Digita la cantidad de libro que deseas tener por 30 días? "))
            self.contador = 1
        
        elif I == 3:
            exit()

    def Prestando(self):
        super().Limpiando()
        for x in Libros:
            print(f"{self.contador} {x}")
            self.contador +=1

        for c in range (self.pre):
            print(" ------------- Libro ",c,"------------ ")
            self.lib = input("Digite el nombre del libro: ")
            if self.lib in Libros:
                for x in range(1):
                    self.escoger1 = random.choice(ISBN)
                    self.escoger2 = random.choice(Paginas)
                    self.escoger3 = random.choice(Edicion)
                    self.escoger4 = random.choice(Editorial)
                    self.SetAutor(input("Digite el nombre del autor: ")); self.SetLugar(input("Digite el lugar del libro: ")); self.SetFecha(input("Digite la fecha de edición: ")) 
            print(self.escoger1, self.escoger2, self.escoger3, self.escoger4)
            New_Guardado =(self.lib,self.escoger1,self.escoger2,self.escoger3,self.escoger4, self.Nombre_Autor, self.Lugar, self.FechaEdi)
            Guardado.append(New_Guardado)
# 2 Estructura del Libro
class Libro(Usuario,Prestar,Autor,Lugar, Fecha):

    Information = {'Nombre':'Biblioteca MundoChimba','NIT':'860508791-1','Respondable Iva':' CIIU  10B124','Agente':'Agente Retenedor de ICA','TEL':3156299375, 'N&C':'DG 23 69 55 LC 126','Dian':'Aut. DIAN 18764027319797'}

    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    segundos = datetime.datetime.now().second
    mes = datetime.datetime.now().month
    mes_u = mes + 1
    año = datetime.datetime.now().year

    if datetime.datetime.now().month == 12:
        año_u = año + 1
    else:
        año_u = año

    def __init__(self):
        super().__init__()
        super().Solicitar_Datos()
        super().Pedir_prestado()
        super().Prestando()
        Biblioteca = input = 'https://openlibra.com/es/collection/search/category/libros_programacion'
        qr = qrcode.QRCode(version=1,box_size=10,border=5)
        qr.add_data(Biblioteca)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')
        img.save('Biblioteca.png')
        self.Limpiando()
       
    def Mostrar(self,diccionario):
        self.Value = diccionario.items()
        print("\t                      ",list(self.Value)[0][1])
        print("\t                         NIT: ",list(self.Value)[1][1])
        print("\t                RESPONSABLE DE IVA.  ",list(self.Value)[2][1])
        print("\t                      ",list(self.Value)[3][1])
        print("\t                        TELEFONO:",list(self.Value)[4][1])
        print("\t                        ",list(self.Value)[5][1])
        print("\n\t          ",list(self.Value)[6][1], "      FEC  01/04/2022")
        print("\t           FECHA: ",datetime.datetime.now().day,"/",datetime.datetime.now().month,"/",datetime.datetime.now().year,"      Hora:",self.hora,":",self.minuto,":",self.segundos)
        print("\t           Nombre del autizado:",self.Nombre)
        print("\t           ===============================================")
        print("\t           ==========> LIBROS CON AUTORIZACIÓN <==========")
        print("\t           ===============================================")
        for c in range(self.pre):
            print("\t           ================== LIBRO N",c,"==================")
            print('\t           Titulo: ',Guardado[c][0])
            print("\t          ",Guardado[c][3])
            print('\t           Autor:',Guardado[c][5])
            print('\t           ISBN: ',Guardado[c][1])
            print("\t          ",Guardado[c][4],", ", Guardado[c][6],", ", Guardado[c][7])
            print("\t          ",Guardado[c][2],'páginas')
        print("\t           ============[ DETALLE DEL PRODUCTO ]=============")
        print("\t               Producto: Libros_Virtuales")
        print("\t               Fecha_limite: ",datetime.datetime.now().day,"/",self.mes_u,"/",self.año_u)
        print("\t           ===============================================")
        print("\t                      !GRACIAS POR ELEGIRNOS!")
        print("\t            Scanee esté código QR para que comiences a ")
        print("\t                disfrutar de los libros que pediste")
        print("\t                          AQUÍ VA EL CÓDIGO QR              ")
        print("\t        !Unete a nuestro programa de suscripción Libros_pack!")
        print("\t           ===============================================")
        print("\t               SI TIENES PROBLEMAS CON LA VISUALIZACIÓN")
        print("\t                ENVIANOS LOS DETALLES DEL PROBLEMA EN: ")
        print("\t                    BIBLIOTECHIMBA_MUNDOCHIMBA.COM      ")   
        w, h = letter
        B = canvas.Canvas('Factura_Biblioteca.pdf',pagesize=letter)
        B.setLineWidth(.2)
        B.setFont('Helvetica',10)
        B.rect(160,h-660,300,655)
        B.drawString(245, h-30, list(self.Value)[0][1])
        B.drawString(253, h-42,f"NIT:{list(self.Value)[1][1]}")
        B.drawString(204, h-55,f"RESPONSABLE DE IVA.  {list(self.Value)[2][1]}")
        B.drawString(238, h-67, list(self.Value)[3][1]) 
        B.drawString(236, h-79,f"TELEFONO:   {list(self.Value)[4][1]}")
        B.drawString(246, h-92, list(self.Value)[5][1])
        B.drawString(175, h-110,f"{list(self.Value)[6][1]}                FECHA  01/11/2022")
        B.drawString(175, h-121,f"Cliente con acceso: {self.Nombre}")
        B.drawString(175, h-130,"=============================================")
        B.drawString(175, h-142,"=========> LIBROS CON AUTORIZACIÓN <=========")
        B.drawString(175, h-152,"=============================================")
        for c in range(self.pre):
            B.drawString(175, h-162,f"================= LIBRO {c} ===================")
            B.drawString(175, h-172,f"Titulo: {Guardado[c][0]}")
            B.drawString(175, h-182,f"{Guardado[c][3]}")
            B.drawString(175, h-192,f"Autor: {Guardado[c][5]}")
            B.drawString(175, h-202,f"ISBN: {Guardado[c][1]}")
            B.drawString(175, h-212,f"{Guardado[c][4]}, {Guardado[c][6]}, {Guardado[c][7]}")
            B.drawString(175, h-222,f"{Guardado[c][2]} páginas")
            h = h-72
        B.drawString(175, h-220,"==========[ DETALLE DEL PRODUCTO ]===========")
        B.drawString(240,h-232," Producto: Libros_Virtuales")
        B.drawString(240, h-244,f" Fecha_limitada: {datetime.datetime.now().day} / {self.mes_u} / {self.año_u}")
        B.drawString(175, h-256,"=============================================")
        B.drawString(250, h-272,"!GRACIAS POR ELEGIRNOS!")
        B.drawString(200, h-284,"Scanee esté código QR para que comiences a ")
        B.drawString(235, h-296,"disfrutar de los libros que pediste")
        B.drawImage("Biblioteca.png",250, h-400,width=100, height=100)
        B.drawString(190,h-420,"!Unete a nuestro programa de suscripción Libros_pack!")
        B.drawString(175,h-432,"=============================================")
        B.drawString(195,h-444,"SI TIENES PROBLEMAS CON LA VISUALIZACIÓN")
        B.drawString(200,h-456,"ENVIANOS LOS DETALLES DEL PROBLEMA EN: ")
        B.drawString(218,h-468,"BIBLIOTECHIMBA_MUNDOCHIMBA.COM")

        # B.drawString(175, h-232,"==========[ DETALLE DEL PRODUCTO ]===========")
        # B.drawString(240,h-242," Producto: Libros_Virtuales")
        # B.drawString(240, h-252,f" Fecha_limitada: {datetime.datetime.now().day} / {self.mes_u} / {self.año_u}")
        # B.drawString(175, h-262,"=============================================")
        # B.drawString(250, h-272,"!GRACIAS POR ELEGIRNOS!")
        # B.drawString(200, h-282,"Scanee esté código QR para que comiences a ")
        # B.drawString(235, h-292,"disfrutar de los libros que pediste")
        # B.drawImage("Biblioteca.png",250, h-400,width=100, height=100)
        # B.drawString(190,h-420,"!Unete a nuestro programa de suscripción Libros_pack!")
        # B.drawString(175,h-432,"=============================================")
        # B.drawString(195,h-444,"SI TIENES PROBLEMAS CON LA VISUALIZACIÓN")
        # B.drawString(200,h-456,"ENVIANOS LOS DETALLES DEL PROBLEMA EN: ")
        # B.drawString(218,h-468,"BIBLIOTECHIMBA_MUNDOCHIMBA.COM") 
        B.save()
        self.Limpiando()
        # self.

if s == "Si" or s == "si" or s == "1":
    Lim = Limpiar()
    Lim.Limpiando()
    Objeto = Libro()
    Objeto.Mostrar(Objeto.Information)
else: 
    exit()