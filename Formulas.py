from tkinter import *
from matplotlib import pyplot as plt

def cost():
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], [1000, 2200, 3000, 4000,2000,2533,5000,5600,2345,1220,3340,1222])
    plt.title('Gastos personales')
    plt.ylabel('Dinero personal gastado')
    plt.xlabel('Flujo(Meses)')
    plt.plot()
    plt.show()

def Semanal():
    plt.plot([1,2,3,4], [int(semana1.get()),int(semana2.get()), int(semana3.get()),int(semana4.get())] )
    plt.title('Gastos personales')
    plt.ylabel('Dinero personal gastado')
    plt.xlabel('Flujo(Meses)')
    plt.plot()
    plt.show()

window=Tk()
window.geometry("500x300")
window.title('Software para calcular costos personales') 
#Gastos semanales calculando el flujo por dia
semana1 = StringVar()
semana2 = StringVar()
semana3 = StringVar()
semana4 = StringVar()

etiqueta_costo = Label(window, text="Ingrese el 1°Semana:")
etiqueta_costo.pack()
etiqueta_costo = Entry(window,textvariable=semana1)
etiqueta_costo.pack()

etiqueta_costo2 = Label(window, text="Ingrese el 2°Semana:")
etiqueta_costo2.pack()
etiqueta_costo2 = Entry(window,textvariable=semana2)
etiqueta_costo2.pack()

etiqueta_costo3 = Label(window, text="Ingrese el 3°Semana:")
etiqueta_costo3.pack()
etiqueta_costo3 = Entry(window,textvariable=semana3)
etiqueta_costo3.pack()

etiqueta_costo4 = Label(window, text="Ingrese de 4°Semana:")
etiqueta_costo4.pack()
etiqueta_costo4 = Entry(window,textvariable=semana4)
etiqueta_costo4.pack()
boton_costo=Button(window, text="Calcular", command=Semanal)
boton_costo.pack()


window.mainloop()
