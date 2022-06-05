import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5
}

nx.draw_networkx(G, **options)

# Seta margens para evitar o corte de nos
# e não plota os eixos

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
