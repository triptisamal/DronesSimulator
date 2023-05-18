import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
yer1=[0.66,
1.487,
2.558,
2.884,
4.571
]


yer2=[
0.429,
0.556,
0.7747,
1.336,
0.371 
]
#petal
ax.plot([27, 64, 125,216,343],[12,19,26,26,32], color='blue',marker="o", markersize=3,linewidth=1,label="Petal")
#ax.plot([27, 64, 125,216,343],[13,14,14,14,14], color='blue',marker="o",markersize=2,label="Petal")

ax.errorbar([27,64, 125,216,343],[12,19,26,26,32], yerr = yer1, linewidth=1, color='black',ls='none')
#ax.errorbar([27,64, 125,216,343],[13,14,14,14,14], yerr = yer1,  color='black',capsize=3,ls='none')

#flood
ax.plot([27, 64, 125,216,343],[22, 59, 118,208,334], color='red',marker="v",markersize=3,linewidth=1,label="Flooding")
ax.errorbar([27, 64, 125,216,343],[22, 59, 118,208,334], yerr = yer2, linewidth=1, color='black',ls='none')
##ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',capsize=3,ls='none')
plt.legend(loc="upper left")
ax.set_xlabel("Number of Nodes", fontsize=15)
ax.set_ylabel("Average Number of Transmission",fontsize=15)

#fig.suptitle('With fixed distance between source and destination',fontsize=18,wrap=True)

#ax.set_title('Perturbed Lattice with sd 0.9, Petal Eccentricity = 0.4,\n source-destination distance ~ 75 feet, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=15)
ax.set_title('Perturbed Lattice, Petal Eccentricity = 0.4,\n source-destination distance ~ 75 feet, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=15)

plt.subplots_adjust(top=0.82)
#plt.show()
fig.savefig('floodvspetal_morevariation.png',
            format='png',
            dpi=100,
            bbox_inches='tight')
