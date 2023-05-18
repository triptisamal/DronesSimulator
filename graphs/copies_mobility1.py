import numpy as np
import matplotlib.pyplot as plt


# width of the bars
barWidth = 0.3

petal = [9,9,10]
flood = [9,9,10]

yerr_petal = [0.15,
0.16,
0.16 ]

yerr_flood = [0.14,
0.16,
0.15]

# The x position of bars
r1 = np.arange(len(petal))
r2 = [x + barWidth for x in r1]
fig = plt.figure()
# Create blue bars
plt.bar(r1, petal, width = barWidth, color = 'blue', edgecolor = 'black', yerr=yerr_petal, capsize=7, label='Petal')
 
# Create red bars
plt.bar(r2, flood, width = barWidth, color = 'red', edgecolor = 'black', yerr=yerr_flood, capsize=7, label='Flood')
 
# general layout
plt.xticks([r + barWidth for r in range(len(petal))], ['64', '125', '216'])
plt.xlabel('Number of Nodes', fontsize=14)
plt.ylabel("Average Number of Packet Copies",fontsize=14)
plt.legend(loc="upper left")


plt.title('Perturbed Lattice, Petal Eccentricity = 0.4, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=12)
plt.suptitle('With varying distance between source and destination',fontsize=15,wrap=True)
plt.subplots_adjust(top=0.85)

# Show graphic
plt.show()



fig.savefig('copies_mobility1.png',
            format='png',
           dpi=100,
            bbox_inches='tight')
