#find if a point is inside an ellipsoid
import plotly.graph_objects as go
import networkx as nx
from networkx import grid_graph
import random
from random import randint
import math
import globalvars
import pylab
import numpy as np
import pickle

from itertools import combinations
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
import sys
import time

def process_each_line(line,edgelist):
    words = line.split()
    for word in words:
        edgelist.append(int(word))

def check_collision(node_loc):
    
    
    for u, v in combinations(globalvars.G, 2):
        
        dist = distance_between_nodes(u,v,node_loc)
        #print(dist)
        if dist <= 0.4: #if distance is less than 10 feet
            print("distance=",dist,"nodes",u,v,"are too close; adjusting positions")
            #to_del.append(u)
            #to_del.append(v)
            z_v = avoid_collision(u,v,node_loc)
            #update position of v
            
            index = int(v)
            posi = list(globalvars.pos[v])
            posi[2] = z_v
            globalvars.pos[v] = tuple(posi)
            
            #also update node_loc
            node_loc[v]['z'] = z_v
            #distance is 10 feet
            globalvars.G.add_edge(u, v)
            continue


def update_all_position(current_time):
    print("Updating at time: ", current_time)
    
    
    if int(sys.argv[6]) == globalvars.MobilityModel.PRESERVE_FORM.value:
        print("Updating the positions (coordinates) of all the nodes after moving")
        for i in range(globalvars.number_of_nodes):
            units = get_displacement(current_time)
            change_loc = (0,0,units)
            #find destination i to update the packet
            if globalvars.pos[i] == globalvars.packet['dLoc']:
                #Change destination in packet 
                curr_dest = calculate_current_dest(current_time,globalvars.packet['dLoc'])
                #curr_dest is the modified coordinates
                globalvars.packet['dLoc'] = curr_dest
                print("Updated destination globalvars.packet['dLoc']: ",globalvars.packet['dLoc'])
            
            globalvars.pos[i] = [sum(x) for x in zip(globalvars.pos[i],change_loc)]
            globalvars.node[i]['loc'] = globalvars.pos[i]
            if globalvars.packet['dLoc'] == globalvars.node[i]['loc']:
                print("YES packet dLoc is same as dest node loc")
#           print(globalvars.pos[i]) 

    if int(sys.argv[6]) == globalvars.MobilityModel.MODIFY_FORM.value:
        print("Updating the positions (coordinates) of the nodes that are moving (not all nodes are moving)")
        for i in range(globalvars.number_of_nodes):  
            move_yes_or_no = randint(0,1)
            if move_yes_or_no == 1:
                units = get_displacement(current_time)
                change_loc = (0,0,units)
                #find destination i to update the packet
                print("globalvars.pos[i] = ",globalvars.pos[i])
                print("globalvars.packet['dLoc']",globalvars.packet['dLoc'])
                if globalvars.pos[i] == globalvars.packet['dLoc']:
                    #Change destination in packet 
                    curr_dest = calculate_current_dest(current_time,globalvars.packet['dLoc'])
                    #curr_dest is the modified coordinates
                    globalvars.packet['dLoc'] = curr_dest
                    print("Updated destination globalvars.packet['dLoc']: ",globalvars.packet['dLoc'])
                
                globalvars.pos[i] = [sum(x) for x in zip(globalvars.pos[i],change_loc)]
                globalvars.node[i]['loc'] = globalvars.pos[i]
                #check is packet dLoc is same as dest node loc; it should be same
                if globalvars.packet['dLoc'] == globalvars.node[i]['loc']:
                    print("YES packet dLoc is same as dest node loc")
#           print(globalvars.pos[i])


def source_destination_distance():
    
    ff = (globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0])*(globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0])+(globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1])*(globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1])+(globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2])*(globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2])
    focaldist = math.sqrt(ff)

    #globalvars.sourcedestdistance = focaldist

    
    return focaldist


def magnitude(x):
 return math.sqrt(sum(i*i for i in x))

def calculate_backoff(location):

    '''returns backoff time in seconds'''

    validtB1 = 0
    validtB2 = 0
    proj_valid =0
    ##extract the exact x,y,z coordinates
    x = location[0]
    y = location[1]
    z = location[2]
    t = (x,y,z) #t is the node for which backoff is calculated

    #ds is the directional vector of line joining points d (destination) and s (source)
    #calculated by subtracting dest coordinates from source coordinates 
    ds = tuple(map(lambda i, j: i - j, globalvars.packet['sLoc'], globalvars.packet['dLoc'] ))
    print("ds: ",ds)
    #dt is the directional vector of line joining d (destination) and t (node for which backoff is calculated)
    dt = tuple(map(lambda i, j: i - j, t, globalvars.packet['dLoc']))
    print("dt: ",dt)

    #To find: projection of vector dt_v on ds_v

    dt_v = np.array([dt[0],dt[1],dt[2]])
    ds_v = np.array([ds[0],ds[1],ds[2]])

    # finding norm of the vector ds_v
    #ds_v_norm = np.sqrt(sum(ds_v**2)) 
    numerator = np.dot(dt_v, ds_v)
    denominator = np.dot(ds_v, ds_v)
    # Apply the formula for projecting a vector onto another vector
    # find dot product using np.dot()
    
    print("numerator:", numerator)
    print("denominator:",denominator)
    
   # time.sleep(2.4)
    if denominator:
        proj_of_dtv_on_dsv = np.multiply((numerator/denominator),ds_v)
        print(proj_of_dtv_on_dsv)
        proj_valid = 1
    #The above gives runtimewarning: invalid value encountered in double_scalars
    
    

    #backoff time proportional to the distance from destination
    if proj_valid:
        proj = magnitude(proj_of_dtv_on_dsv)
    else:
        proj = 0
 
    try:
        tB1 = (globalvars.packet['tUB1'] * proj)/magnitude(ds_v) 
        print("tB1: ",tB1)
        validtB1 = 1
    except ZeroDivisionError:
        print("tB1 is inf")
        print("magnitude(ds_v):", magnitude(ds_v))
        print("globalvars.packet['tUB1'] * proj:",globalvars.packet['tUB1'] * proj)
        
    #backoff time proportional to the distance from source-destination line
    #print("mag dt_v sq: ",(magnitude(dt_v))**2)
    #print("mag : proj_of_dtv_on_dsv sq",(magnitude(proj_of_dtv_on_dsv))**2)
  #  print("mag : proj_of_dtv_on_dsv sq",(proj)**2)
    #orthogonal_dist = math.sqrt((magnitude(dt_v))**2 - (magnitude(proj_of_dtv_on_dsv))**2)
    orthogonal_dist = math.sqrt((magnitude(dt_v))**2 - (proj)**2)
    print("orth dist: ",orthogonal_dist)

    try:
        tB2 = (globalvars.packet['tUB2'] * orthogonal_dist)/source_destination_distance() 
        print("tB2: ",tB2)
        validtB2 = 1
    except ZeroDivisionError:
        print("tB2 is inf")
        print("globalvars.packet['tUB2'] * orthogonal_dist:",globalvars.packet['tUB2'] * orthogonal_dist)
        print("source_destination_distance():", source_destination_distance())
 

    if validtB2 == 1 and validtB1 ==1:
        backofftime = tB1 + tB2
    else:
        backofftime = 0
 #   backofftime = magnitude(backofftime)

    return backofftime

def find_centroid(received_from_location):
    x = [p[0] for p in received_from_location]
    y = [p[1] for p in received_from_location]
    z = [p[2] for p in received_from_location]
    centroid = (sum(x) / len(received_from_location), sum(y) / len(received_from_location), sum(z)/len(received_from_location))

    print("centroid",centroid)

    return centroid


def compare_distance_to_destination(centroid,mylocation,destlocation):
    x1 = centroid[0]
    y1 = centroid[1]
    z1 = centroid[2]

    xd = destlocation[0]
    yd = destlocation[1]
    zd = destlocation[2]
    
    x2 = mylocation[0]
    y2 = mylocation[1]
    z2 = mylocation[2]
    
    
    dif = ((xd - x1 )**2) + ((yd-y1)**2) + ((zd-z1)**2)
    centroiddist = math.sqrt(dif)

    dif1 = ((xd - x2)**2) + ((yd-y2)**2) + ((zd-z2)**2)
    mydist = math.sqrt(dif1)
    print("dist from centroid",centroiddist) 
    print("dist from my location",mydist) 

    if centroiddist > mydist:
        return 1
    else:
        return 0


def insideCylinderOrNot(location):


    #Assuming the cylinder is defined by (p1,p2,r), check that the point q is inside the cylinder
    #p1 is cap1 centre, p2 is cap2 centre, r is radius given by W_p/2 

    #(vec_q - vec_p1).(vec_p2-vec_p1) >= 0
    #(vec_q - vec_p2).(vec_p2-vec_p1) <= 0
    ##if the above two cases are true, then point lies between the planes of the two circular facets of the cylinder


    condition1 = 0
    condition2 = 0
    #extract the exact x,y,z coordinates
    
    x = location[0]
    y = location[1]
    z = location[2]


    ##calculate the perpendicular distance of (x,y,z) = orthogonal_dist (in 2D) from sd line
   
    t = (x,y,z) #t is the node whose distance is calculated

    #ds is the directional vector of line joining points d (destination) and s (source)
    #calculated by subtracting dest coordinates from source coordinates 
    ds = tuple(map(lambda i, j: i - j, globalvars.packet['sLoc'], globalvars.packet['dLoc'] ))
    
    #st is the directional vector of line joining s (source) and t 
    st = tuple(map(lambda i, j: i - j, t, globalvars.packet['sLoc']))
 

    #finding projection of vector st on ds
    st_v = np.array([st[0],st[1],st[2]])
    ds_v = np.array([ds[0],ds[1],ds[2]])

    # finding norm of the vector ds_v
    numerator = np.dot(st_v, ds_v)
    denominator = np.dot(ds_v, ds_v)
    
    # Apply the formula for projecting a vector onto another vector
    # find dot product using np.dot()
    
    if denominator:
        proj_of_stv_on_dsv = np.multiply((numerator/denominator),ds_v)
        proj_valid = 1
    
    if proj_valid:
        proj = magnitude(proj_of_stv_on_dsv)
    else:
        proj = 0

    orthogonal_dist = math.sqrt((magnitude(st_v))**2 - (proj)**2)

    
    ##check-1: Lies inside the curved surface of the cylinder
    if orthogonal_dist <= globalvars.W_p/2: 
        #(W_p is the petal width) 
        condition1 = 1
        #then could be inside, continue to check-2
    else:
        return 0 


    ##check-2: Lies between the planes of the two circular facets of the cylinder
    
    t_v = np.array([x,y,z])
    cc1_v = np.array([globalvars.cc1[0],globalvars.cc1[1],globalvars.cc1[2]])
    cc2_v = np.array([globalvars.cc2[0],globalvars.cc2[1],globalvars.cc2[2]])
    
    if condition1 == 1:
        w1 = np.dot((t_v-cc1_v),(cc2_v-cc1_v))
        w2 = np.dot((t_v-cc2_v),(cc2_v-cc1_v))
        if w1 >= 0 and w2 <= 0:
            return 1
        else :
            return 0
        


def insideOrNot(location):

    #extract the exact x,y,z coordinates
    
    x = location[0]
    y = location[1]
    z = location[2]
        
    #eq of the ellipsoid centered at (h,k,f)

    h= (globalvars.pos[globalvars.focus1_key][0]+globalvars.pos[globalvars.focus2_key][0])/2
    k= (globalvars.pos[globalvars.focus1_key][1]+globalvars.pos[globalvars.focus2_key][1])/2
    f= (globalvars.pos[globalvars.focus1_key][2]+globalvars.pos[globalvars.focus2_key][2])/2

 #   v = [positions[focus2_key][0]-positions[focus1_key][0],positions[focus2_key][1]-positions[focus1_key][1],positions[focus2_key][2]-positions[focus1_key][2]]
 
    s = globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0]
    t = globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1]
    u = globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2]
    sol = ((t*(f-z)-u*(k-y))**2+(u*(h-x)-s*(f-z))**2+(s*(k-y)-t*(h-x))**2)/((globalvars.b**2)*(s**2+t**2+u**2)) + ((s*(h-x)+t*(k-y)+u*(f-z))**2)/((globalvars.a**2)*(s**2+t**2+u**2))    #semi axes are of lengths a, b, c

    if sol <= 1:
        return 1 #inside
    else:
        return 0


def write_to_file(src,dest,protocol):
    original_stdout = sys.stdout
    
    if protocol == 0:
        petal_source = "flood_source.txt" 
        petal_dest = "flood_dest.txt"
    else:
        petal_source = "petal_source.txt" 
        petal_dest = "petal_dest.txt"
         
        
        
    with open(petal_source,'a') as f:
        sys.stdout = f
        print(src)

    
    with open(petal_dest,'a') as f1:
        sys.stdout = f1
        print(dest)

    sys.stdout = original_stdout



def read_from_file(choice):
    
    #reading s and d
    if choice == 1:
        petal_source = "petal_source_all500.txt" 
        f=open(petal_source)
        lines1=f.readlines()
        
        if globalvars.protocol ==0:
            print("iteration for flooding: ",globalvars.iteration) 
        else:
            print("iteration for petal: ",globalvars.iteration) 

        globalvars.focus1_key = int(lines1[globalvars.iteration-1])
    
        petal_dest = "petal_dest_all500.txt"
        f1=open(petal_dest)
        lines=f1.readlines()
        globalvars.focus2_key = int(lines[globalvars.iteration-1])
        
        globalvars.s = globalvars.focus1_key
        globalvars.d = globalvars.focus2_key
        return 1


    #reading velocity
    if choice == 2:
        f1 = open("velocity_for_all")
        lines = f1.readline()
    #    print("Velocity read from file = ",lines,"m/s")
        return int(lines)
        



def initiate_source_destination():

    ret = 0
    
    print("protocol: ",globalvars.protocol);
    all_position_keys = []
    all_position_keys = list(globalvars.pos.keys())

    if globalvars.sd_random == 1:

        globalvars.focus1_key = np.random.choice(all_position_keys)
    
        while True:
            globalvars.focus2_key = np.random.choice(all_position_keys)
            if globalvars.focus1_key != globalvars.focus2_key:
                break
   
        globalvars.s = globalvars.focus1_key
        globalvars.d = globalvars.focus2_key
        ##in case we use cylinder petal, we will use s and d for all calculations

        #write_to_file(globalvars.focus1_key,globalvars.focus2_key)
        original_stdout = sys.stdout
        petal_source = "petal_source_all500.txt" 
        with open(petal_source,'a') as f:
            sys.stdout = f
            print(globalvars.focus1_key)

        petal_dest = "petal_dest_all500.txt" 
        with open(petal_dest,'a') as f1:
            sys.stdout = f1
            print(globalvars.focus2_key)

        sys.stdout = original_stdout
    elif globalvars.sd_random == 2:
        #choose s and d according to distance

        node_loc = [{'x':0, 'y':0, 'z':0} for i in range(0,globalvars.number_of_nodes+1)]
        for key, value in globalvars.pos.items():
            node_loc[key]['x'] = value[0]
            node_loc[key]['y'] = value[1]
            node_loc[key]['z'] = value[2]



        
        for u, v in combinations(globalvars.G, 2):
        
            dist = distance_between_nodes(u,v,node_loc)
            if round(dist) == 12:
                globalvars.focus1_key = u
                globalvars.focus2_key = v
                globalvars.s = globalvars.focus1_key
                globalvars.d = globalvars.focus2_key
                print("source-destination: distance",round(dist))

                break
        if globalvars.focus2_key ==0:
            print("ERR DESTINATION")
            sys.exit()


    else:
        ret = read_from_file(1)
    
    if ret == 1:
        print("Using source and destination from file")
    else:
        print("Using randomly generated source and destination")
    
    print("source:",globalvars.focus1_key)
    print("destination:",globalvars.focus2_key)
    
   # del(globalvars.G)
    #Initiating petal parameters for the first time
    initiate_petal_parameters(globalvars.PetalParamType.INIT.value)
    #calc_local_density()
    #globalvars.G.clear()
    #del(globalvars.G)
    #sys.exit()
    #find_points_inside_ellipsoid()

def get_displacement(current_time):
    vel = read_from_file(2)
    #position at time 0 is the initial position
    #position at time current_time is calculated basis velocity (uniform)
    #vel is in meters per second, current_time is in seconds
    #assumption all nodes are moving in z direction
    distance_travelled = vel*current_time
    #print("Current Time = ",current_time, "seconds")
    #print("Distance travelled = ",distance_travelled,"meters")
    #find new coordinates
    ##1 unit of distance is 25 feet or 7.62 meters
    units = distance_travelled/7.62
   
    return units


def calculate_current_dest(current_time,old_loc):
    print("Calculating current location based on movement")
    units = get_displacement(current_time)
    print("Distance travelled in coordinate units = ",units)
    print("Old coordinates = ", old_loc)
    change_loc = (0,0,units)
    new_loc = [sum(x) for x in zip(old_loc,change_loc)]
    
    print("New coordinates = ", new_loc)
    return new_loc



#choose midpoint/centre point of lattice to sanity check
def local_nodes(location,source,r):
    #extract the exact x,y,z coordinates
    
    x = location[0]
    y = location[1]
    z = location[2]

    a = source[0]
    b = source[1]
    c = source[2]

    sol = (x-a)**2 + (y-b)**2 + (z-c)**2 # (x - a)² + (y - b)² + (z - c)²
    r_sq = math.ceil(r*r)
    if sol <= r_sq:
        return 1 #inside
    return 0 

def calc_local_density():


    radius = 0
    s = globalvars.focus1_key
    
    edg = []
    for e in globalvars.G.edges:
        edg.append(e)


    print("total number of edges:",len(edg))
    #print(edg)
    #print(globalvars.G.edges)
    #print(edg)
    rad = [1,1.41,1.73,2,2.24,2.44,2.82,3,3.16,3.31,3.46,3.6,3.74,4]
    itr=0
    while itr <=13:
        total_connections = -1
        total_connections_both = -1
        total_potential_connections = -1
        total_ellip_circ = -1
        inside = 0
        inside_ellipsoid = 0
        for i in range(globalvars.number_of_nodes):

            inside = local_nodes(globalvars.node[i]['loc'],globalvars.packet['sLoc'],rad[itr])
            if inside:
                total_potential_connections +=1
                #point = (s,i)
                #if point in edg:
                #    total_connections += 1

                ##check if this point i is inside the ellipsoid
                #inside_ellipsoid = insideOrNot(globalvars.node[i]['loc'])
                #if inside_ellipsoid == 1:
                #    total_ellip_circ +=1
                #    point2 = (s,i)
                #    if point2 in edg:
                #        total_connections_both += 1
        itr +=1

        original_stdout = sys.stdout
        total_nodes_inside = "total_nodes_inside_sphere.txt"  
        total_connections_inside = "total_connection_inside_sphere.txt" 
        total_nodes_both = "total_nodes_both_%f.txt" % (globalvars.e) 
        total_connections_both = "total_connection_both_%f.txt" % (globalvars.e) 
        local_density = "local_density.txt" 
        with open(total_nodes_inside,'a') as f:
            sys.stdout = f
            print(total_potential_connections)

        with open(total_connections_inside,'a') as f1:
            sys.stdout = f1
            print(total_connections)
        
        with open(total_nodes_both,'a') as f2:
            sys.stdout = f2
            print(total_ellip_circ)
    
        with open(total_connections_both,'a') as f3:
            sys.stdout = f3
            print(total_connections_both)

        sys.stdout = original_stdout
       
       # if total_potential_connections >= 1:
       #     local_density = total_connections/total_potential_connections
       # for e in globalvars.G.edges:
       #     print(e)
    
    #return local_density


       
def nodes_in_volume_of_interest(focus1_key):

    #nodes in volume of interest V are the nodes inside the unit sphere with source at the centre that are also in 
    # the petal

    total_nodes = 0

    for i in range(globalvars.number_of_nodes):
        if i!=focus1_key:
            inside_unit_sphere = local_nodes(globalvars.node[i]['loc'],globalvars.packet['sLoc'],1)
            if inside_unit_sphere:
                inside_petal = insideCylinderOrNot(globalvars.node[i]['loc'])
                if inside_petal:
                    total_nodes += 1

    return total_nodes

def get_experienced_density(source):

    total_connections = 0
    edg = []
    for e in globalvars.G.edges:
        edg.append(e)


    for i in range(globalvars.number_of_nodes):
        inside = local_nodes(globalvars.node[i]['loc'],globalvars.packet['sLoc'],1)#change radius to increase density
        if inside:
            point = (source,i)
            if point in edg:
                total_connections += 1

  
    return total_connections

def get_threshold_density():
    return 6;

def decrease_height(h):
    return h-0.1

def getUnitVector(vector):
    unit_vector = vector / np.linalg.norm(vector)
    return unit_vector

def get_point_on_line(start, end, distance):
        z = end[2]-start[2]
        y = end[1]-start[1]
        x = end[0]-start[0]
        arr = []
        arr.append(x)
        arr.append(y)
        arr.append(z)
        vector = np.array(arr)
        unitVector = getUnitVector(vector)

        ar=[]
        ar.append(end[0])
        ar.append(end[1])
        ar.append(end[2])
        vec = np.array(ar)
        result = np.subtract(vec,unitVector*distance)
        return result

def initiate_petal_parameters(choice):

    print("PETAL PARAMETERS")
    print("----------------")

    if choice == 1:
        print("At the start:")
    print("Source key=",globalvars.focus1_key)
    print("Destination key=",globalvars.focus2_key)

    print("Coordinates of source: (", globalvars.pos[globalvars.focus1_key][0],",", globalvars.pos[globalvars.focus1_key][1],",", globalvars.pos[globalvars.focus1_key][2],")" )
    print("Coordinates of destination: (", globalvars.pos[globalvars.focus2_key][0],",", globalvars.pos[globalvars.focus2_key][1],",", globalvars.pos[globalvars.focus2_key][2],")" )
    
    #At the start of algorithm
    if choice == globalvars.PetalParamType.INIT.value:
        globalvars.packet['sLoc'] = (globalvars.pos[globalvars.focus1_key][0], globalvars.pos[globalvars.focus1_key][1], globalvars.pos[globalvars.focus1_key][2])
        globalvars.packet['dLoc'] = (globalvars.pos[globalvars.focus2_key][0], globalvars.pos[globalvars.focus2_key][1], globalvars.pos[globalvars.focus2_key][2])

        ff = (globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0])**2 +(globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1])**2+(globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2])**2
        focaldist = math.sqrt(ff)
        globalvars.sourcedestdistance = focaldist

        if globalvars.cylinder == 1:
            globalvars.height = globalvars.sourcedestdistance+1
        
            ds = tuple(map(lambda i, j: i - j, globalvars.packet['sLoc'], globalvars.packet['dLoc'] ))
            mag_ds = magnitude(ds)

            
            #cylinder cap centres cc1, cc2 are source and destination
            globalvars.cc2 = globalvars.packet['dLoc']
            globalvars.cc1 = globalvars.packet['sLoc']

    #when the destination is updated, in case of diverged petal algorithm

    if choice == globalvars.PetalParamType.MODIFY.value:
        #only for ellipsoid
        if globalvars.cylinder == 0:
            print("updating s and d")
            #New petal will have the current location of destination, 
            #but old location of source
            print("globalvars.packet['sLoc']: ",globalvars.packet['sLoc'])
            print("Destination: ",globalvars.packet['dLoc'])
            print("Source: ",globalvars.save_old_source)

            ff = (globalvars.packet['dLoc'][0]-globalvars.save_old_source[0])**2 +(globalvars.packet['dLoc'][1]-globalvars.save_old_source[1])**2+(globalvars.packet['dLoc'][2]-globalvars.save_old_source[2])**2
            focaldist = math.sqrt(ff)

   
    if globalvars.cylinder == 0:
        print("Distance between two foci =", focaldist)
        print("Linear eccentricity =", focaldist/2)
        print("Centre of ellipsoid = (", (globalvars.pos[globalvars.focus1_key][0]+globalvars.pos[globalvars.focus2_key][0])/2,",",(globalvars.pos[globalvars.focus1_key][1]+globalvars.pos[globalvars.focus2_key][1])/2,",",(globalvars.pos[globalvars.focus1_key][2]+globalvars.pos[globalvars.focus2_key][2])/2,")")
        #globalvars.e = calculate_eccentricity(globalvars.focus1_key)
        print("Eccentricity:",globalvars.e)
        #is that of the ellipse formed by a section containing both the longest and the shortest axes (one of which will be the polar axis (x axis))
        globalvars.a = focaldist/(2*globalvars.e)
        ma = globalvars.a+globalvars.a
        globalvars.c = globalvars.a * math.sqrt(1-(globalvars.e)**2)
        print("Semi major axis, a = ", globalvars.a)
        print("major axis, a+a = ", ma)
        print("Semi minor axis, b = ", globalvars.b)
        print("minor axis, b = ", globalvars.b+ globalvars.b)
        if focaldist > ma:
            print("incorrect")
        #globalvars.c = random.uniform(globalvars.b,globalvars.c)
        # a = b = c: sphere
        # a = b > c: oblate spheroid.
        # a = b < c: prolate spheroid
        # a > b > c: scalene spheroid or triaxial.
        globalvars.b = globalvars.c
        print("c = ",globalvars.c)



    if globalvars.cylinder == 1:
        if globalvars.increase_width == 0:
            globalvars.W_p = 2 #petal width initialize
        else:
            globalvars.W_p += globalvars.increase_width
        

        rho_e = get_experienced_density(globalvars.focus1_key)
        print("Experience density for source=",rho_e)
        rho_d = get_threshold_density()

        if rho_e > rho_d:
            while True:
                old_height = globalvars.height
                globalvars.height = decrease_height(globalvars.height)
                #update cc1

               # print("height:",globalvars.height)
                point = get_point_on_line(globalvars.cc1,globalvars.cc2,globalvars.height) 
                globalvars.cc1 = tuple(point)
               # print(globalvars.cc1)
                
             #   a = globalvars.cc2[0] - ((globalvars.height*(globalvars.cc2[0]-globalvars.cc1[0]))/old_height)
             #   b = globalvars.cc2[1] - ((globalvars.height*(globalvars.cc2[1]-globalvars.cc1[1]))/old_height)
             #   c = globalvars.cc2[2] - ((globalvars.height*(globalvars.cc2[2]-globalvars.cc1[2]))/old_height)
             #   globalvars.cc1 = (a,b,c)
             #   print(globalvars.cc1)
                N = nodes_in_volume_of_interest(globalvars.focus1_key)
                print("N=",N)
                if N <= rho_d:
                    break


         
        #Temp code: DO NOT DELETE YET
        #calc_local_density()
    #print("Local density:",density_source)



def generate_adjlist_with_all_edges(G,delimiter):
    
    for s, nbrs in globalvars.G.adjacency():
        line1 = str(s) + delimiter
        for t, data in nbrs.items():
            line1 += str(t) + delimiter
        yield line1[: -len(delimiter)]

def distance(u, v):
    x1 = globalvars.pos[u][0]
    x2 = globalvars.pos[v][0]
    y1 = globalvars.pos[u][1]
    y2 = globalvars.pos[v][1]
    z1 = globalvars.pos[u][2]
    z2 = globalvars.pos[v][2]
    
    dd = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1)
    d = math.sqrt(dd)
    return d


def avoid_collision(u, v, node_loc):
    
    #Adjust distance such that the nodes u and v have a minimu of 10 feet (0.4 euclidean) distance between them
    adjusted_distance = 0.4
    temp = adjusted_distance*adjusted_distance
    x1 = node_loc[u]['x']
    x2 = node_loc[v]['x']
    y1 = node_loc[u]['y']
    y2 = node_loc[v]['y']
    z1 = node_loc[u]['z']
    z2 = node_loc[v]['z']
    
    #Changing position of v
    #temp = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2_new-z1)*(z2_new-z1)
    z2_new = math.sqrt(temp-((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))+z1
    
    print("Old z:",z2)
    print("New z:",z2_new)
    return z2_new
    
    
def distance_between_nodes(u, v, node_loc):
    x1 = node_loc[u]['x']
    x2 = node_loc[v]['x']
    y1 = node_loc[u]['y']
    y2 = node_loc[v]['y']
    z1 = node_loc[u]['z']
    z2 = node_loc[v]['z']
    
    dd = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1)
    d = math.sqrt(dd)
    return d

def generate_random_3Dgraph(n_nodes, radius, seed=None):

    if seed is not None:
        random.seed(seed)
   
    node_loc = [{'x':0, 'y':0, 'z':0} for i in range(0,globalvars.number_of_nodes+1)]

    #wireless range: 25 to 50 feet
    #4 units of distance is 100 feet
    #Total area is 1000 x 1000 x 1000 cubic feet
    
   
    if globalvars.topology == 0: #Perfect Lattice
        n = 0
        side = int((globalvars.number_of_nodes+1)**(1.0/3))
        print(globalvars.number_of_nodes)
        print(side)
        while n < globalvars.number_of_nodes:
            for i in range(1,side+1):
                for j in range(1,side+1):
                    for k in range(1,side+1):
                        node_loc[n]['x'] = i
                        node_loc[n]['y'] = j
                        node_loc[n]['z'] = k
                        n += 1


    if globalvars.topology == 1: #Gaussian Perturbation Lattice
        n = 0
        side = int((globalvars.number_of_nodes+1)**(1.0/3))
        print(globalvars.number_of_nodes)
        print(side)

        #gaussian noise
        mu = 0
        sigma = 0.9
        noise = np.random.normal(mu, sigma, [globalvars.number_of_nodes])
        while n < globalvars.number_of_nodes:
            for i in range(1,side+1):
                for j in range(1,side+1):
                    for k in range(1,side+1):
                        node_loc[n]['x'] = i + noise[n]
                        node_loc[n]['y'] = j + noise[n]
                        node_loc[n]['z'] = k + noise[n]
                        n += 1


    # Generate a dict of positions
    position = {i: (node_loc[i]['x'], node_loc[i]['y'], node_loc[i]['z']) for i in range(n_nodes)}
    
    # Create random 3D network
    globalvars.G = nx.Graph()
    globalvars.G = nx.random_geometric_graph(n_nodes, radius, pos=position)
 
   # print("default edges")
   # print(globalvars.G.edges())
    globalvars.pos = nx.get_node_attributes(globalvars.G, 'pos')
    counter = 0
    if globalvars.adjlist == "generate":
        for u, v in combinations(globalvars.G, 2):
            #fully connected
            #globalvars.G.add_edge(u, v)

           # #sparsely connected
             dist = distance_between_nodes(u,v,node_loc)
           #  if dist == 1:#sparsely connected
           #     globalvars.G.add_edge(u, v)

             
            #probabilistic disk model
         #    if dist < 0.2: #if distance is less than 10 feet
         #        print("distance=",dist,"nodes",u,v,"are too close; adjusting positions")
         #        #to_del.append(u)
         #        #to_del.append(v)
         #        z_v = avoid_collision(u,v,node_loc)
         #        #update position of v
         #        
         #        index = int(v)
         #        posi = list(globalvars.pos[v])
         #        posi[2] = z_v
         #        globalvars.pos[v] = tuple(posi)
         #        
         #        #also update node_loc
         #        node_loc[v]['z'] = z_v
         #        #distance is 10 feet
         #        globalvars.G.add_edge(u, v)
         #        counter += 1
         #        continue
             if dist >= 2: 
                 pass
             elif dist < 0.2: #if distance is less than 20 feet = 20/25; 1 = 25 feet
                 globalvars.G.add_edge(u, v)
                 counter += 1
             else:
                 p = 1 - ((dist - 0.2)/1.8)
                 q = random.uniform(0,1)
                 if q <= p:
                     globalvars.G.add_edge(u, v)
                     counter += 1
        name = "graph_%d.pickle" % (globalvars.iteration)

        pickle.dump(globalvars.G, open(name,'wb'))
        print("counter=",counter)



    if globalvars.adjlist != "generate":
        globalvars.G = pickle.load(open(sys.argv[10], 'rb'))
        globalvars.pos = nx.get_node_attributes(globalvars.G, 'pos')
        #this will also rewrite the positions
        #globalvars.G = pickle.load(open('graph.pickle', 'rb'))

       # file = open('network_1.txt', 'r')
       # lines = []
       # lines = file.readlines()

       # for index, line in enumerate(lines):
       #     edgelist = []
       #     process_each_line(line.strip(),edgelist)
       #     for i in range(1,len(edgelist)):
       #         globalvars.G.add_edge(edgelist[0], edgelist[i])
       #         print("adding edge",edgelist[0], edgelist[i])

       #     del(edgelist) #added this because of memory leak; edgelist had older numbers than the ones read from file
       # file.close()

      #  print("AFTER READING FILE")
      #  for n, nbrdict in globalvars.G.adjacency():
      #      print((n,nbrdict))	
	
	

    
    #globalvars.G.remove_nodes_from(to_del)

#Temporary code for sanity check
  #  found = 0
  #  for u, v in combinations(globalvars.G, 2):
  #      dist = distance_between_nodes(u,v,node_loc)
  #      if dist < 0.4:
  #          print("Distance between",u,v,"is less than 0.4; check code")
  #          found = 1
  #  
  #  if found == 0:
  #      print("Distance sanity check passed")
  #     
        
        
    #print("removed nodes = ",to_del)
    print("NUMBER OF NODES = ",len(globalvars.G.nodes))
    globalvars.number_of_nodes = globalvars.G.number_of_nodes()
    print("NUMBER OF NODES = ",len(globalvars.G.nodes))
    
    print("Position of all nodes after: ",globalvars.pos) 

    return globalvars.G

def find_network_density():
    '''Graph Density | Baeldung on Computer Science
Graph density represents the ratio between the edges present in a graph and the maximum number of edges that the graph can contain. Conceptually, it provides an idea of how dense a graph is in terms of edge connectivity.'''


    max_edges = globalvars.number_of_nodes*(globalvars.number_of_nodes-1)/2
    number_of_edges = globalvars.G.number_of_edges()
    print("Density = ", number_of_edges/max_edges)
    print("number of edges = ", number_of_edges)


def network_plot_3D(G, angle, save):

    # Get node positions
    globalvars.pos = nx.get_node_attributes(G, 'pos')
    print("Position of all nodes: ",globalvars.pos) 
    # Get number of nodes
    n = G.number_of_nodes()
    # Get the maximum number of edges adjacent to a single node
    #edge_max = max([G.degree(i) for i in range(n)])

    # Define color range proportional to number of edges adjacent to a single node
 #   colors = [plt.cm.plasma(G.degree(i)/edge_max) for i in range(n)] 

    # 3D network plot
    with plt.style.context(('ggplot')):
        
        fig = plt.figure(figsize=(10,7))
        ax = Axes3D(fig)
        
        # Loop on the pos dictionary to extract the x,y,z coordinates of each node
        for key, value in globalvars.pos.items():
            xi = value[0]
            yi = value[1]
            zi = value[2]
            
            # Scatter plot
            ax.scatter(xi, yi, zi, s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
            #ax.scatter(xi, yi, zi, c=colors[key], s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
        
        # Loop on the list of edges to get the x,y,z, coordinates of the connected nodes
        # Those two points are the extrema of the line to be plotted
        for i,j in enumerate(G.edges()):

            x = np.array((globalvars.pos[j[0]][0], globalvars.pos[j[1]][0]))
            y = np.array((globalvars.pos[j[0]][1], globalvars.pos[j[1]][1]))
            z = np.array((globalvars.pos[j[0]][2], globalvars.pos[j[1]][2]))
        
        # Plot the connecting lines
            ax.plot(x, y, z, c='black', alpha=0.5)
    
    # Set the initial view
    ax.view_init(30, angle)

    # Hide the axes
    ax.set_axis_off()

  #   if save is not False:
  #       plt.savefig("./net".png")
  #       plt.close('all')
  #   else:
  #       plt.show()
    #plt.show()
   # plt.clf()
    
    return

def data_for_cylinder_along_z(center_x,center_y,radius,height_z):
    z = np.linspace(0, height_z, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid=np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return x_grid,y_grid,z_grid

def plot_3D_cylinder(radius, height, elevation=0, resolution=100, color='r', x_center = 0, y_center = 0):
    
    #fig=plt.figure()
    #ax = Axes3D(fig, azim=30, elev=30)

    x = np.linspace(x_center-radius, x_center+radius, resolution)
    z = np.linspace(elevation, elevation+height, resolution)
    X, Z = np.meshgrid(x, z)

    Y = np.sqrt(radius**2 - (X - x_center)**2) + y_center # Pythagorean theorem

    ax.plot_surface(X, Y, Z, linewidth=0, color=color)
    ax.plot_surface(X, (2*y_center-Y), Z, linewidth=0, color=color)

    floor = Circle((x_center, y_center), radius, color=color)
    ax.add_patch(floor)
    art3d.pathpatch_2d_to_3d(floor, z=elevation, zdir="z")

    ceiling = Circle((x_center, y_center), radius, color=color)
    ax.add_patch(ceiling)
    art3d.pathpatch_2d_to_3d(ceiling, z=elevation+height, zdir="z")

    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')

   # plt.show()


def read_adjacency_list_from_file():
    from collections import defaultdict

    with open(sys.argv[10]) as f:
        lines = f.read().strip().split("\n")

    d = defaultdict(list)

    for line in lines:
        ls = line.split(" ")
        d[ls[0]] = ls[1:]

    print(d)
    sys.exit()
    


def create_drones_network():

    n = globalvars.number_of_nodes  
    G = generate_random_3Dgraph(n_nodes=n, radius=0.25, seed=1)
    # network_plot_3D(G,0, save=True)
    
    
    x_nodes = [globalvars.pos[key][0] for key in globalvars.pos.keys()]
    y_nodes = [globalvars.pos[key][1] for key in globalvars.pos.keys()]
    z_nodes = [globalvars.pos[key][2] for key in globalvars.pos.keys()]
    
    #assign node id to each coordinate
    globalvars.node = [{'nodeID':0, 'loc':(0,0,0), 'packet':0} for i in range(globalvars.number_of_nodes)]
    for i in range(globalvars.number_of_nodes):
        globalvars.node[i]['nodeID'] = i
        globalvars.node[i]['loc'] = (x_nodes[i],y_nodes[i],z_nodes[i])
        globalvars.node[i]['packet'] = 0
    print("NODES")
    print("----------------")
    #print(globalvars.node)

    
    #update number of nodes
    globalvars.number_of_nodes = len(G.nodes())
    #make adj list correct (both directions) 
    print("ADJACENCY LIST")
    print("----------------")

    original_stdout = sys.stdout
    name = "network_%d.txt" % (globalvars.iteration)
 
    with open(name,'a') as f:
        sys.stdout = f
        for line in generate_adjlist_with_all_edges(globalvars.G,' '):
            print(line)
    sys.stdout = original_stdout


def take_a_snapshot_of_network():
              #START:Take a snapshot, not printing all, only printing one
    xi = []
    yi = []
    zi = []
    xii = []
    yii = []
    zii = []
    xiii = []
    yiii = []
    ziii = []
    fig = plt.figure()
    for key, value in globalvars.pos.items():

        if key == globalvars.s or key == globalvars.d:
            xii.append(value[0])
            yii.append(value[1])
            zii.append(value[2])
            print("TEST: ",xii,yii,zii)
            print("TEST: ",globalvars.pos[globalvars.focus1_key][0],globalvars.pos[globalvars.focus1_key][0],globalvars.pos[globalvars.focus1_key][0])
            print(value, key)
            print(globalvars.focus1_key, globalvars.focus2_key)
            print(globalvars.s, globalvars.d)
     #   elif (value[0] == 1 and value[1] == 2 and value[2] == 2) or  (value[0] == 2 and value[1] == 2 and value[2] == 3) or  (value[0] == 2 and value[1] == 2 and value[2] == 1)  or  (value[0] == 2 and value[1] == 3 and value[2] == 2) or (value[0] == 3 and value[1] == 2 and value[2] == 2) or (value[0] == 2 and value[1] == 1 and value[2] == 2):
     #       xiii.append(value[0])
     #       yiii.append(value[1])
     #       ziii.append(value[2])
        else:       
            xi.append(value[0])
            yi.append(value[1])
            zi.append(value[2])
        

                            
    ax = plt.axes(projection='3d')
    ax.scatter(xi,yi,zi, color='black')
    ax.scatter(xii,yii,zii, color='red')
   # ax.scatter(xiii,yiii,ziii, color='blue')
    for i,j in enumerate(globalvars.G.edges()):

        x = np.array((globalvars.pos[j[0]][0], globalvars.pos[j[1]][0]))
        y = np.array((globalvars.pos[j[0]][1], globalvars.pos[j[1]][1]))
        z = np.array((globalvars.pos[j[0]][2], globalvars.pos[j[1]][2]))
    
    # Plot the connecting lines
        ax.plot(x, y, z, c='black', alpha=0.5)
   

   
#22d cylinder
  #  Xc,Yc,Zc = data_for_cylinder_along_z(2,2,1,3)
   # ax.plot_surface(Xc, Yc, Zc, alpha=0.5)

    #plt.show()


  #  #3d cylinder
  #  from matplotlib.patches import Circle
  #  import mpl_toolkits.mplot3d.art3d as art3d
  #  radius = 1
  #  height = 3
  #  elevation = 5
  #  resolution = 100
  #  color = 'r'
  #  x_center = 2
  #  y_center = 2
  #  x = np.linspace(x_center-radius, x_center+radius, resolution)
  #  z = np.linspace(elevation, elevation+height, resolution)
  #  X, Z = np.meshgrid(x, z)

  #  Y = np.sqrt(radius**2 - (X - x_center)**2) + y_center # Pythagorean theorem

  #  ax.plot_surface(X, Y, Z, linewidth=0, color=color)
  #  ax.plot_surface(X, (2*y_center-Y), Z, linewidth=0, color=color)

  #  floor = Circle((x_center, y_center), radius, color=color)
  #  ax.add_patch(floor)
  #  art3d.pathpatch_2d_to_3d(floor, z=elevation, zdir="z")

  #  ceiling = Circle((x_center, y_center), radius, color=color)
  #  ax.add_patch(ceiling)
  #  art3d.pathpatch_2d_to_3d(ceiling, z=elevation+height, zdir="z")
    
    figname = "snap_network%d.png" % (globalvars.iteration)
 
    plt.savefig(figname)
    plt.close('all')

   #END: Take a snapshot, not printing all, only printing one

def find_points_inside_ellipsoid():
    for i in range(0,globalvars.number_of_nodes):
        inside = insideOrNot(globalvars.node[i]['loc'])
        if inside == 1:
            globalvars.insidectr += 1
    print("Total points inside the ellipsoid: ",globalvars.insidectr)


