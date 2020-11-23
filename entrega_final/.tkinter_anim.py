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
	plt.xlabel('Iteração')