import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
yer1=[0.66,
1.487,
2.558,
2.884,
4.571
]


yer2=[0.796,
1.0118,
1.057855,
1.004098,
1.021409
]
#petal more variation
ax.plot([27, 64, 125,216,343],[12,19,26,26,32], color='purple',marker="o", markersize=3,linewidth=1,label="high perturbation (σ=0.9, μ=0)")
#ax.plot([27, 64, 125,216,343],[13,14,14,14,14], color='blue',marker="o",markersize=2,label="Petal")

ax.errorbar([27,64, 125,216,343],[12,19,26,26,32], yerr = yer1, linewidth=1, color='black',ls='none')
#ax.errorbar([27,64, 125,216,343],[13,14,14,14,14], yerr = yer1,  color='black',capsize=3,ls='none')

#petal less variation
ax.plot([27, 64, 125,216,343],[13,14,14,14,14], color='lightgreen',marker="v",markersize=3,linewidth=1,label="low perturbation (σ=0.2, μ=0)")
ax.errorbar([27, 64, 125,216,343],[13,14,14,14,14], yerr = yer2, linewidth=1, color='black',ls='none')
##ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',capsize=3,ls='none')
plt.legend(loc="upper left")
ax.set_xlabel("Number of Nodes", fontsize=15)
ax.set_ylabel("Average Number of Transmission",fontsize=15)

#fig.suptitle('Different variations in drone-platoons',fontsize=18,wrap=True)

ax.set_title('Perturbed Lattice, Petal Eccentricity = 0.4,\n source-destination distance ~ 75 feet, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=15)

plt.subplots_adjust(top=0.82)
#plt.show()
fig.savefig('variation.png',
            format='png',
            dpi=100,
            bbox_inches='tight')
