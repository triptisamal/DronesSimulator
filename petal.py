#find if a point is inside an ellipsoid
import plotly.graph_objects as go
import networkx as nx
import random
import math
import globalvars
import pylab

#def insideOrNot(x,y,z):
#    global focus1_key
#    global focus2_key
#    global a
#    global b
#    global c
#    global pos
#    #eq of the ellipsoid centered at (h,k,f)
#
#    h= (pos[focus1_key][0]+pos[focus2_key][0])/2
#    k= (pos[focus1_key][1]+pos[focus2_key][1])/2
#    f= (pos[focus1_key][2]+pos[focus2_key][2])/2
#    sol = (x-h)*(x-h)/(a*a) + (y-k)*(y-k)/(b*b) + (x-f)*(x-f)/(c*c)
#    #semi axes are of lengths a, b, c
#    return sol
from itertools import combinations
import matplotlib.pyplot as plt
import math

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
    G = nx.gnm_random_graph(n, m, seed=seed)

    ##Add edges by radio frequency


    ##ratio 
    ##drone diameter 1 metre, must not come any closer than 10 feet.
    ## if they do come closer than 10 feet, they disrupt each other so much that they fall out of the sky



    ## Try other graphs too
    ## eg. 3D Poisson probabilty graph
    ##Perturbed mesh model
            #take rectagular mesh
            #petrub x y z by some probability
            #you get a deformed retangular mesh
    
    
   # edges = G.edges()
    
   # print("the adjacency list")
   # for line in nx.generate_adjlist(G):
   #     print(line)
    globalvars.pos = nx.random_layout(G,seed=seed,dim=3)
    #globalvars.pos = nx.spring_layout(G, seed=seed,dim=3,k=1,scale=10)  # Seed for reproducible layout
    x_nodes = [globalvars.pos[key][0] for key in globalvars.pos.keys()]
    y_nodes = [globalvars.pos[key][1] for key in globalvars.pos.keys()]
    z_nodes = [globalvars.pos[key][2] for key in globalvars.pos.keys()]
  

    #assign node id to each coordinate
    globalvars.node = [{'nodeID':0, 'loc':(0,0,0)} for i in range(globalvars.number_of_nodes)]
    for i in range(globalvars.number_of_nodes):
        globalvars.node[i]['nodeID'] = i
        globalvars.node[i]['loc'] = (x_nodes[i],y_nodes[i],z_nodes[i])
    print(globalvars.node)




    #create links between nodes according to wireless network


    #Area of the drone area -- large enough to have many hops, also have sparse UAVs
    #typical wireless range ~ 200-250 feet 
    # 
    #network_height = 1000 feet
    #network_length = 1000 feet 
    #network_width = 1000 feet
    #wireless_range = 250-300 feet outside
    #since, points are generated inside cubic (1,1,1) distance
    #wireless range = 250/1000 - 300/1000
    #Minimum distance between the drones should be 10 feet,i.e., 10/1000=0.001
    

    for u, v in combinations(G, 2):
      dist=distance(u,v)
      if dist <=0.001:
          print("distance=",dist)
      if dist >= 0.3:
          pass
      elif dist < 0.25:
          G.add_edge(u, v)
      else:
          p = 1 - ((dist - 0.25)/0.05)
          q = random.uniform(0,1)
          if q <= p:
              G.add_edge(u, v)
    
    #make adj list correct (both directions) TODO 
    print("the adjacency list")
    for line in nx.generate_adjlist(G):
        print(line)
   # A = nx.adjacency_matrix(G)
   # print(A)
    pylab.figure(1,figsize=(10,10))
    nx.draw(G, cmap = plt.get_cmap('ocean'))
    plt.show()
   # #we need to create lists that contain the starting and ending coordinates of each edge.
   # x_edges=[]
   # y_edges=[]
   # z_edges=[]
   # 
   # #need to fill these with all of the coordinates
   # for edge in edges:
   #     #format: [beginning,ending,None]
   #     x_coords = [globalvars.pos[edge[0]][0],globalvars.pos[edge[1]][0],None]
   #     x_edges += x_coords
   # 
   #     y_coords = [globalvars.pos[edge[0]][1],globalvars.pos[edge[1]][1],None]
   #     y_edges += y_coords
   # 
   #     z_coords = [globalvars.pos[edge[0]][2],globalvars.pos[edge[1]][2],None]
   #     z_edges += z_coords
   # 
   # #create a trace for the edges
   # trace_edges = go.Scatter3d(
   #     x=x_edges,
   #     y=y_edges,
   #     z=z_edges,
   #     mode='lines',
   #     line=dict(color='black', width=2),
   #     hoverinfo='none')
   # 
   # #create a trace for the nodes
   # trace_nodes = go.Scatter3d(
   #     x=x_nodes,
   #     y=y_nodes,
   #     z=z_nodes,
   #     mode='markers',
   #     marker=dict(symbol='circle',
   #             size=10,
   #             color='skyblue')
   #     )
   # 
   # #Include the traces we want to plot and create a figure
   # data = [trace_edges, trace_nodes]
   # fig = go.Figure(data=data)
   # fig.show()


