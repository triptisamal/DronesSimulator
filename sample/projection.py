import numpy as np
import math

def mag(x):
    return math.sqrt(sum(i*i for i in x))



packet = {
            'dLoc':(3,4,5),   #destination location
            'sLoc':(2,2,7) #source location
           # 'myLoc':(2,6,4) #my location 
        }#message details

print(packet['dLoc'])
print(packet['sLoc'])
ds = tuple(map(lambda i, j: i - j, packet['sLoc'], packet['dLoc'] ))
print(ds)

myLoc = (2,6,4)
#directional vector
dt = tuple(map(lambda i, j: i - j, myLoc, packet['dLoc'] ))
print(dt)

#To find: projection of vector dt_v on ds_v

dt_v = np.array([dt[0],dt[1],dt[2]])
print(dt_v)
ds_v = np.array([ds[0],ds[1],ds[2]])
print(ds_v)

# finding norm of the vector ds_v
ds_v_norm = np.sqrt(sum(ds_v*ds_v)) 

# Apply the formula for projecting a vector onto another vector
# find dot product using np.dot()
proj_of_dsv_on_dtv = (np.dot(dt_v, ds_v)/ds_v_norm*ds_v_norm)*ds_v
print("Projection of Vector ds_v on Vector dt_v is: ", proj_of_dsv_on_dtv)



tb1 = (0.005 * mag(proj_of_dsv_on_dtv))/mag(ds_v)

print(tb1)
  





