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
with open("total_nodes_both_0.100000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y.append(num)


ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y, color='blue',label="e=0.1")



y1=[]
with open("total_nodes_both_0.200000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y1.append(num)
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y1, color='orange',label="e=0.2")



y2=[]
with open("total_nodes_both_0.300000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y2.append(num)

ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y2, color='green',label="e=0.3")



y3=[]
with open("total_nodes_both_0.400000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y3.append(num)
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y3, color='red',label="e=0.4")



y4=[]
with open("total_nodes_both_0.500000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y4.append(num)
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y4, color='brown',label="e=0.5")




y5=[]
with open("total_nodes_both_0.600000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y5.append(num)
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y5, color='purple',label="e=0.6")




y6=[]
with open("total_nodes_both_0.700000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y6.append(num)
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y6, color='cyan',label="e=0.7")



y7=[]
with open("total_nodes_both_0.800000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y7.append(num)
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y7, color='black',label="e=0.8")



y8=[]
with open("total_nodes_both_0.900000.txt") as myfile:
    Lines=myfile.readlines()[0:15] 


# Strips the newline character
for line in Lines:
    num = int(line.strip())
    y8.append(num)
ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],y8, color='yellow',label="e=0.9")


#ax.errorbar([27,64, 125,216,343],[13,14,14,14,14], yerr = yer1,  color='black',ls='none')




#flood
#ax.plot([27, 64, 125,216,343],[24, 61, 122,213,340], color='red',label="Flooding")
##ax.plot([27, 64, 125,216,343],[24, 61, 122,213,340], color='red',marker="o",markersize=5,label="Flooding")
#ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',ls='none')
##ax.errorbar([27, 64, 125,216,343],[24, 61, 122,213,340], yerr = yer2,  color='black',capsize=3,ls='none')
plt.legend(loc="upper left", fontsize=12)
ax.set_xlabel("Radius (coordinate units)", fontsize=15)
ax.set_ylabel("Total Number of Nodes",fontsize=15)

#ax.set_title('Comparison of Petal Routing and Flooding with equal distance between source and destination',loc='center', wrap=True,fontsize=16)
ax.set_title('Total nodes inside sphere and petal',loc='center', wrap=True,fontsize=15)
#fig.suptitle('With fixed distance between source and destination',fontsize=18,wrap=True)
plt.subplots_adjust(top=0.85)
plt.show()
fig.savefig('totalnodesinsideboth.png',
            format='png',
            dpi=100,
            bbox_inches='tight')


