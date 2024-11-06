import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 * num2
        messagebox.showinfo("Resultado", f" El producto es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 / num2
        messagebox.showinfo("Resultado", f"La division es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
 
ventana = tk.Tk()
ventana.title("Calculadora ")
ventana.geometry("450x100")
 
label_num1 = tk.Label(ventana, text="Número 1:", bg="red", fg="white", font=("Arial", 12, "bold"))
label_num1.grid(row=0, column=1)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=1, column=1)
 
label_num2 = tk.Label(ventana, text="Número 2:", bg="red", fg="white", font=("Arial", 12, "bold"))
label_num2.grid(row=0, column=3)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=3)
 
boton_sumar = tk.Button(ventana, text="Sumar", bg="black", fg="white", font=("Arial", 12), command=sumar)
boton_sumar.grid(row=3, column=0)

boton_restar = tk.Button(ventana, text="Restar", bg="black", fg="white", font=("Arial", 12), command=restar)
boton_restar.grid(row=3, column=1)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", bg="black", fg="white", font=("Arial", 12), command=multiplicar)
boton_multiplicar.grid(row=3, column=3)

boton_dividir = tk.Button(ventana, text="dividir", bg="black", fg="white", font=("Arial", 12), command=dividir)
boton_dividir.grid(row=3, column=4)

label_result = tk.Label(ventana, text="Resultado", bg="green", fg="white", font=("Arial", 12, "bold"))
label_result.grid(row=4, column=2)
 
ventana.mainloop()