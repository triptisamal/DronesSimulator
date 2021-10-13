#find if a point is inside an ellipsoid
import plotly.graph_objects as go
import networkx as nx
import random
import math
import globalvars
import pylab


from itertools import combinations
import matplotlib.pyplot as plt
import math


def insideOrNot(locationstr):

    #string processing to extract the exact x,y,z coordinates
    arr = locationstr.split(', ')
    x = float(arr[0])
    y = float(arr[1])
    z = float(arr[2])

    #eq of the ellipsoid centered at (h,k,f)

    h= (globalvars.pos[globalvars.focus1_key][0]+globalvars.pos[globalvars.focus2_key][0])/2
    k= (globalvars.pos[globalvars.focus1_key][1]+globalvars.pos[globalvars.focus2_key][1])/2
    f= (globalvars.pos[globalvars.focus1_key][2]+globalvars.pos[globalvars.focus2_key][2])/2
    sol = (x-h)*(x-h)/(globalvars.a*globalvars.a) + (y-k)*(y-k)/(globalvars.b*globalvars.b) + (x-f)*(x-f)/(globalvars.c*globalvars.c)
    #semi axes are of lengths a, b, c

    if sol <= 1:
        return 1 #inside
    else:
        return 0

def initiate_petal_parameters():

    print("PETAL PARAMETERS")
    print("----------------")
    globalvars.focus1_key = random.choice(range(len(globalvars.pos)))
    while True:
        globalvars.focus2_key = random.choice(range(len(globalvars.pos)))
        if globalvars.focus1_key != globalvars.focus2_key:
            break
    
    print("Coordinates of focus 1 (source): (", globalvars.pos[globalvars.focus1_key][0],",", globalvars.pos[globalvars.focus1_key][1],",", globalvars.pos[globalvars.focus1_key][2],")" )
    print("Coordinates of focus 2 (destination): (", globalvars.pos[globalvars.focus2_key][0],",", globalvars.pos[globalvars.focus2_key][1],",", globalvars.pos[globalvars.focus2_key][2],")" )
    globalvars.packet['sLoc'] = (globalvars.pos[globalvars.focus1_key][0], globalvars.pos[globalvars.focus1_key][1], globalvars.pos[globalvars.focus1_key][2])
    globalvars.packet['dLoc'] = (globalvars.pos[globalvars.focus2_key][0], globalvars.pos[globalvars.focus2_key][1], globalvars.pos[globalvars.focus2_key][2])

    ff = (globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0])*(globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0])+(globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1])*(globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1])+(globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2])*(globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2])
    focaldist = math.sqrt(ff)
    print("Distance between two foci =", focaldist)
    print("Centre of ellipsoid = (", (globalvars.pos[globalvars.focus1_key][0]+globalvars.pos[globalvars.focus2_key][0])/2,",",(globalvars.pos[globalvars.focus1_key][1]+globalvars.pos[globalvars.focus2_key][1])/2,",",(globalvars.pos[globalvars.focus1_key][2]+globalvars.pos[globalvars.focus2_key][2])/2,")")

    print("Orbital eccentricity:",globalvars.e)
    #is that of the ellipse formed by a section containing both the longest and the shortest axes (one of which will be the polar axis (x axis))
    globalvars.a = focaldist/globalvars.e
    print("Semi major axis, a = ", globalvars.a)
    globalvars.b = globalvars.a * math.sqrt(1-globalvars.e*globalvars.e)
    print("Semi minor axis, b = ", globalvars.b)
    globalvars.c = random.uniform(globalvars.b,1)
    print("c = ",globalvars.c)



def generate_adjlist_with_all_edges(G,delimiter):
    for s, nbrs in G.adjacency():
        line = str(s) + delimiter
        for t, data in nbrs.items():
            line += str(t) + delimiter
        yield line[: -len(delimiter)]

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


def create_drones_network():


    n = globalvars.number_of_nodes  
    m = 0  #  edges
    seed = 20160  # seed random number generators for reproducibility

    # Use seed for reproducibility
    globalvars.G = nx.gnm_random_graph(n, m, seed=seed)
    globalvars.pos = nx.random_layout(globalvars.G,seed=seed,dim=3)
    x_nodes = [globalvars.pos[key][0] for key in globalvars.pos.keys()]
    y_nodes = [globalvars.pos[key][1] for key in globalvars.pos.keys()]
    z_nodes = [globalvars.pos[key][2] for key in globalvars.pos.keys()]
  

    #assign node id to each coordinate
    globalvars.node = [{'nodeID':0, 'loc':(0,0,0)} for i in range(globalvars.number_of_nodes)]
    for i in range(globalvars.number_of_nodes):
        globalvars.node[i]['nodeID'] = i
        globalvars.node[i]['loc'] = (x_nodes[i],y_nodes[i],z_nodes[i])
    print("NODES")
    print("----------------")
    #print(globalvars.node)


    #create links between nodes according to wireless network


    #Area of the drone area -- large enough to have many hops, also have sparse UAVs
    #network_height = 1000 feet
    #network_length = 1000 feet 
    #network_width = 1000 feet
    #wireless_range = 250-300 feet outside
    #since, points are generated inside cubic (1,1,1) distance
    #wireless range = 50/1000 - 75/1000
    #Minimum distance between the drones should be 10 feet,i.e., 10/1000=0.001

    #nodes -- 250 
    #range 90 - 250 feet
    

    to_del = []
    for u, v in combinations(globalvars.G, 2):
      dist = distance(u,v)
      if dist <= 0.001:
          print("distance=",dist," : nodes are too close, removing")
          to_del.append(u)
          to_del.append(v)
          continue
      if dist >= 0.25:
          pass
      elif dist < 0.09:
          globalvars.G.add_edge(u, v)
      else:
          p = 1 - ((dist - 0.09)/0.16)
          q = random.uniform(0,1)
          if q <= p:
              globalvars.G.add_edge(u, v)
    globalvars.G.remove_nodes_from(to_del) 
   
    #update number of nodes
    globalvars.number_of_nodes = len(globalvars.G.nodes())
    #make adj list correct (both directions) 
    print("ADJACENCY LIST")
    print("----------------")

    #for line in generate_adjlist_with_all_edges(globalvars.G,' '):
    #    print(line)
    
    #plot the figure
    pylab.figure(1,figsize=(10,10))
    options = {
    "node_color": "blue",
    "node_size": 30,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.6,
    }

    #nx.draw(globalvars.G, cmap = plt.get_cmap('ocean'),**options)
    #plt.show()
