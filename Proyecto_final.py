import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",
        database="proyecto-libreria"
    )

def validar_login():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if not usuario or not contrasena:
        messagebox.showerror("Error", "Complete todos los campos.")
        return

    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    query = "SELECT * FROM tabla_personas WHERE usuario = %s AND contraseña = %s"
    cursor.execute(query, (usuario, contrasena))
    resultados = cursor.fetchall()  

    if resultados: 
        for resultado in resultados:
            if resultado["rol"] == "administrador":
                abrir_gestion_empleados()
                break  
            elif resultado["rol"] == "empleado":
                abrir_gestion_libros()
                break
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
    
    conexion.close()


# crud para empleados
def cargar_empleados():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, apellido, usuario, rol FROM tabla_personas")
    registros = cursor.fetchall()
    
    for i in tree_empleados.get_children():
        tree_empleados.delete(i)
        
    for row in registros:
        tree_empleados.insert("", "end", values=row)  
    
    conexion.close()

def agregar_empleado():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    usuario = entry_usuario_emp.get()
    contrasena = entry_contrasena_emp.get()
    rol = combo_rol.get() 

    if not nombre or not apellido or not usuario or not contrasena or not rol:
        messagebox.showerror("Error", "Completa todos los campos.")
        return

    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "INSERT INTO tabla_personas (nombre, apellido, usuario, contraseña, rol) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, apellido, usuario, contrasena, rol))  # Pasa el valor, no el objeto
    conexion.commit()
    conexion.close()
    cargar_empleados()
    messagebox.showinfo("Éxito", "Empleado agregado correctamente.")


def eliminar_empleado():
    seleccion = tree_empleados.selection()
    if not seleccion:
        messagebox.showerror("Error", "Selecciona un empleado.")
        return

    id_empleado = tree_empleados.item(seleccion)["values"][0]
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "DELETE FROM tabla_personas WHERE id = %s"
    cursor.execute(query, (id_empleado,))
    conexion.commit()
    conexion.close()
    cargar_empleados()
    messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")



def limpiar_campos_2():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_usuario.delete(0, tk.END)
    entry_contrasena.delete(0, tk.END)
    combo_rol.delete(0, tk.END)

    global empleado_seleccionado_id
    empleado_seleccionado_id = None



def actualizar_empleado():
    try:
        if not empleado_seleccionado_id:
            messagebox.showerror("Error", "Selecciona un empleado para actualizar.")
            return

        nuevo_nombre = entry_nombre.get()
        nuevo_apellido = entry_apellido.get()
        nueva_usuario = entry_usuario_emp.get()
        nuevo_contrasena = entry_contrasena_emp.get()
        nuevo_rol = combo_rol.get()

        if not nuevo_nombre or not nuevo_apellido or not nueva_usuario or not nuevo_contrasena or not nuevo_rol:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = """
            UPDATE tabla_personas
            SET nombre = %s, apellido = %s, usuario = %s, contraseña = %s, rol = %s
            WHERE id = %s"""
        cursor.execute(query, (nuevo_nombre, nuevo_apellido, nueva_usuario, nuevo_contrasena, nuevo_rol, empleado_seleccionado_id))
        conexion.commit()
        conexion.close()

        cargar_empleados()  
        messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
        limpiar_campos_2()
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def seleccionar_empleado(event):
    seleccion = tree_empleados.selection()
    if not seleccion:
        return

    global empleado_seleccionado_id
    empleado_seleccionado_id = tree_empleados.item(seleccion)["values"][0]

    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, tree_empleados.item(seleccion)["values"][1])

    entry_apellido.delete(0, tk.END)
    entry_apellido.insert(0, tree_empleados.item(seleccion)["values"][2])

    entry_usuario_emp.delete(0, tk.END)
    entry_usuario_emp.insert(0, tree_empleados.item(seleccion)["values"][3])

    combo_rol.set(tree_empleados.item(seleccion)["values"][4])  



# crud para los libros

def cargar_libros():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, titulo, autor, editorial, año_publicacion, precio FROM tabla_libros")
    registros = cursor.fetchall()
    for i in tree_libros.get_children():
        tree_libros.delete(i) 

    for row in registros:
        tree_libros.insert("", "end", values=row)
    conexion.close()

def agregar_libro():
    try:
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        editorial = entry_editorial.get()
        anio = entry_anio.get()
        precio = entry_precio.get()

        
        if not anio.isdigit():
            raise ValueError("El año de publicación debe ser un valor numérico.")
        
        if not precio.replace('.', '', 1).isdigit():
            raise ValueError("El precio debe ser un valor numérico.")

        if not titulo or not autor or not editorial or not anio or not precio:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "INSERT INTO tabla_libros (titulo, autor, editorial, año_publicacion, precio) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (titulo, autor, editorial, anio, precio))
        conexion.commit()
        conexion.close()
        cargar_libros()
        messagebox.showinfo("Éxito", "Libro agregado correctamente.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def eliminar_libro():
    seleccion = tree_libros.selection()
    if not seleccion:
        messagebox.showerror("Error", "Selecciona un libro.")
        return

    id_libro = tree_libros.item(seleccion)["values"][0] 
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "DELETE FROM tabla_libros WHERE id = %s"
    cursor.execute(query, (id_libro,))
    conexion.commit()
    conexion.close()
    cargar_libros()
    messagebox.showinfo("Éxito", "Libro eliminado correctamente.")

# Filtrar libros
def filtrar_libros(editorial):
    if not editorial.strip():
        messagebox.showerror("Error", "Ingrese la editorial a filtrar.")
        return

    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "SELECT id, titulo, autor, editorial, año_publicacion, precio FROM tabla_libros WHERE editorial LIKE %s"
    cursor.execute(query, ('%' + editorial + '%',))  
    registros = cursor.fetchall()

    for i in tree_libros.get_children():
        tree_libros.delete(i)

    for row in registros:
        tree_libros.insert("", "end", values=row) 

    conexion.close()

# SelecciONAR Y actualizar  libros
def seleccionar_libro(event):
    seleccion = tree_libros.selection()
    if not seleccion:
        return

    global libro_seleccionado_id
    libro_seleccionado_id = tree_libros.item(seleccion)["values"][0]

    entry_titulo.delete(0, tk.END)
    entry_titulo.insert(0, tree_libros.item(seleccion)["values"][1]) 

    entry_autor.delete(0, tk.END)
    entry_autor.insert(0, tree_libros.item(seleccion)["values"][2])

    entry_editorial.delete(0, tk.END)
    entry_editorial.insert(0, tree_libros.item(seleccion)["values"][3])

    entry_anio.delete(0, tk.END)
    entry_anio.insert(0, tree_libros.item(seleccion)["values"][4])

    entry_precio.delete(0, tk.END)
    entry_precio.insert(0, tree_libros.item(seleccion)["values"][5])

def actualizar_libro():
    try:
        if not libro_seleccionado_id:
            messagebox.showerror("Error", "Selecciona un libro para actualizar.")
            return

        nuevo_titulo = entry_titulo.get()
        nuevo_autor = entry_autor.get()
        nueva_editorial = entry_editorial.get()
        nuevo_anio = entry_anio.get()
        nuevo_precio = entry_precio.get()

        # Validar que el precio sea un num
        if not nuevo_precio.replace('.', '', 1).isdigit():
            raise ValueError("El precio debe ser un valor numérico.")

        if not nuevo_titulo or not nuevo_autor or not nueva_editorial or not nuevo_anio or not nuevo_precio:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = """
            UPDATE tabla_libros SET titulo = %s, autor = %s, editorial = %s, año_publicacion = %s, precio = %s WHERE id = %s"""
        cursor.execute(query, (nuevo_titulo, nuevo_autor, nueva_editorial, nuevo_anio, nuevo_precio, libro_seleccionado_id))
        conexion.commit()
        conexion.close()

        cargar_libros() 
        messagebox.showinfo("Éxito", "Libro actualizado correctamente.")
        limpiar_campos()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def limpiar_campos():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_editorial.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

    global libro_seleccionado_id
    libro_seleccionado_id = None


def abrir_gestion_empleados():
    ventana_login.withdraw()
    ventana_empleados = tk.Toplevel(ventana_login)
    ventana_empleados.title("Gestión de Empleados")
    ventana_empleados.geometry("800x600")

    tk.Label(ventana_empleados, text="Gestión de Empleados", font=("Arial", 20)).pack(pady=10)
    
    global entry_nombre, entry_apellido, entry_usuario_emp, entry_contrasena_emp, combo_rol, tree_empleados

    tk.Label(ventana_empleados, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana_empleados)
    entry_nombre.pack()

    tk.Label(ventana_empleados, text="Apellido:").pack()
    entry_apellido = tk.Entry(ventana_empleados)
    entry_apellido.pack()

    tk.Label(ventana_empleados, text="Usuario:").pack()
    entry_usuario_emp = tk.Entry(ventana_empleados)
    entry_usuario_emp.pack()

    tk.Label(ventana_empleados, text="Contraseña:").pack()
    entry_contrasena_emp = tk.Entry(ventana_empleados, show="*")
    entry_contrasena_emp.pack()

    tk.Label(ventana_empleados, text="Rol:").pack()
    combo_rol = ttk.Combobox(ventana_empleados, values=["administrador", "empleado"])
    combo_rol.pack()

    tk.Button(ventana_empleados, text="Agregar", command=agregar_empleado).pack(pady=5)
    tk.Button(ventana_empleados, text="Eliminar", command=eliminar_empleado).pack(pady=5)
    tk.Button(ventana_empleados, text="Editar", command=actualizar_empleado).pack(pady=5)####editar

    columnas = ("ID", "Nombre", "Apellido", "Usuario", "Rol")
    tree_empleados = ttk.Treeview(ventana_empleados, columns=columnas, show="headings")
    for col in columnas:
        tree_empleados.heading(col, text=col)
    tree_empleados.pack(fill="both", expand=True)

    tree_empleados.bind("<Double-1>", seleccionar_empleado)

    cargar_empleados()

    tk.Button(ventana_empleados, text="Regresar", command=lambda: regresar(ventana_empleados)).pack(pady=10)

def abrir_gestion_libros():
    ventana_login.withdraw()
    global ventana_libros
    ventana_libros = tk.Toplevel(ventana_login)
    ventana_libros.title("Gestión de Libros")
    ventana_libros.geometry("800x600")

    global entry_titulo, entry_autor, entry_editorial, entry_anio, entry_precio, tree_libros, libro_seleccionado_id
    libro_seleccionado_id = None

    tk.Label(ventana_libros, text="Gestión de Libros", font=("Arial", 20)).pack(pady=10)
    
    tk.Label(ventana_libros, text="Título:").pack()
    entry_titulo = tk.Entry(ventana_libros)
    entry_titulo.pack()

    tk.Label(ventana_libros, text="Autor:").pack()
    entry_autor = tk.Entry(ventana_libros)
    entry_autor.pack()

    tk.Label(ventana_libros, text="Editorial:").pack()
    entry_editorial = tk.Entry(ventana_libros)
    entry_editorial.pack()

    tk.Label(ventana_libros, text="Año Publicación:").pack()
    entry_anio = tk.Entry(ventana_libros)
    entry_anio.pack()

    tk.Label(ventana_libros, text="Precio:").pack()
    entry_precio = tk.Entry(ventana_libros)
    entry_precio.pack()

    tk.Button(ventana_libros, text="Agregar", command=agregar_libro).pack(pady=5)
    tk.Button(ventana_libros, text="Eliminar", command=eliminar_libro).pack(pady=5)
    tk.Button(ventana_libros, text="Editar", command=actualizar_libro).pack(pady=5)  

    tk.Label(ventana_libros, text="Filtrar por Editorial:").pack()
    entry_filtro_editorial = tk.Entry(ventana_libros)
    entry_filtro_editorial.pack()
    tk.Button(ventana_libros, text="Filtrar", command=lambda: filtrar_libros(entry_filtro_editorial.get())).pack(pady=5)

    columnas = ("ID", "Título", "Autor", "Editorial", "Año Publicación", "Precio")
    tree_libros = ttk.Treeview(ventana_libros, columns=columnas, show="headings")

    for col in columnas:
        tree_libros.heading(col, text=col)  
    tree_libros.pack(fill="both", expand=True)  

    tree_libros.bind("<Double-1>", seleccionar_libro)

    cargar_libros()

    tk.Button(ventana_libros, text="Regresar", command=lambda: regresar(ventana_libros)).pack(pady=10)

# Regresar al login
def regresar(ventana_actual):
    ventana_actual.destroy()
    ventana_login.deiconify()

# Ventana principal
ventana_login = tk.Tk()
ventana_login.title("Entrar")
ventana_login.geometry("400x300")

tk.Label(ventana_login, text="Usuario", font=("Arial", 12)).pack(pady=5)
entry_usuario = tk.Entry(ventana_login)
entry_usuario.pack(pady=5)

tk.Label(ventana_login, text="Contraseña", font=("Arial", 12)).pack(pady=5)
entry_contrasena = tk.Entry(ventana_login, show="*")
entry_contrasena.pack(pady=5)

tk.Button(ventana_login, text="Entrar", command=validar_login).pack(pady=20)

ventana_login.mainloop()