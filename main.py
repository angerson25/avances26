#INPUT

print("\n Escoge la parte que quieras ejercitar: \n")

# Se despliega el menu
print("1. Brazos")
print("2. Piernas")
print("3. Abdomen")
print("4. Cardio")

ejercicios=int(input("\nDigite su opcion: "))

#PROCESAMIENTO
if(ejercicios==1):
    from tkinter import*
    ventana=Tk()
    ventana.title("Ejercicios Brazos")
    ventana.geometry("884x482")
    imagen=PhotoImage(file="brazos.png")
    fondo=Label(ventana, image=imagen).place(x=0,y=0)
    ventana.mainloop()

elif(ejercicios==2):
    from tkinter import*
    ventana=Tk()
    ventana.title("Ejercicios Piernas")
    ventana.geometry("884x482")
    imagen=PhotoImage(file="piernas.png")
    fondo=Label(ventana, image=imagen).place(x=0,y=0)
    ventana.mainloop()

elif(ejercicios==3):
    from tkinter import*
    ventana=Tk()
    ventana.title("Ejercicios Abdomen")
    ventana.geometry("884x482")
    imagen=PhotoImage(file="abdomen.png")
    fondo=Label(ventana, image=imagen).place(x=0,y=0)
    ventana.mainloop()

elif(ejercicios==4):
    from tkinter import*
    ventana=Tk()
    ventana.title("Ejercicios Cardio")
    ventana.geometry("884x482")
    imagen=PhotoImage(file="cardio.png")
    fondo=Label(ventana, image=imagen).place(x=0,y=0)
    ventana.mainloop()

else:
    print("ERROR, opcion no disponible")