import networkx as nx
import matplotlib.pyplot as plt
 
G = nx.triangular_lattice_graph(m=2, n=2, periodic=False, with_positions=True, create_using=None)
plt.subplot(111)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
