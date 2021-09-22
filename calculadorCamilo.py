from tkinter import *

ventana = Tk()

ventana.title("Calculadora cuenta huevos")

pantalla=Entry(ventana, font=("Calibri 20"))
pantalla.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
indice=0
def digitar_value(valor):
    global indice
    valor =str(valor)
    caracteres = len(valor)
    pantalla.insert(indice,valor)
    indice +=caracteres

def calcular():
    ecuacion=pantalla.get()
    resultado = eval(ecuacion)
    pantalla.delete(0, END)
    pantalla.insert(0,resultado)
    indice = 0

def limpiar():
    pantalla.delete(0, END)
    indice = 0

def deshacer():
    global indice
    contenido_pantalla=pantalla.get()
    contenido_pantalla=(contenido_pantalla)
    if len(contenido_pantalla)>0:
        nuevo_contenido = contenido_pantalla[:-1]
        limpiar()
        pantalla.insert(0,nuevo_contenido)
        indice=indice-1
    else:
        limpiar()
        pantalla.insert(0,"Error")


boton_1=Button(ventana, text="1", command= lambda:digitar_value(1)).grid(row=1, column=0, sticky=W + E)
boton_2=Button(ventana, text="2", command= lambda:digitar_value(2)).grid(row=1, column=1, sticky=W + E)
boton_3=Button(ventana, text="3", command= lambda:digitar_value(3)).grid(row=1, column=2, sticky=W + E)

boton_4=Button(ventana, text="4", command= lambda:digitar_value(4)).grid(row=2, column=0, sticky=W + E)
boton_5=Button(ventana, text="5", command= lambda:digitar_value(5)).grid(row=2, column=1, sticky=W + E)
boton_6=Button(ventana, text="6", command= lambda:digitar_value(6)).grid(row=2, column=2, sticky=W + E)

boton_7=Button(ventana, text="7", command= lambda:digitar_value(7)).grid(row=3, column=0, sticky=W + E)
boton_8=Button(ventana, text="8", command= lambda:digitar_value(8)).grid(row=3, column=1, sticky=W + E)
boton_9=Button(ventana, text="9", command= lambda:digitar_value(9)).grid(row=3, column=2, sticky=W + E)

boton_resta=Button(ventana, text="-", command= lambda:digitar_value("-")).grid(row=4, column=0, sticky=W + E)
boton_0=Button(ventana, text="0", command= lambda:digitar_value(0)).grid(row=4, column=1, sticky=W + E)
boton_suma=Button(ventana, text="+", command= lambda:digitar_value("+")).grid(row=4, column=2, sticky=W + E)
boton_limpiar=Button(ventana, text="AC", command= lambda:limpiar()).grid(row=4, column=3, sticky=W + E)

boton_multi=Button(ventana, text="*", command= lambda:digitar_value("*")).grid(row=1, column=3, sticky=W + E)
boton_div=Button(ventana, text="/", command= lambda:digitar_value("/")).grid(row=2, column=3, sticky=W + E)
boton_potencia=Button(ventana, text="^", command= lambda:digitar_value("**")).grid(row=3, column=3, sticky=W + E)


boton_parentesis_iz=Button(ventana, text="(", command= lambda:digitar_value("(")).grid(row=1, column=4, sticky=W + E)
boton_parentesios_der=Button(ventana, text=")", command= lambda:digitar_value(")")).grid(row=2, column=4, sticky=W + E)
boton_punto=Button(ventana, text=".", command= lambda:digitar_value(".")).grid(row=3, column=4, sticky=W + E)
boton_borrar=Button(ventana, text="↼", command= lambda:deshacer()).grid(row=4, column=4, sticky=W + E)

boton_resultado=Button(ventana, text="=", command= lambda:calcular()).grid(row=5, column=1,columnspan=3, sticky=W + E)

ventana.mainloop()