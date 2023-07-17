import tkinter as tk

#Juan Felipe Rojas 
# Segunda parte 

def verificar_contrasena():
    global cliente, password
    password_input = password_entry.get()
    if password_input != 'crack':
        result_label.config(text='Contraseña incorrecta')
    else:
        result_label.config(text='Contraseña correcta')
        elegir_pelicula()

def elegir_pelicula():
    login_frame.pack_forget()
    pelicula_frame.pack()

def calcular_precio():
    global price
    opcion_pelicula = opcion_var.get()
    if opcion_pelicula == 1:
        price = 100
    elif opcion_pelicula == 2:
        price = 200
    else:
        price_label.config(text='Pelicula no disponible')
        return

    elegir_teatro()

def elegir_teatro():
    pelicula_frame.pack_forget()
    teatro_frame.pack()

def calcular_precio_final():
    global price
    opcion_teatro = teatro_var.get()
    if opcion_teatro == 1:
        price *= 1.0
    elif opcion_teatro == 2:
        price *= 0.9
    elif opcion_teatro == 3:
        price *= 0.8
    elif opcion_teatro == 4:
        price *= 0.6
    elif opcion_teatro == 5:
        price *= 0.4
    else:
        price_label.config(text='Opcion inválida')
        return

    desea_comida()

def desea_comida():
    teatro_frame.pack_forget()
    comida_frame.pack()

def calcular_precio_final_con_comida():
    global price
    opcion_comida = comida_var.get()
    if opcion_comida == 1:
        price += 20

    price_label.config(text='Precio: $' + str(price))

# Crear la ventana
ventana = tk.Tk()
ventana.title('VirtualFilm')
ventana.geometry('400x300')

# Variables globales
price = 0

# Frame para el login
login_frame = tk.Frame(ventana)
login_frame.pack(pady=20)
tk.Label(login_frame, text='!Bienvenido a VirtualFilm!', font=('Arial', 16)).pack()
tk.Label(login_frame, text='Digite usuario => ').pack()
cliente = tk.StringVar()
tk.Entry(login_frame, textvariable=cliente).pack()
tk.Label(login_frame, text='Digite contraseña => ').pack()
password = tk.StringVar()
password_entry = tk.Entry(login_frame, textvariable=password, show='*')
password_entry.pack()
tk.Button(login_frame, text='Ingresar', command=verificar_contrasena).pack()
result_label = tk.Label(login_frame, text='')
result_label.pack()

# Frame para elegir la película
pelicula_frame = tk.Frame(ventana)
tk.Label(pelicula_frame, text='Elegir película', font=('Arial', 14)).pack()
opcion_var = tk.IntVar()
opcion_var.set(1)
tk.Radiobutton(pelicula_frame, text='Avatar', variable=opcion_var, value=1).pack()
tk.Radiobutton(pelicula_frame, text='Avengers', variable=opcion_var, value=2).pack()
tk.Button(pelicula_frame, text='Continuar', command=calcular_precio).pack()
pelicula_frame.pack_forget()

# Frame para elegir el teatro
teatro_frame = tk.Frame(ventana)
tk.Label(teatro_frame, text='Elegir teatro', font=('Arial', 14)).pack()
teatro_var = tk.IntVar()
teatro_var.set(1)
tk.Radiobutton(teatro_frame, text='Chile', variable=teatro_var, value=1).pack()
tk.Radiobutton(teatro_frame, text='Gran Estacion', variable=teatro_var, value=2).pack()
tk.Radiobutton(teatro_frame, text='Hayuelos', variable=teatro_var, value=3).pack()
tk.Radiobutton(teatro_frame, text='Titan', variable=teatro_var, value=4).pack()
tk.Radiobutton(teatro_frame, text='Colina', variable=teatro_var, value=5).pack()
tk.Button(teatro_frame, text='Continuar', command=calcular_precio_final).pack()
teatro_frame.pack_forget()

# Frame para elegir si desea comida
comida_frame = tk.Frame(ventana)
tk.Label(comida_frame, text='¿Desea comida?', font=('Arial', 14)).pack()
comida_var = tk.IntVar()
comida_var.set(1)
tk.Radiobutton(comida_frame, text='Sí', variable=comida_var, value=1).pack()
tk.Radiobutton(comida_frame, text='No', variable=comida_var, value=2).pack()
tk.Button(comida_frame, text='Continuar', command=calcular_precio_final_con_comida).pack()
comida_frame.pack_forget()

# Frame para mostrar el precio final
price_label = tk.Label(ventana, text='Precio:')
price_label.pack()

ventana.mainloop()
