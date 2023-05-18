import numpy as np
import matplotlib.pyplot as plt


# width of the bars
barWidth = 0.3

mm1 = [19,46,76,141]
mm2 = [14,32,58,106]

yerr_mm1 = [0.86,
1.9,
3.23,
5.39 ]

yerr_mm2 = [0.71,
1.55,
2.74,
4.52]
fig = plt.figure()
# The x position of bars
r1 = np.arange(len(mm1))
r2 = [x + barWidth for x in r1]

# Create blue bars
plt.bar(r1, mm1, width = barWidth, color = 'blue', edgecolor = 'black', yerr=yerr_mm1, capsize=7, label='Mobility Model 1')
 
# Create red bars
plt.bar(r2, mm2, width = barWidth, color = 'red', edgecolor = 'black', yerr=yerr_mm2, capsize=7, label='Mobility Model 2')
 
# general layout
plt.xticks([r + barWidth for r in range(len(mm1))], ['64', '125', '216', '343'])
plt.xlabel('Number of Nodes', fontsize=14)
plt.ylabel("Average Number of Transmissions",fontsize=14)
plt.legend(loc="upper left")



plt.title('Perturbed Lattice, Petal Eccentricity = 0.4, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=12)
plt.suptitle('',fontsize=15,wrap=True)
plt.subplots_adjust(top=0.85)


# Show graphic
plt.show()



fig.savefig('mmcomp.png',
            format='png',
           dpi=100,
            bbox_inches='tight')
