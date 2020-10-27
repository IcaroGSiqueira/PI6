import subprocess 

# Grafico Animado -------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation #sudo apt install python3-tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from pandas import DataFrame
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#define o maximo de pontos plotados no grafico
n=10

#valores iniciais
xs = [0.0]
ys = [0.0]
tempo=0

def animate(i, xs, ys, titulo, label):

	global tempo
	tempo = tempo + 1

	#recebe o valor do banco
	output = 0
	#incremento do novo valor
	xs.append(tempo)
	ys.append(int(output))

	#mantem grafico dentro do intervalo de n plots
	if tempo > n:
		xs = xs[tempo-(n-1):tempo]
		ys = ys[tempo-(n-1):tempo]

	ax.clear()

	# desenhar x e y
	ax.plot(xs, ys)

	plt.title(titulo)
	plt.ylabel(label)
	plt.xlabel('Tempo')



# Conexão do Banco -------------------------------------------------------------------------

import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost', database='pivi', user='icaro', password='')

def quary_ocupa():
	cursor = connection.cursor()

	cursor.execute("SELECT * FROM Ocupação")
	records = cursor.fetchall()
	print(records)

	print_records = ""
	for record in records:
		print_records += str(record) + "\n"

	quary_label = Label(root, text=print_records)
	#quary_label.grid(row=3, column=0, columnspan=1)

	connection.commit()
	connection.close()

def quary_Perfo():
	cursor = connection.cursor()

	cursor.execute("SELECT * FROM Performance")
	records = cursor.fetchall()
	print(records)

	print_records = ""
	for record in records:
		print_records += str(record) + "\n"

	quary_label = Label(root, text=print_records)
	#quary_label.grid(row=3, column=0, columnspan=1)

	connection.commit()
	connection.close()

def quary_Temp():
	cursor = connection.cursor()

	cursor.execute("SELECT * FROM Temperaturas")
	records = cursor.fetchall()
	print(records)

	print_records = ""
	for record in records:
		print_records += str(record) + "\n"

	quary_label = Label(root, text=print_records)
	#quary_label.grid(row=3, column=0, columnspan=1)

	connection.commit()
	connection.close()	

def run_bd():
	#p = subprocess.Popen(["python3", "hw_info_psutil_BD.py"])
	p = subprocess.Popen([sys.executable, 'hw_info_psutil_BD.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
	return


# Interface Gráfica -------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


root = Tk()
root.title("Sistema de Monitoramento - PIVI")
#root.iconbitmap("~/sexto_semestre/PI6/test/test.ico")
root.geometry("800x650")


aba = ttk.Notebook(root)
aba.pack(side="top", pady=15)
#aba.grid()

aba_quadro1 = Frame(aba, width=750, height=600, bg="#282923")
aba_quadro2 = Frame(aba, width=750, height=600, bg="#282923")

aba_quadro1.pack(fill="y")
aba_quadro2.pack(fill="y")
#aba_quadro1.grid()
#aba_quadro2.grid()

aba.add(aba_quadro1, text="Gráfico")
aba.add(aba_quadro2, text="Busca")


nums = ("7.8	16	379	5117.79	15023.1	1841.16	450	6,000.17	65	51	39	45	20-09-16 17:35")
bd0,bd1,bd2,bd3,bd4,bd5,bd6,bd7,bd8,bd9,bd10,bd11,bd12 = nums.split("\t")


frame_lists = Frame(aba_quadro2, height=28)
frame_graph = Frame(aba_quadro1, height=500, width=50)


scrolly = Scrollbar(frame_lists, orient="vertical")

#listtt = Listbox(frame_lists, height=1, width=6, fg="#ffffff", bg="#404142")
#listtt.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")
#listtt.pack(side="bottom", fill="x")

#listbox = Listbox(frame_lists, height=26, width=74, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
#listbox.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")
#listbox.pack(side="bottom", fill="x")

listt0 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
listt0.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt1 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
listt1.grid(column=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt2 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
listt2.grid(column=2, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt3 = Listbox(frame_lists, height=2, width=8, fg="#ffffff", bg="#404142")
listt3.grid(column=3, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt4 = Listbox(frame_lists, height=2, width=8, fg="#ffffff", bg="#404142")
listt4.grid(column=4, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt5 = Listbox(frame_lists, height=2, width=8, fg="#ffffff", bg="#404142")
listt5.grid(column=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt6 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
listt6.grid(column=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt7 = Listbox(frame_lists, height=2, width=7, fg="#ffffff", bg="#404142")
listt7.grid(column=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt8 = Listbox(frame_lists, height=2, width=4, fg="#ffffff", bg="#404142")
listt8.grid(column=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt9 = Listbox(frame_lists, height=2, width=4, fg="#ffffff", bg="#404142")
listt9.grid(column=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt10 = Listbox(frame_lists, height=2, width=4, fg="#ffffff", bg="#404142")
listt10.grid(column=10, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt11 = Listbox(frame_lists, height=2, width=4, fg="#ffffff", bg="#404142")
listt11.grid(column=11, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt12 = Listbox(frame_lists, height=2, width=13, fg="#ffffff", bg="#404142")
listt12.grid(column=12, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")


listt0.insert("end", "CPU");listt0.insert("end", "Uso")
listt1.insert("end", "GPU");listt1.insert("end", "Uso")
listt2.insert("end", "GPU");listt2.insert("end", "MB")
listt3.insert("end", "RAM");listt3.insert("end", "Uso")
listt4.insert("end", "RAM");listt4.insert("end", "free")
listt5.insert("end", "CPU");listt5.insert("end", "MHz")
listt6.insert("end", "GPU");listt6.insert("end", "MHz")
listt7.insert("end", "Rede");listt7.insert("end", "kbps")
listt8.insert("end", "CPU");listt8.insert("end", "°C")
listt9.insert("end", "GPU");listt9.insert("end", "°C")
listt10.insert("end", "HDD");listt10.insert("end", "°C")
listt11.insert("end", "SSD");listt11.insert("end", "°C")
listt12.insert("end", "Data");listt12.insert("end", "Hora")


listbox0 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox0.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox1 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox1.grid(column=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox2 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox2.grid(column=2, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox3 = Listbox(frame_lists, height=25, width=8, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox3.grid(column=3, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox4 = Listbox(frame_lists, height=25, width=8, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox4.grid(column=4, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox5 = Listbox(frame_lists, height=25, width=8, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox5.grid(column=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox6 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox6.grid(column=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox7 = Listbox(frame_lists, height=25, width=7, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox7.grid(column=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox8 = Listbox(frame_lists, height=25, width=4, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox8.grid(column=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox9 = Listbox(frame_lists, height=25, width=4, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox9.grid(column=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox10 = Listbox(frame_lists, height=25, width=4, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox10.grid(column=10, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox11 = Listbox(frame_lists, height=25, width=4, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox11.grid(column=11, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox12 = Listbox(frame_lists, height=25, width=13, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox12.grid(column=12, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox0.insert("end", bd0)
listbox1.insert("end", bd1)
listbox2.insert("end", bd2)
listbox3.insert("end", bd3)
listbox4.insert("end", bd4)
listbox5.insert("end", bd5)
listbox6.insert("end", bd6)
listbox7.insert("end", bd7)
listbox8.insert("end", bd8)
listbox9.insert("end", bd9)
listbox10.insert("end", bd10)
listbox11.insert("end", bd11)
listbox12.insert("end", bd12)

def scrollall(*args):
	listbox0.yview(*args)
	listbox1.yview(*args)
	listbox2.yview(*args)
	listbox3.yview(*args)
	listbox4.yview(*args)
	listbox5.yview(*args)
	listbox6.yview(*args)
	listbox7.yview(*args)
	listbox8.yview(*args)
	listbox9.yview(*args)
	listbox10.yview(*args)
	listbox11.yview(*args)
	listbox12.yview(*args)

frame_lists.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=5, pady=5, row=0, rowspan=1, sticky="n")

scrolly.config(command=scrollall)
scrolly.grid(column=13, padx=0, pady=0, row=1, rowspan=1, sticky="w")



#barra_load = ttk.Progressbar(aba_quadro2, orient="vertical", length=100, mode="determinate")
#barra_load.grid(column=1, padx=5, pady=5, row=0, sticky="n")
#barra_load.start(54)



click1 = StringVar()
click1.set("Selecione o Componente")

click2 = StringVar()
click2.set("Selecione a Informação")

click3 = StringVar()
click3.set("Selecione a Tabela")

click4 = StringVar()
click4.set("Selecione a Coluna")

lista_comp = OptionMenu(frame_graph, click1, "CPU", "GPU", "RAM", "HDD", "SSD", "Rede")
#lista_comp.pack(side="right", anchor="nw", padx=15, pady=25)
lista_comp.grid(column=0, row=0, pady=100, sticky="n")

#lista_inf = OptionMenu(aba_quadro1, click2, "Uso", "Freq", "Mem", "Temp")
#lista_inf.pack(side="right", anchor="ne", padx=5, pady=25)
#lista_inf.grid()

#lista_tabl = OptionMenu(aba_quadro2, click3, "CPU", "GPU", "RAM", "HDD", "SSD", "Rede")
#lista_tabl.pack(side="top")
#lista_tabl.grid(column=1, row=0, pady=5, sticky="n")

#lista_colu = OptionMenu(aba_quadro2, click4, "CPU", "GPU", "RAM", "HDD", "SSD", "Rede")
#lista_colu.pack(side="top")
#lista_colu.grid(column=1, row=0, pady=40, sticky="n")


frame_graph.pack(side="right", padx=10, anchor="e")

botao0 = Button(root, text="QUIT", fg="#ffffff", bg="#404142", command=quit, width=5)
#botao.grid()
botao0.pack(side="top", padx=20, anchor="se")

botao1 = Button(frame_graph, text="Iniciar", fg="#ffffff", bg="#404142", command=run_bd , width=5)
#botao1.pack(side="right", padx=20, anchor="se")
botao1.grid(column=0, row=2, pady=100, sticky="s")

botao2 = Button(aba_quadro2, text="Busca", fg="#ffffff", bg="#404142", command=quary_Temp, width=5)
botao2.grid(column=1, row=0, pady=75, sticky="s")
#botao.pack()

botao3 = Button(aba_quadro2, text="Gráfico", fg="#ffffff", bg="#404142", width=5)
botao3.grid(column=1, row=0, pady=5, sticky="s")
#botao.pack()



graf = FigureCanvasTkAgg(fig, aba_quadro1)
#graf.show()
graf.get_tk_widget().pack(side="left", padx=15, pady=15)
#graf.get_tk_widget().grid()

toolbar = NavigationToolbar2TkAgg(graf, root)
#toolbar.update()
graf._tkcanvas.pack(side="left", fill="x")
#graf._tkcanvas.grid()



titulo="tituloo"
label="ladoo"

# altere o valor de "interval" para que que o frame seja atualizado de maneira mais rapida
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, titulo, label), interval=3333)
#plt.show(aba_quadro1)

root.mainloop()