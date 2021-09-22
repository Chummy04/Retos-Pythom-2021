# Reto No. 3
import os
os.system ("cls")
#RF01
clave = 43615
coordenadas = []

def mostrar_coordenadas_frecuentes(matriz):
    for i in range(len(matriz)):
        print("coordenada [latitud,longitud] " + str(i + 1)+ " :", matriz[i])



def definirZonasWifi():
    zWifi = [[6.211,-72.482,2], [6.212,-72.470,25],[6.105,-72.342,25],[6.210,-72.442,50]]
    valZonas = 0
    for i in range (4):
        for j in range (2):
            if j==0:
                if zWifi[i][j]>6.306 or zWifi[i][j]<5.888:
                    print ("La latitud de la coordenada", i +1, "No está dentro de los limites indicados")
                    valZonas=1
            else:
                 if zWifi[i][j]>-72.321 or zWifi[i][j]<-72.552:
                     print ("La latitud de la coordenada", i +1, "No está dentro de los limites indicados")
                     valZonas=1
    if valZonas==0:
        print ("Las coordenas cumplen con los limites indicados")
    return (zWifi)
                        




menu =["Cambiar contraseña", "Ingresar coordenadas", "Ubicar Zonas Wifi más cercana", "XXXXX Wifi", "Guardar Archivo importado", "Menu favorito", "Cerrar sesión"]
intentos=0
while intentos<3:
    if intentos >=3:
        os.system("cls")
        print ("error")
        exit()
    for i in range(len(menu)):
        print(i)
        opcion = int (input("Usted ha elegido la Opcion "))
        if opcion>=1 and opcion<=7:
            if opcion==1:
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
#RF02
            elif opcion == 2:
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
                        print (" Coordenadas [Latitu,Longitud] " + str(i + 1) + ": ", coordenadas[i])
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
                    print("La coordenda promedio de todos los puntos [Laltitud,Longitud]: [" + str (latitud_prom)+ "," + str(longitud_prom) + "]")
                    try:
                        actualizar_coordenada = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú "))
                        if actualizar_coordenada >=1 and actualizar_coordenada <=3:
                            coordenadas[actualizar_coordenada - 1][0] = round(float(input("Digite la latitud para la coordenada" + str (actualizar_coordenada))+": "),3)
                            if coordenadas[int(actualizar_coordenada) - 1][0]>6.306 or coordenadas[int(actualizar_coordenada) - 1][0] <5.888:
                                print ("Error coordenadas")
                                exit ()
                            coordenadas[actualizar_coordenada - 1][1] = round(float(input("Digite la longitud para la coordenada" + str (actualizar_coordenada))+": "),3)
                            if coordenadas[int(actualizar_coordenada) - 1][1]>72.321 or coordenadas[int(actualizar_coordenada) - 1][1] <-72.552:
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
            elif opcion == 3:
                zWifi=definirZonasWifi()
                if len(coordenadas)==0:
                    print("Error sin registro de coordenadas")
                    exit()
                mostrar_coordenadas_frecuentes(coordenadas)
                try:
                    menu_ubicacion=int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión"))
                    if menu_ubicacion>=1 and menu_ubicacion<=3:
                        print("Zonas wifi cercanas con menos usuarios")
                except ValueError:
                    print("Error actualización")
                    exit ()
            else:
                print("Error")
        else:
            print("error")
            exit()
            break
    intentos=intentos + 1
    