import math
import os
os.system("cls")
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")




def mostrar_coordenadas_frecuentes(matriz):
    for i in range(len(matriz)):
        print("coordenada [latitud,longitud] " + str(i + 1)+ " :", matriz[i])



def definirZonasWifi():
    #coordenadas predeterminadas en el ejercicio
    zWifi = [[6.211,-72.482,2], [6.212,-72.470,25],[6.105,-72.342,25],[6.210,-72.442,50]] 
    valZonas = 0
    for i in range (4):
        for j in range (2):
            if j==0:
                if zWifi[i][j]>6.306 or zWifi[i][j]<5.888:
                    print ("La latitud de la coordenada", i + 1, "No está dentro de los limites indicados")
                    valZonas=1
            else:
                 if zWifi[i][j]>-72.321 or zWifi[i][j]<-72.552:
                     print ("La latitud de la coordenada", i + 1, "No está dentro de los limites indicados")
                     valZonas=1
    if valZonas==0:
        print ("Las coordenas cumplen con los limites indicados")
    return (zWifi)

def distancia_zonas(zona, punto):
    latitud1= math.radians(punto[0])
    longitud1= math.radians(punto[1])
    R=6372.795477598
    for i in range(len(zona)):
        latitud2=math.radians(zona[i][0])
        longitud2=math.radians(zona[i][1])
    #No se utiliza la operación math porque ya esta en radianes por el nombramiento de las variables
        delta_longitud=longitud2-longitud1 
    # Formula diferente porque el que hizo el codigo verifico que la formula más exacta en pagina de internte es la que sigue y no la de la guía
        distancia=(math.acos(math.sin(latitud1) * math.sin(latitud2) + math.cos(latitud1) * math.cos(latitud2) * math.cos(delta_longitud))) * R
        #distancia *=1000 Se convierte de Km a m
        distancia = round(distancia,3)
        zona[i].append(distancia) #Se adiciona una columna en la matriz para evitar organizar por listas una a una
    #Se ordenan las distancias
    for i in range(len(zona)-1):
        for j in range(i+1, len(zona)):
            if zona[i][3]>zona[j][3]:
                distancia_temp=zona[i]
                zona[i]=zona[j]
                zona[j]=distancia_temp
    return(zona[:2]) #se retornan las dos distancias menores

def ord_vector(vector):
    for i in range(len(vector)-1):
        for j in range(i+1,len(vector)):
            if vector[i][2]>vector[j][2]:
                usuarios_prom=vector[i]
                vector[i]=vector[j]
                vector[j]=usuarios_prom
    return(vector) #se retornan el vector ordenado pero por numero de usuarios

Nombredeusuario=51634
contraseña=43615
penultimo= (5-(6%4)*1)
velmoto=19.44 #m/s
velbici=3.33 #m/s

coordenadas = []
ubicacion_actual = []


nombre=int(input("Ingrese Nombre de usuario: "))
if nombre==Nombredeusuario:
    clave=int(input("Ingrese contraseña: "))
    if clave==contraseña:
        captcha=int(input("ingrese el valor de la suma de 634 + 3 = "))
        if captcha== (634+penultimo):
            print("Sesión iniciada") 
            #RF01: El programa muestra el siguiente menú de opciones
            import os
            os.system("cls")

            lista=["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", 
            "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión"]
            
            intentos=0           
            while intentos<3:
                if intentos >=3:
                    os.system("cls")
                    print ("error")
                    exit()
                for i in range (len(lista)):
                    print(str(i+1)+ ".", lista[i])
                try:
                    operacion = int(input("Elija una opción "))
                    if operacion >=1 and operacion <= 7:
                        if operacion == 1:
                            print ("Usted ha elegido la opción cambiar contraseña")
                            clave2 = int(input("digite la clave actual "))
                            if clave == clave2:
                                clave2 = int(input("digite la nueva clave  "))
                                if clave != clave2:
                                    clave = clave2
                                else:
                                    print("La nueva contraseña no puede ser igual a la anterior")
                            else:
                                print("Error")
                                exit ()
                        elif operacion == 2: #opcion para ingresar y cambiar coordenadas
                            if len(coordenadas)==0:
                                coordenadas = [[0]* 2 for i in range (3)]
                                for i in range (3):
                                    for j in range (2):
                                        if j==0:
                                            coordenadas [i][j]=float(input("Digite la latitud para la coordenada " + str(i + 1) + ": ")) 
                                            coordenadas [i][j]= round(coordenadas [i][j], 3)
                                            if coordenadas[i][j]>6.306 or coordenadas[i][j]<5.888:
                                                print ("Error coordenada")
                                                exit()
                                        else:
                                            coordenadas [i][j]=float(input("Digite la longitud para la coordenada "+ str(i + 1) + ": ")) 
                                            coordenadas [i][j]= round(coordenadas [i][j], 3)
                                            if coordenadas[i][j]>-72.321 or coordenadas[i][j]<-72.552:
                                                print ("Error coordenada")
                                                exit()
                                #RF03
                            else:
                                for i in range(3):
                                    print (" Coordenadas [Latitud,Longitud] " + str(i + 1) + ": ", coordenadas[i])
                                print ("La coordenada "+ str(coordenadas.index(min(coordenadas)) + 1) + " es la que esta más al sur")
                                latitud_prom = 0
                                longitud_prom = 0
                                for i in range (3):
                                    for j in range (2):
                                        if j ==0:
                                            latitud_prom = latitud_prom + coordenadas[i][j]
                                        else:
                                            longitud_prom = longitud_prom + coordenadas[i][j]
                                latitud_prom /=3
                                longitud_prom /=3
                                latitud_prom = round(latitud_prom, 3)
                                longitud_prom = round(longitud_prom, 3)
                                print("La coordenda promedio de todos los puntos [Latitud,Longitud]: [" + str (latitud_prom)+ "," + str(longitud_prom) + "]")
                                try:
                                    actualizar_coordenada = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú "))
                                    if actualizar_coordenada >=1 and actualizar_coordenada <=3:
                                        coordenadas[actualizar_coordenada - 1][0] = round(float(input("Digite la latitud para la coordenada " + str (actualizar_coordenada)+": ")),3)
                                        if coordenadas[int(actualizar_coordenada) - 1][0]>6.306 or coordenadas[int(actualizar_coordenada) - 1][0] <5.888:
                                            print ("Error coordenadas")
                                            exit ()
                                        coordenadas[actualizar_coordenada - 1][1] = round(float(input("Digite la longitud para la coordenada " + str (actualizar_coordenada)+": ")),3)
                                        if coordenadas[int(actualizar_coordenada) - 1][1]>-72.321 or coordenadas[int(actualizar_coordenada) - 1][1] <-72.552:
                                            print ("Error coordenadas")
                                            exit ()
                                    elif actualizar_coordenada ==0:
                                        pass
                                    else:
                                        print("Error actualización")
                                        exit ()
                                except ValueError:
                                    print("Error actualización")
                                    exit ()
                        elif operacion == 3:
                            zWifi=definirZonasWifi()
                            if len(coordenadas)==0:
                                print("Error sin registro de coordenadas")
                                exit()
                            mostrar_coordenadas_frecuentes(coordenadas)
                            try:
                                menu_ubicacion=int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión "))
                                if menu_ubicacion>=1 and menu_ubicacion<=3:
                                    cordistancia = distancia_zonas(zWifi, coordenadas[menu_ubicacion - 1])
                                    ubicacion_actual = coordenadas[menu_ubicacion-1].copy()
                                    cordistancia = ord_vector(cordistancia)
                                    print("Zonas wifi cercanas con menos usuarios")
                                    for i in range(len(cordistancia)):
                                        print("La zona wifi", i + 1, "ubicada en [", cordistancia[i][:2], "] a", cordistancia[i][3], "kilometros, tiene en promedio", cordistancia[i][2], "usuarios")
                                    try:
                                        ruta="Para llegar a la zona wifi dirigirse "
                                        indicaciones=int(input("Elija 1 o 2 para recibir indicaciones de llegada "))
                                        if indicaciones >= 1 and indicaciones <=2:
                                            if coordenadas[menu_ubicacion - 1][1] < cordistancia[indicaciones - 1][1]:
                                                ruta = ruta + "primero al oriente"
                                            elif coordenadas[menu_ubicacion - 1][1] > cordistancia[indicaciones - 1][1]:
                                                ruta = ruta + "primero al occidente"
                                            if coordenadas[menu_ubicacion - 1][0] < cordistancia[indicaciones - 1][0]:
                                                ruta = ruta + " y luego hacia al norte"
                                            elif coordenadas[menu_ubicacion - 1][0] > cordistancia[indicaciones - 1][0]:
                                                ruta = ruta + " y luego hacia al sur"
                                            tiempoMoto=(cordistancia[indicaciones-1][3]*10000)/velmoto
                                            tiempoBici=(cordistancia[indicaciones-1][3]*1000)/velbici
                                            tiempoMoto=round(tiempoMoto/60,2)
                                            tiempoBici=round(tiempoBici/60,2)
                                            print(ruta)
                                            print("Tiempo estimado en moto ",tiempoMoto," minutos")
                                            print("Tiempo estimado en bicicleta ",tiempoBici," minutos")
                                            while True:
                                                opcionSalir=input("Presione 0 para salir ")
                                                if opcionSalir == "0":
                                                    break
                                        else:
                                            print("Error zona wifi")
                                            exit ()
                                    except ValueError:
                                        print("Error zona wifi")
                                        exit ()
                                else:
                                    print("Error actualización")
                                    exit ()
                            except ValueError:
                                print("Error actualización")
                                exit ()
                        elif operacion == 4:
                            if len(coordenadas)==0:
                                print("Error de alistamiento")
                                exit()
                            if len(ubicacion_actual)==0:
                                print("Error de alistamiento")
                                exit()
                            wifi_cercanas={"actual":ubicacion_actual, "zonawifi1":[cordistancia[0][0:3]], "recorrido":[cordistancia[0][3],'Bicicleta', tiempoBici]}
                            print(wifi_cercanas)
                            while True:
                                opcion_menu=input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal ")
                                if opcion_menu =="1":
                                    try:
                                        archivo=open(r'C:\Users\Camilo\Desktop\DISEÑO_WEB\PYTHON\wifiCercano.txt',"w")
                                        archivo.write(str(wifi_cercanas))
                                        print("Exportando archivo")
                                        exit()
                                    except IOError:
                                        print("Exportando archivo")
                                        exit()
                                elif opcion_menu == "0":
                                    break
                        elif operacion == 5:
                            try:
                                archivo=open(r'C:\Users\Camilo\Desktop\DISEÑO_WEB\PYTHON\actualizaZonas.txt')
                                indice=0
                                #Ciclo para las zonas wifi desde los datos del archivo
                                for i in archivo.readlines(): #Se leee la linea y se agrega un salto de linea, osea un :\n
                                    #se elimina con el strip especio al inicio y al final
                                    zWifi[indice]=i.strip().split(',')
                                    zWifi[indice][0]=float(zWifi[indice][0])
                                    zWifi[indice][1]=float(zWifi[indice][1])
                                    zWifi[indice][2]=int(zWifi[indice][2])
                                    indice +=1
                                print("Estas son las zonas wifi actualizada")
                                print(zWifi)
                                while True:
                                    submenu=input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal ")
                                    if submenu == "0":
                                        break
                            except:
                                while True:
                                    submenu=input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal ")
                                    if submenu == "0":
                                        break
                        elif operacion == 6:
                            opcion = int(input("Seleccione opción favorita "))
                            if opcion >=1 and opcion<=5:
                                adivinanza1=3
                                adivinanza2=4
                                resadivinanza1 = int(input("Para confirmar por favor responda: Tengo forma de serpiente entre el 2 y 4 siempre estoy, ¿Quién soy?: "))
                                if resadivinanza1 == adivinanza1:
                                    resadivinanza2 = int(input("Para confirmar por favor responda: Cuatro gatos en un cuarto, cada gato en un rincón, cada gato ve tres gatos, adivina cuántos gatos son: "))
                                    if resadivinanza2 == adivinanza2:
                                        os.system("cls")
                                        if resadivinanza1 == adivinanza1 and resadivinanza2 == adivinanza2:
                                            opcfav=opcion-1
                                            adicional=lista[opcfav]
                                            lista.pop(opcfav)
                                            lista.insert(0,adicional)
                                        else:
                                            os.system("cls")
                                            print("Error")
                                    else:
                                        os.system("cls")
                                        print("Error")
                                else:
                                    os.system("cls")
                                    print("Error")
                            else: 
                                print("Error")
                                exit()   
                        elif operacion == 7:
                            print ("Hasta pronto")
                            exit()
                    else:
                        print("Error")
                except ValueError:
                    print("Error ")
                    break
                intentos=intentos + 1
        else:
            print("Error!")
    else:
        print("Error!")
else:
    print("Error!")











