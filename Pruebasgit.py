from matplotlib import pyplot as plt
from tkinter import*
import tkinter
import time
from tkinter import messagebox
from tkinter import font
from tkinter import Canvas


def Interfaz():
    window=Tk()
    window.geometry("500x300")
    window.title('Software para calcular costos personales') 
    labelframe=LabelFrame(window, text="Flujo de costo personal")
    labelframe.pack(fill="both",expand="yes")
Interfaz()

lenguajes=('python','C','java','GO','JavaScript')
slice= (100,130,90,80,128)
colores=('yellow','blue','brown','cyan','red')
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], [1000, 2200, 3000, 4000,2000,2533,5000,5600,2345,1220,3340,1222])
""" plt.plot([1, 2, 3, 4]) """


plt.title('Gastos personales')
plt.ylabel('Dinero personal gastado')
plt.xlabel('Flujo(Meses)')

plt.plot()

""" pyplot.pie(slice,colors=colores) """

""" plt.axis('equal') """
plt.show()