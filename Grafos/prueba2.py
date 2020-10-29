# -*- coding: utf-8 -*-
"""Prueba2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D7C21n_mqIgaUsyZG8aDMAUKIFFgSAVP
"""



# Commented out IPython magic to ensure Python compatibility.
# Importando algunas librerías que utilizaremos

# Networkx para grafos
import networkx as nx

# Pandas
import pandas as pd

# Mostrar imágenes
from IPython.display import HTML

# Mathplotlib
import matplotlib.pyplot as plt

# %matplotlib inline
plt.rcParams['figure.figsize'] = (20.0, 10.0)

from google.colab import files
uploades = files.upload()

"""Se incluye el costo del vuelo se carga un archivo sin cabeza  
Los datos se almacena en el dataframe df2
"""

df2 = pd.read_csv('costo.csv',  sep=';' , header = None, names =['origen', 'destino', 'precio'])

df2

G = nx.Graph()

G =  nx.from_pandas_edgelist( df2,'origen', 'destino', edge_attr ='precio')

pos = nx.spring_layout(G)

pos

G.nodes(data=True)

nx.draw_circular(G,
                 node_color="lightblue",
                 edge_color="gray",
                 font_size=24,
                 width=2, with_labels=True, node_size=3500,
)

nx.draw_planar(G,node_color="lightblue",
                 edge_color="gray",
                 font_size=24,
                 width=2, with_labels=False, node_size=3500)

list(nx.all_shortest_paths(G, source="MED", target='BOG '))

nx.draw(G, with_labels=True, node_color='lightgreen')

# https://en.wikipedia.org/wiki/Dijkstra's_algorithm
print("Dijkstra's algorithm")
HTML('<img src="https://upload.wikimedia.org/wikipedia/commons/2/23/Dijkstras_progress_animation.gif">')

# instruccion para calcular la ruta mas corta
list(nx.all_shortest_paths(G, source="BOG ", target='AGH'))

list(nx.all_shortest_paths(G, source="MED", target='BOG '))

#all_shortest_paths(G, source, target, weight=None, method='dijkstra')
list(nx.all_shortest_paths(G, source="BOG ", target='MED',weight=None))

#Devuelve una lista de nodos en la ruta más corta entre el origen y el destino utilizando el algoritmo A * ("A-star").
list(nx.astar_path(G, ("BOG "), ("MED"), weight='precio'))

list(nx.dijkstra_path(G, ("MED"), ("BOG "), weight='precio'))

list(nx.shortest_path(G, ("BOG "), ("MED"), weight='precio'))

list(nx.all_shortest_paths(G, source="MED", target='GPI',weight=None))

list(nx.dijkstra_path(G, ("MED"), ("GPI"), weight='precio'))