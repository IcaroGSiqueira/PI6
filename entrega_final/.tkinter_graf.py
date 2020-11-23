
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter_bd import *
from tkinter_anim import *

# define a janela principal
root = Tk()
root.title("Sistema de Monitoramento - PIVI") # titulo da janela
#root.iconbitmap("~/sexto_semestre/PI6/test/test.ico")
root.geometry("200x200") # tamanho da janela


'''
# inicia criação das abas
aba = ttk.Notebook(root)
aba.pack(side="top", pady=15)
#aba.grid()

#criação de quadros para organizar conjuntos de itens em abas diferentes
aba_quadro1 = Frame(aba, width=800, height=650, bg="#282923") 
aba_quadro2 = Frame(aba, width=800, height=650, bg="#282923")
aba_quadro3 = Frame(aba, width=800, height=650, bg="#282923")

aba_quadro1.pack(fill="y")
aba_quadro2.pack(fill="y")
aba_quadro3.pack(fill="y")
#aba_quadro1.grid()
#aba_quadro2.grid()

# cria abas
aba.add(aba_quadro1, text="Monitoramento")
aba.add(aba_quadro2, text="Busca")
aba.add(aba_quadro3, text="Gráfico")
'''

# define novas janelas
aba_quadro1 = Toplevel()
aba_quadro2 = Toplevel()
aba_quadro3 = Toplevel()

aba_quadro1.title("Monitoramento em Tempo Real") # titulo da janela
#root.iconbitmap("~/sexto_semestre/PI6/test/test.ico")
aba_quadro1.geometry("800x545") # tamanho da janela

aba_quadro2.title("Tabela de Busca no Banco de Dados") # titulo da janela
#root.iconbitmap("~/sexto_semestre/PI6/test/test.ico")
aba_quadro2.geometry("793x616") # tamanho da janela

aba_quadro3.title("Grafico do Histórico") # titulo da janela
#root.iconbitmap("~/sexto_semestre/PI6/test/test.ico")
aba_quadro3.geometry("800x676") # tamanho da janela

# cria quadros nas abas/janelas com para seus conteudos
frame_graph = Frame(aba_quadro1)
frame_lists = Frame(aba_quadro2)
frame_hist = Frame(aba_quadro3)

frame_graph.pack(side="right", padx=10, anchor="e")
frame_lists.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=5, pady=5, row=0, rowspan=1, sticky="n")
frame_hist.pack(side="right", padx=10, anchor="e")

# adiciona barra de rolagem a lista
scrolly = Scrollbar(frame_lists, orient="vertical")

# cria os campos de titulo das colunas
listt0 = Listbox(frame_lists, height=2, width=6, fg="#ffffff", bg="#404142")
listt0.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt1 = Listbox(frame_lists, height=2, width=6, fg="#ffffff", bg="#404142")
listt1.grid(column=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt2 = Listbox(frame_lists, height=2, width=6, fg="#ffffff", bg="#404142")
listt2.grid(column=2, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt3 = Listbox(frame_lists, height=2, width=8, fg="#ffffff", bg="#404142")
listt3.grid(column=3, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt4 = Listbox(frame_lists, height=2, width=8, fg="#ffffff", bg="#404142")
listt4.grid(column=4, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt5 = Listbox(frame_lists, height=2, width=8, fg="#ffffff", bg="#404142")
listt5.grid(column=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt6 = Listbox(frame_lists, height=2, width=6, fg="#ffffff", bg="#404142")
listt6.grid(column=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt7 = Listbox(frame_lists, height=2, width=9, fg="#ffffff", bg="#404142")
listt7.grid(column=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt8 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
listt8.grid(column=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt9 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
listt9.grid(column=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt10 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
listt10.grid(column=10, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt11 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
listt11.grid(column=11, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

listt12 = Listbox(frame_lists, height=2, width=13, fg="#ffffff", bg="#404142")
listt12.grid(column=12, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

# escreve os tutilos de coluna
listt0.insert("end", "CPU");listt0.insert("end", "Uso")
listt1.insert("end", "GPU");listt1.insert("end", "Uso")
listt2.insert("end", "GPU");listt2.insert("end", "MB")
listt3.insert("end", "RAM");listt3.insert("end", "Uso")
listt4.insert("end", "RAM");listt4.insert("end", "Livre")
listt5.insert("end", "CPU");listt5.insert("end", "MHz")
listt6.insert("end", "GPU");listt6.insert("end", "MHz")
listt7.insert("end", "Rede");listt7.insert("end", "kbps")
listt8.insert("end", "CPU");listt8.insert("end", "°C")
listt9.insert("end", "GPU");listt9.insert("end", "°C")
listt10.insert("end", "HDD");listt10.insert("end", "°C")
listt11.insert("end", "SSD");listt11.insert("end", "°C")
listt12.insert("end", "Data");listt12.insert("end", "Hora")

# cria as colunas de informaçoes
listbox0 = Listbox(frame_lists, height=25, width=6, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox0.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox1 = Listbox(frame_lists, height=25, width=6, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox1.grid(column=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox2 = Listbox(frame_lists, height=25, width=6, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox2.grid(column=2, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox3 = Listbox(frame_lists, height=25, width=8, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox3.grid(column=3, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox4 = Listbox(frame_lists, height=25, width=8, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox4.grid(column=4, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox5 = Listbox(frame_lists, height=25, width=8, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox5.grid(column=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox6 = Listbox(frame_lists, height=25, width=6, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox6.grid(column=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox7 = Listbox(frame_lists, height=25, width=9, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox7.grid(column=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox8 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox8.grid(column=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox9 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox9.grid(column=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox10 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox10.grid(column=10, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox11 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox11.grid(column=11, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

listbox12 = Listbox(frame_lists, height=25, width=13, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
listbox12.grid(column=12, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

# insere as informações nas colunas
def list_insert():
	

	nums = ("----,----,----,-------,--------,--------,----,--------,----,----,----,----,--------------")

	bd0,bd1,bd2,bd3,bd4,bd5,bd6,bd7,bd8,bd9,bd10,bd11,bd12 = nums.split(",")

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

# função que permite rolar todas colunas ao mesmo tempo
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

scrolly.config(command=scrollall)
scrolly.grid(column=13, padx=0, pady=0, row=1, rowspan=1, sticky="w")


#barra_load = ttk.Progressbar(aba_quadro2, orient="vertical", length=100, mode="determinate")
#barra_load.grid(column=1, padx=5, pady=5, row=0, sticky="n")
#barra_load.start(54)

# click1 = StringVar()
# click1.set("Selecione o Componente")

# click2 = StringVar()
# click2.set("Selecione a Informação")

# click3 = StringVar()
# click3.set("Selecione a Tabela")

# click4 = StringVar()
# click4.set("Selecione a Coluna")

# lista_comp = OptionMenu(frame_graph, click1, "CPU", "GPU", "RAM", "HDD", "SSD", "Rede")
# #lista_comp.pack(side="right", anchor="nw", padx=15, pady=25)
# lista_comp.grid(column=0, row=0, pady=100, sticky="n")

# lista_inf = OptionMenu(aba_quadro1, click2, "Uso", "Freq", "Mem", "Temp")
# lista_inf.pack(side="right", anchor="ne", padx=5, pady=25)
# #lista_inf.grid()

# lista_tabl = OptionMenu(aba_quadro2, click3, "CPU", "GPU", "RAM", "HDD", "SSD", "Rede")
# #lista_tabl.pack(side="top")
# lista_tabl.grid(column=1, row=0, pady=5, sticky="n")

# lista_colu = OptionMenu(aba_quadro2, click4, "CPU", "GPU", "RAM", "HDD", "SSD", "Rede")
# #lista_colu.pack(side="top")
# lista_colu.grid(column=1, row=0, pady=40, sticky="n")


r = StringVar()

def monitor(value):
	label = Label(root, text=value).pack()#grid(column=0, row=15, sticky="s")

Radiobutton(frame_graph, text="CPU Temp."	, variable=r, value=1, command = lambda: monitor(r.get())).grid(column=0, row=0, sticky="w")
Radiobutton(frame_graph, text="CPU Freq."	, variable=r, value=2, command = lambda: monitor(r.get())).grid(column=0, row=1, sticky="w")
Radiobutton(frame_graph, text="CPU Uso"		, variable=r, value=3, command = lambda: monitor(r.get())).grid(column=0, row=2, sticky="w")
Radiobutton(frame_graph, text="GPU Temp."	, variable=r, value=4, command = lambda: monitor(r.get())).grid(column=0, row=3, sticky="w")
Radiobutton(frame_graph, text="GPU Freq."	, variable=r, value=5, command = lambda: monitor(r.get())).grid(column=0, row=4, sticky="w")
Radiobutton(frame_graph, text="GPU Uso."	, variable=r, value=6, command = lambda: monitor(r.get())).grid(column=0, row=6, sticky="w")
Radiobutton(frame_graph, text="GPU Mem."	, variable=r, value=7, command = lambda: monitor(r.get())).grid(column=0, row=7, sticky="w")
Radiobutton(frame_graph, text="RAM Uso"		, variable=r, value=8, command = lambda: monitor(r.get())).grid(column=0, row=8, sticky="w")
Radiobutton(frame_graph, text="RAM Livre"	, variable=r, value=9, command = lambda: monitor(r.get())).grid(column=0, row=9, sticky="w")
Radiobutton(frame_graph, text="HDD Temp."	, variable=r, value=10, command = lambda: monitor(r.get())).grid(column=0, row=10, sticky="w")
Radiobutton(frame_graph, text="SSD Temp."	, variable=r, value=11, command = lambda: monitor(r.get())).grid(column=0, row=11, sticky="w")
Radiobutton(frame_graph, text="Rede Uso"	, variable=r, value=12, command = lambda: monitor(r.get())).grid(column=0, row=12, sticky="w")

ct = StringVar()
cf = StringVar()
cu = StringVar()
gt = StringVar()
gf = StringVar()
gu = StringVar()
gm = StringVar()
ru = StringVar()
rl = StringVar()
ht = StringVar()
st = StringVar()
wu = StringVar()

CT = Checkbutton(aba_quadro2, text="CPU Temp."	, variable=ct)
CT.deselect()
CT.grid(column=0, row=1, padx=5, sticky="w")

CF = Checkbutton(aba_quadro2, text="CPU Freq."	, variable=cf)
CF.deselect()
CF.grid(column=0, row=2, padx=5, sticky="w")

CU = Checkbutton(aba_quadro2, text="CPU Uso"	, variable=cu)
CU.deselect()
CU.grid(column=0, row=3, padx=5, sticky="w")

GT = Checkbutton(aba_quadro2, text="GPU Temp."	, variable=gt)
GT.deselect()
GT.grid(column=0, row=1, padx=105 , sticky="w")

GF = Checkbutton(aba_quadro2, text="GPU Freq."	, variable=gf)
GF.deselect()
GF.grid(column=0, row=2, padx=105 , sticky="w")

GU = Checkbutton(aba_quadro2, text="GPU Uso."	, variable=gu)
GU.deselect()
GU.grid(column=0, row=3, padx=105 , sticky="w")

GM = Checkbutton(aba_quadro2, text="GPU Mem."	, variable=gm)
GM.deselect()
GM.grid(column=0, row=1, padx=205 , sticky="w")

RU = Checkbutton(aba_quadro2, text="RAM Uso"	, variable=ru)
RU.deselect()
RU.grid(column=0, row=2, padx=205 , sticky="w")

RL = Checkbutton(aba_quadro2, text="RAM Livre"	, variable=rl)
RL.deselect()
RL.grid(column=0, row=3, padx=205 , sticky="w")

HT = Checkbutton(aba_quadro2, text="HDD Temp."	, variable=ht)
HT.deselect()
HT.grid(column=0, row=1, padx=305 , sticky="w")

ST = Checkbutton(aba_quadro2, text="SSD Temp."	, variable=st)
ST.deselect()
ST.grid(column=0, row=2, padx=305 , sticky="w")

WU = Checkbutton(aba_quadro2, text="Rede Uso"	, variable=wu)
WU.deselect()
WU.grid(column=0, row=3, padx=305 , sticky="w")

# configura os botões
botao0 = Button(root, text="QUIT", fg="#ffffff", bg="#404142", command=lambda:[stop_bd(),quit()], width=5)
#botao.grid()
botao0.pack(side="top", padx=20, anchor="se")

botao1 = Button(frame_graph, text="Iniciar", fg="#ffffff", bg="#404142", command=run_bd , width=5)
#botao1.pack(side="right", padx=20, anchor="se")
botao1.grid(column=0, row=13, sticky="s")

botao2 = Button(aba_quadro2, text="Busca", fg="#ffffff", bg="#404142", command=quary_bd, width=5)
botao2.grid(column=0, row=1, pady=0, padx=20, sticky="e")
#botao.pack()

botao3 = Button(aba_quadro2, text="Gráfico", fg="#ffffff", bg="#404142", width=5)
botao3.grid(column=0, row=3, pady=0, padx=20, sticky="e")
#botao.pack()

# inicia o grafico animado de monitoramento
graf = FigureCanvasTkAgg(fig, aba_quadro1)
#graf.show()
graf.get_tk_widget().pack(side="left", padx=15, pady=15)
#graf.get_tk_widget().grid()

# inicia a barra de ferramentas do grafico
toolbar = NavigationToolbar2TkAgg(graf, aba_quadro1)
#toolbar.update()
graf._tkcanvas.pack(side="top", fill="x")
#graf._tkcanvas.grid()

titulo_gh="tituloo"
label_gh="ladoo"

# altere o valor de "interval" para que que o frame seja atualizado de maneira mais rapida
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, titulo_gh, label_gh), interval=3333)
#plt.show(aba_quadro1)

root.mainloop()