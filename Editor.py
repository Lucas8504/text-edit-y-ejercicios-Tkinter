from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from io import open

ruta = ""  # Almacena la ruta del fichero

# funcion que pregunta si salir sin guardar
def CsinGuardar():
    result = messagebox.askyesnocancel("Salir", "¿Quieres salir sin guardar?")
    if result is not None:             # None es Cancel esta condicional identifica a cancel para cancelar la operacion
        if result:
            root.destroy()
        else:
            guardar()
            root.destroy()
    else:
        pass


# funcion que compara el estado del fichero, contenido y ruta antes de guardar.
def sin_guardar():
    context = texto.get(1.0, 'end-1c')  # Guarda el contenido del cuadro de texto
    if context != "":
        if ruta == "":
            CsinGuardar()

        else:
            fichero = open(ruta, 'r')  # Abre el fichero y guarda la informacion en la variable
            contenido = fichero.read()  # Lee el fichero y guarda el contenido
            if context != contenido:  # Compara las variables para detectar cambios en el fichero
                CsinGuardar()
            else:
                root.destroy()
    else:
        root.destroy()


def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor.")


def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = filedialog.askopenfilename(initialdir="c:",
                                      filetypes=(("ficheros de texto", "*.txt"),),
                                      title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.insert('insert', contenido)
        fichero.close()
        root.title("Mi editor .  " + ruta)


def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guadado!")
    else:
        guardar_como()


def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = filedialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guadado!")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


# Comfiguracion de la raiz
root = Tk()
root.title("Mi editor")

# Menu superior
menubar = Menu(root)
# Menu archivo
file_Menu = Menu(menubar, tearoff=0)
file_Menu.add_command(label="Nuevo", accelerator="Ctrl+N", command=nuevo)
file_Menu.add_command(label="Abrir", command=abrir)
file_Menu.add_command(label="Guardar", command=guardar)
file_Menu.add_command(label="Guardar como", command=guardar_como)
file_Menu.add_separator()

file_Menu.add_command(label="Salir", command=sin_guardar)
menubar.add_cascade(menu=file_Menu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvariable=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)
root.protocol("WM_DELETE_WINDOW", sin_guardar)
# Finalmente bucle de la aplicacion
root.mainloop()