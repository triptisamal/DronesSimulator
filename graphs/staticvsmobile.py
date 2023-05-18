import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
yer1=[
0.66,
1.487,
2.558,
2.884,
4.571
]

yer2=[
0.423,
0.772,
1.079,
1.23,
2.78
]
#mobile
ax.plot([27, 64, 125,216,343],[12,19,26,26,32], color='blue',marker="o", markersize=3,linewidth=1,label="Mobile")
#ax.plot([27, 64, 125,216,343],[13,14,14,14,14], color='blue',marker="o",markersize=2,label="Petal")

ax.errorbar([27,64, 125,216,343],[12,19,26,26,32], yerr = yer1, linewidth=1, color='black',ls='none')
#ax.errorbar([27,64, 125,216,343],[13,14,14,14,14], yerr = yer1,  color='black',capsize=3,ls='none')

#static
ax.plot([27, 64, 125,216,343],[7,9,11,12,14], color='orange',marker="v",markersize=3,linewidth=1,label="Stationary")
#ax.plot([27, 64, 125,216,343],[24, 61, 122,213,340], color='red',marker="o",markersize=5,label="Flooding")
ax.errorbar([27, 64, 125,216,343],[7,9,11,12,14], yerr = yer2,  color='black',linewidth=1,ls='none')
#ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',capsize=3,ls='none')
plt.legend(loc="upper left")
ax.set_xlabel("Number of Nodes", fontsize=15)
ax.set_ylabel("Average Number of Transmission",fontsize=15)

#fig.suptitle('Stationary vs Mobile Drone-platoon',fontsize=18,wrap=True)

ax.set_title('Perturbed Lattice, Petal Eccentricity = 0.4, Group Mobility, \n source-destination distance ~ 75 feet, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=15)
#ax.set_title('Perturbed Lattice with sd 0.9, Petal Eccentricity = 0.4, Group Mobility, \n source-destination distance ~ 75 feet, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=15)
plt.subplots_adjust(top=0.82)
#plt.subplots_adjust(top=0.85)
#plt.show()
fig.savefig('staticvsmobile.png',
            format='png',
            dpi=100,
            bbox_inches='tight')
