import tkinter as tk

def reset():
    entrada1.delete(0, tk.END)
    entrada1.insert(0, "")
    resultado.config(text="Resultado")

def convertir_fahrenheit():
    try:
        celsius = float(entrada1.get())
        fahrenheit = (celsius * 9 / 5) + 32
        resultado.config(text=f"{fahrenheit:.2f} \u00B0F")
    except ValueError:
        resultado.config(text="Error: entrada no valida")

def convertir_celsius():
    try:
        fahrenheit = float(entrada1.get())
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        resultado.config(text=f"{celsius:.2f} \u00B0C")
    except ValueError:
        resultado.config(text="Error: entrada no valida")

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")

# Definir el tamaño de la ventana (ancho x alto)
ventana.geometry("400x200")  # Puedes ajustar estos valores a lo que necesites

entrada = tk.Label(ventana, text="Entrada:")
entrada.grid(row=0, column=0)

entrada1 = tk.Entry(ventana)
entrada1.grid(row=2, column=0)

bt_convertir_C = tk.Button(ventana, text="Convertir a Celsius", command=convertir_celsius)
bt_convertir_C.grid(row=4, column=1)

salida = tk.Label(ventana, text="Salida:")
salida.grid(row=0, column=3)

resultado = tk.Label(ventana, text="Resultado")
resultado.grid(row=2, column=3)

bt_Convertir_F = tk.Button(ventana, text="Convertir a Fahrenheit", command=convertir_fahrenheit)
bt_Convertir_F.grid(row=5, column=1)

bt_Limpiar = tk.Button(ventana, text="Limpiar", command=reset)
bt_Limpiar.grid(row=6, column=1)

ventana.mainloop()
