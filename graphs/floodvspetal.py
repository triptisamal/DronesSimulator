import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
yer1=[0.796,
1.0118,
1.057855,
1.004098,
1.021409
]


yer2=[
0.044141,
0.044052,
0.44052,
0.044,
0.043
]
#petal
ax.plot([27, 64, 125,216,343],[13,14,14,14,14], color='blue',label="Petal")
#ax.plot([27, 64, 125,216,343],[13,14,14,14,14], color='blue',marker="o",markersize=2,label="Petal")

ax.errorbar([27,64, 125,216,343],[13,14,14,14,14], yerr = yer1,  color='black',ls='none')
#ax.errorbar([27,64, 125,216,343],[13,14,14,14,14], yerr = yer1,  color='black',capsize=3,ls='none')

#flood
ax.plot([27, 64, 125,216,343],[24, 61, 122,213,340], color='red',label="Flooding")
#ax.plot([27, 64, 125,216,343],[24, 61, 122,213,340], color='red',marker="o",markersize=5,label="Flooding")
ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',ls='none')
#ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',capsize=3,ls='none')
plt.legend(loc="upper left")
ax.set_xlabel("Number of Nodes", fontsize=15)
ax.set_ylabel("Average Number of Transmission",fontsize=15)

#ax.set_title('Comparison of Petal Routing and Flooding with equal distance between source and destination',loc='center', wrap=True,fontsize=16)
ax.set_title('Perturbed Lattice with sd 0.2, Petal Eccentricity = 0.4, source-destination distance ~ 75 feet, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=15)
fig.suptitle('With fixed distance between source and destination',fontsize=18,wrap=True)
plt.subplots_adjust(top=0.85)
plt.show()
fig.savefig('floodvspetal.png',
            format='png',
            dpi=100,
            bbox_inches='tight')
