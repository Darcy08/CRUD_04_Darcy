from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import database

window=Tk()
window.title("Ventana de Registro")
window.resizable(False,False)
window.geometry("950x630+220+20")
window.config(bg="#DBB991")

nombre = StringVar()
correo = StringVar()
clave = StringVar()

def crear_registro():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    clave = entry_clave.get()

    demo_db = database.MyDatabase()
    demo_db.insert_db(nombre,correo, clave)
       
   
def mostrar_registro():
    db_demo = database.MyDatabase()
    db_demo.read_db()
    fila = 0 
    for user in database.data:
        registro = user
        print('RESULTADO - FrontEnd: ' + str(fila) + " - " + str(registro))
        title1 = Label(window, 
              text=registro, 
              font=("Century Gothic", "15", "bold"), width=32,
              justify=LEFT, bg="#89745B")
        title1.place(x=13, y=530)
        fila = fila + 1     


imag = ImageTk.PhotoImage(Image.open("ropa.jpeg"))
my_label = Label(image=imag, bg="#DBB991")
my_label.place(x=420,y=-390)
lb = Label(text="Regístrate ",font=("Broadway",30),fg="white", bg="#89745B", width=10).place(x=68,y=40)

lb1 = Label(text="Nombre:",font=("Broadway",20),fg="black", bg="#DBB991").place(x=70,y=130)
entry_nombre = Entry(font=("Broadway",15),fg="black",width=18)
entry_nombre.place(x=70,y=172)

lb2 = Label(text="Correo electrónico:",font=("Broadway",20),fg="black", bg="#DBB991").place(x=70,y=225)
entry_correo = Entry(font=("Broadway",15),fg="black",width=22)
entry_correo.place(x=70,y=270)

lb3 = Label(text="Contraseña:",font=("Broadway",20),fg="black", bg="#DBB991").place(x=70,y=330)
entry_clave = Entry(font=("Broadway",15),fg="black",width=18)
entry_clave.place(x=70,y=370)

boton=Button(window,text="Registrarse",font=("Broadway",15),bg="#89745B",width=10,command= crear_registro).place(x=40,y=460)
boton_leer=Button(window,text="Leer registro",font=("Broadway",15),bg="#89745B",width=10,command= mostrar_registro).place(x=225,y=460)
window.mainloop()

