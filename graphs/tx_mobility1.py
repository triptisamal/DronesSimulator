import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
yer1=[0.73,
1.48,
2.67]

yer2=[0.04,
0.4405,
0.044
]
ax.plot([64, 125, 216],[21, 43, 83], color='blue',marker="o",markersize=5,label="Petal")

ax.errorbar([64, 125, 216],[21, 43, 83], yerr = yer1,  color='black',capsize=3,ls='none')


ax.plot([64, 125, 216],[61, 122, 213], color='red',marker="o",markersize=5,label="Flooding")
ax.errorbar([64, 125, 216],[61, 122, 213], yerr = yer2,  color='black',capsize=3,ls='none')
plt.legend(loc="upper left")
ax.set_xlabel("Number of Nodes", fontsize=14)
ax.set_ylabel("Average Number of Transmission",fontsize=14)
ax.set_title('Perturbed Lattice, Petal Eccentricity = 0.4, 500 iterations, 99% CI',loc='center', wrap=True,fontsize=12)
fig.suptitle('With varying distance between source and destination',fontsize=15,wrap=True)
plt.subplots_adjust(top=0.85)

plt.show()
fig.savefig('tx_mobility1.png',
            format='png',
            dpi=100,
            bbox_inches='tight')
