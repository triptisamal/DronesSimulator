import numpy as np
import matplotlib.pyplot as plt


# width of the bars
barWidth = 0.3

petal = [4,6,7,8,9]
flood = [4,6,7,8,8]

yerr_petal = [
0.2855,
0.4028,
0.4507,
0.5116,
0.5206
]
yerr_flood = [
0.2984,
0.4625,
0.4725,
0.526,
0.5513
]
fig = plt.figure()
# The x position of bars
r1 = np.arange(len(petal))
r2 = [x + barWidth for x in r1]

# Create blue bars
plt.bar(r1, petal, width = barWidth, color = 'blue', edgecolor = 'blue', yerr=yerr_petal, label='Petal')
 
# Create red bars
plt.bar(r2, flood, width = barWidth, color = 'red', edgecolor = 'red', yerr=yerr_flood, label='Flooding')
 
# general layout
plt.xticks([r + barWidth for r in range(len(petal))], ['27','64', '125', '216', '343'])
plt.xlabel('Number of Nodes', fontsize=15)
plt.ylabel("Average Number of Redundant\n Packets Delivered",fontsize=15)
plt.legend(loc="upper left")



plt.title('Perturbed Lattice, Petal Eccentricity = 0.4, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=15)
#plt.suptitle('',fontsize=15,wrap=True)
plt.subplots_adjust(top=0.82)


# Show graphic
plt.show()



fig.savefig('redundant_packets.png',
            format='png',
           dpi=100,
            bbox_inches='tight')
