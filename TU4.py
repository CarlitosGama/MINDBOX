import tkinter as tk
from tkinter import messagebox, ttk

# Excepción personalizada para errores en los datos de productos
class ProductError(Exception):
    pass

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not nombre:
            raise ProductError("El nombre del producto no puede estar vacío.")
        if precio <= 0:
            raise ProductError("El precio debe ser un número positivo.")
        if cantidad < 0:
            raise ProductError("La cantidad no puede ser negativa.")
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self, cantidad_seleccionada=None):
        if cantidad_seleccionada is None:
            return self.precio * self.cantidad
        return self.precio * cantidad_seleccionada

# Clase Tienda para manejar los productos
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

# Función para agregar un producto desde la interfaz gráfica
def agregar_producto():
    try:
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        producto = Producto(nombre, precio, cantidad)
        tienda.agregar_producto(producto)

        # Actualizar la lista de productos en la interfaz
        actualizar_lista_productos()

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado exitosamente.")
        
        # Limpiar las entradas
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos para el precio y la cantidad.")
    except ProductError as e:
        messagebox.showerror("Error", str(e))

# Función para mostrar el valor total del inventario
def mostrar_valor_inventario():
    valor_total = sum(producto.valor_total() for producto in tienda.productos)
    messagebox.showinfo("Valor Total del Inventario", f"El valor total del inventario es: ${valor_total:.2f}")

# Función para calcular el valor total de los productos seleccionados con cantidades específicas
def calcular_seleccion():
    seleccionados = lista_productos.curselection()
    valor_total_seleccion = 0
    
    if seleccionados:
        for i in seleccionados:
            producto = tienda.productos[i]
            try:
                cantidad_seleccionada = int(entry_cantidad_seleccion.get())
                if cantidad_seleccionada < 0:
                    raise ValueError("La cantidad seleccionada no puede ser negativa.")
                elif cantidad_seleccionada > producto.cantidad:
                    messagebox.showwarning("Advertencia", f"La cantidad seleccionada para '{producto.nombre}' supera el inventario disponible. Se usará la cantidad máxima disponible.")
                    cantidad_seleccionada = producto.cantidad
                valor_total_seleccion += producto.valor_total(cantidad_seleccionada)
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido para la cantidad seleccionada.")
                return
        messagebox.showinfo("Valor de Productos Seleccionados", f"Valor total de los productos seleccionados: ${valor_total_seleccion:.2f}")
    else:
        messagebox.showwarning("Atención", "Seleccione al menos un producto.")

# Función para actualizar la lista de productos en la interfaz
def actualizar_lista_productos():
    lista_productos.delete(0, tk.END)  # Limpiar la lista
    for idx, producto in enumerate(tienda.productos):
        lista_productos.insert(tk.END, f"ID {idx} - {producto.nombre} - Precio: ${producto.precio} - Cantidad: {producto.cantidad}")

# Configuración de la interfaz gráfica con tkinter
root = tk.Tk()
root.title("Sistema de Gestión de Productos")

# Crear la tienda
tienda = Tienda()

# Etiquetas y campos de entrada
tk.Label(root, text="Nombre del Producto:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Precio del Producto:").grid(row=1, column=0)
entry_precio = tk.Entry(root)
entry_precio.grid(row=1, column=1)

tk.Label(root, text="Cantidad en Inventario:").grid(row=2, column=0)
entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=2, column=1)

# Botones
btn_agregar = tk.Button(root, text="Agregar Producto", command=agregar_producto)
btn_agregar.grid(row=3, column=0)

btn_mostrar_valor = tk.Button(root, text="Mostrar Valor del Inventario", command=mostrar_valor_inventario)
btn_mostrar_valor.grid(row=4, column=0)

# Lista de productos
tk.Label(root, text="Productos:").grid(row=5, column=0, columnspan=2)
lista_productos = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
lista_productos.grid(row=6, column=0, columnspan=2)

# Campo de entrada para la cantidad seleccionada
tk.Label(root, text="Cantidad Seleccionada para el Cálculo:").grid(row=7, column=0)
entry_cantidad_seleccion = tk.Entry(root)
entry_cantidad_seleccion.grid(row=7, column=1)

# Botón para calcular el valor de los productos seleccionados con la cantidad específica
btn_calcular_seleccion = tk.Button(root, text="Calcular Valor Seleccionado", command=calcular_seleccion)
btn_calcular_seleccion.grid(row=8, column=0, columnspan=2)

# Iniciar la aplicación
root.mainloop()
