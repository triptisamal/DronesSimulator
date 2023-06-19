import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
yer1=[
0.7244,
1.9632,
3.8128,
6.6721,
10.4316]

yer2=[
0.3557,
0.3732,
0.2888,
0.3037,
0.3537
]



ax.plot([27, 64, 125, 216,343],[11,24,48,87,144], color='blue',marker="o",markersize=3,linewidth=1,label="Petal")

ax.errorbar([27, 64, 125, 216,343],[11,24,48,87,144], yerr = yer1,  color='black',ls='none')


ax.plot([27, 64, 125, 216,343],[22,59,119,209,334], color='red',marker="v",markersize=3,linewidth=1,label="Flooding")
ax.errorbar([27, 64, 125, 216,343],[22,59,119,209,334], yerr = yer2,  color='black',ls='none')
plt.legend(loc="upper left")
ax.set_xlabel("Number of Nodes", fontsize=15)
ax.set_ylabel("Average Number of Transmission",fontsize=15)
ax.set_title('Perturbed Lattice, Petal Eccentricity = 0.4, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=15)
#fig.suptitle('With varying distance between source and destination',fontsize=15,wrap=True)
plt.subplots_adjust(top=0.82)

plt.show()
fig.savefig('tx_vardist.png',
            format='png',
            dpi=100,
            bbox_inches='tight')
