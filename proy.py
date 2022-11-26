#Importarla libreria tkinter y todas sus funciones
from tkinter import *
from tkinter import Tk, Label, Button, Entry, Spinbox, OptionMenu, StringVar, Toplevel

#-----------------
#Ventana principal
#-----------------

#funciones
#funcion piernas
def piernas():
    ventana_piernas = Toplevel()
    ventana_piernas.title("Login")
    ventana_piernas.resizable(False, False)
    imagen=PhotoImage(file="piernas.png")
    fondo=Label(ventana_piernas, image=imagen)
    fondo.place(x=0,y=0)
    ventana_piernas.geometry("884x482")
    ventana_piernas.mainloop()

def brazos():
    ventana_brazos = Toplevel()
    ventana_brazos.title("Login")
    ventana_brazos.resizable(False, False)
    imagen=PhotoImage(file="brazos.png")
    fondo=Label(ventana_brazos, image=imagen)
    fondo.place(x=0,y=0)
    ventana_brazos.geometry("884x482")
    ventana_brazos.mainloop()


def abdomen():
    ventana_abdomen = Toplevel()
    ventana_abdomen.title("Login")
    ventana_abdomen.resizable(False, False)
    imagen=PhotoImage(file="abdomen.png")
    fondo=Label(ventana_abdomen, image=imagen)
    fondo.place(x=0,y=0)
    ventana_abdomen.geometry("884x482")
    ventana_abdomen.mainloop()

def cardio():
    ventana_cardio = Toplevel()
    ventana_cardio.title("Login")
    ventana_cardio.resizable(False, False)
    imagen=PhotoImage(file="cardio.png")
    fondo=Label(ventana_cardio, image=imagen)
    fondo.place(x=0,y=0)
    ventana_cardio.geometry("884x482")
    ventana_cardio.mainloop()

#Se declara una variable llamada ventana_principal y que adquiere las caracteristicas tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Proyecto")

#dimensiones de la ventana(ancho,alto)
ventana_principal.geometry("884x482")

#permite deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo
ventana_principal.config(bg="white")

#imagen de fondo
imagenfondo=PhotoImage(file="fondo.png")
fondo_principal=Label(ventana_principal, image=imagenfondo)
fondo_principal.place(x=0,y=0)


#boton
bt_pie = Button(fondo_principal, text=("Piernas") , command=piernas)
bt_pie.place(x=50, y=270, width=100, height=30)

#boton
bt_bra = Button(fondo_principal, text=("Brazos") , command=brazos)
bt_bra.place(x=278, y=270, width=100, height=30)

#boton
bt_ab = Button(fondo_principal, text=("Abdomen") , command=abdomen)
bt_ab.place(x=506, y=270, width=100, height=30)

#boton
bt_car = Button(fondo_principal, text=("Cardio") , command=cardio)
bt_car.place(x=734, y=270, width=100, height=30)






ventana_principal.mainloop()