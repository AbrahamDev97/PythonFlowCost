from tkinter import *
from matplotlib import pyplot as plt

def cost():
    plt.plot([1,2,3,4,5,6,7,8,9,10,11,12], [1000, 2200, 3000, 4000,2000,2533,5000,5600,2345,1220,3340,1222])
    plt.title('Gastos personales')
    plt.ylabel('Dinero personal gastado')
    plt.xlabel('Flujo(Meses)')
    plt.axis()
    plt.show()

def Semanal():
    name=['Semana 1','Semana 2','Semana 3','Semana 4']
    plt.figure(figsize=(5,5))
    plt.bar(name, [int(semana1.get())+ int(extra1.get()) , int(semana2.get()) + int(extra2.get()) , int(semana3.get()) + int(extra3.get()), int(semana4.get())+ + int(extra4.get())] )
    plt.title('Ganancia personal semanal')
    plt.ylabel('Dinero personal ganado')
    plt.xlabel('Flujo(Semanal)')
    plt.show()

window=Tk()
window.geometry("500x400")
window.title('Software para calcular costos personales') 
#Gastos semanales calculando el flujo por dia
semana1 = StringVar() 
semana2 = StringVar()
semana3 = StringVar()
semana4 = StringVar()

extra1 = StringVar()
extra2 = StringVar()
extra3 = StringVar()
extra4 = StringVar()

etiqueta_costoLabel1 = Label(window, text="Ganancia 1°Semana:")
etiqueta_costoLabel1.grid(row = 1, column = 0, pady = 2) 
etiqueta_costoEntry1 = Entry(window,textvariable=semana1)
etiqueta_costoEntry1.grid(row = 1, column = 1, pady = 2) 
etiqueta_costoLabelex1 = Label(window, text=" + Ganancia extra:")
etiqueta_costoLabelex1.grid(row = 1, column = 2, pady = 2)
etiqueta_costoEntryex1 = Entry(window,textvariable=extra1)
etiqueta_costoEntryex1.insert(0, '0')
etiqueta_costoEntryex1.grid(row = 1, column = 3, pady = 2) 

etiqueta_costoLabel2 = Label(window, text="Ganancia 2°Semana:")
etiqueta_costoLabel2.grid(row = 2, column = 0, pady = 2) 
etiqueta_costoEntry2 = Entry(window,textvariable=semana2)
etiqueta_costoEntry2.grid(row = 2, column = 1, pady = 2) 
etiqueta_costoLabelex2 = Label(window, text=" + Ganancia extra:")
etiqueta_costoLabelex2.grid(row = 2, column = 2, pady = 2)
etiqueta_costoEntryex2 = Entry(window,textvariable=extra2)
etiqueta_costoEntryex2.insert(0, '0')
etiqueta_costoEntryex2.grid(row = 2, column = 3, pady = 2) 

etiqueta_costoLabel3 = Label(window, text="Ganancia 3°Semana:")
etiqueta_costoLabel3.grid(row = 3, column = 0, pady = 2) 
etiqueta_costoEntry3 = Entry(window,textvariable=semana3)
etiqueta_costoEntry3.grid(row = 3, column = 1, pady = 2) 
etiqueta_costoLabelex3 = Label(window, text=" + Ganancia extra:")
etiqueta_costoLabelex3.grid(row = 3, column = 2, pady = 2)
etiqueta_costoEntryex3 = Entry(window,textvariable=extra3)
etiqueta_costoEntryex3.insert(0, '0')
etiqueta_costoEntryex3.grid(row = 3, column = 3, pady = 2) 

etiqueta_costoLabel4 = Label(window, text="Ganancia 4°Semana:")
etiqueta_costoLabel4.grid(row = 4, column = 0, pady = 2) 
etiqueta_costoEntry4 = Entry(window,textvariable=semana4)
etiqueta_costoEntry4.grid(row = 4, column = 1, pady = 2) 
etiqueta_costoLabelex4 = Label(window, text=" + Ganancia extra:")
etiqueta_costoLabelex4.grid(row = 4, column = 2, pady = 2)
etiqueta_costoEntryex4 = Entry(window,textvariable=extra4)
etiqueta_costoEntryex4.insert(0, '0')
etiqueta_costoEntryex4.grid(row = 4, column = 3, pady = 2) 

boton_costo=Button(window, text="Calcular", command=Semanal)
boton_costo.grid(row = 5, column = 1, pady = 3) 

#50% La mitad de las ganancias se tienen que cubrir los gatos
#20% para ahorro
#30% Gastos  extra,
window.mainloop()
