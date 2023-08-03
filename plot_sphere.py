import matplotlib.pyplot as plt

fig, ax  = plt.subplots()
#yer1=[0.796,
#1.0118,
#1.057855,
#1.004098,
#1.021409
#]
#
#
#yer2=[
#0.044141,
#0.044052,
#0.44052,
#0.044,
#0.043
#]


#total nodes

y=[]
with open("total_nodes_inside_sphere.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y.append(num)


ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y, color='blue')
#ax.errorbar([27,64, 125,216,343],[13,14,14,14,14], yerr = yer1,  color='black',ls='none')




##flood
#ax.plot([27, 64, 125,216,343],[24, 61, 122,213,340], color='red',label="Flooding")
##ax.plot([27, 64, 125,216,343],[24, 61, 122,213,340], color='red',marker="o",markersize=5,label="Flooding")
#ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',ls='none')
##ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',capsize=3,ls='none')
plt.legend(loc="upper left")
ax.set_xlabel("Radius (coordinate units)", fontsize=15)
ax.set_ylabel("Total Number of Nodes",fontsize=15)

#ax.set_title('Comparison of Petal Routing and Flooding with equal distance between source and destination',loc='center', wrap=True,fontsize=16)
ax.set_title('Total nodes inside sphere',loc='center', wrap=True,fontsize=15)
#fig.suptitle('With fixed distance between source and destination',fontsize=18,wrap=True)
plt.subplots_adjust(top=0.85)
plt.show()
fig.savefig('totalnodesinsidesphere.png',
            format='png',
            dpi=100,
            bbox_inches='tight')


