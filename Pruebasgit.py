from tkinter import *
from matplotlib import pyplot as plt

name=['Semana 1','Semana 2','Semana 3','Semana 4']
plt.figure(figsize=(3,4))
plt.bar(name, [1000,2200,3300,122] )
plt.title('Ganancia personal semanal')
plt.ylabel('Dinero personal ganado')
plt.xlabel('Flujo(Semanal)')
plt.show()