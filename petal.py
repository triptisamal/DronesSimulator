#find if a point is inside an ellipsoid
import plotly.graph_objects as go
import networkx as nx
import random
import math
import globalvars

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




def create_drones_network():


    n = 30  # 10 nodes
    m = 50  # 20 edges
    seed = 20160  # seed random number generators for reproducibility

    # Use seed for reproducibility
    G = nx.gnm_random_graph(n, m, seed=seed)
    edges = G.edges()
    
    print("the adjacency list")
    for line in nx.generate_adjlist(G):
        print(line)

    globalvars.pos = nx.spring_layout(G, seed=seed,dim=3,k=1,scale=10)  # Seed for reproducible layout
    x_nodes = [globalvars.pos[key][0] for key in globalvars.pos.keys()]
    y_nodes = [globalvars.pos[key][1] for key in globalvars.pos.keys()]
    z_nodes = [globalvars.pos[key][2] for key in globalvars.pos.keys()]
    
    #we need to create lists that contain the starting and ending coordinates of each edge.
    x_edges=[]
    y_edges=[]
    z_edges=[]
    
    #need to fill these with all of the coordinates
    for edge in edges:
        #format: [beginning,ending,None]
        x_coords = [globalvars.pos[edge[0]][0],globalvars.pos[edge[1]][0],None]
        x_edges += x_coords
    
        y_coords = [globalvars.pos[edge[0]][1],globalvars.pos[edge[1]][1],None]
        y_edges += y_coords
    
        z_coords = [globalvars.pos[edge[0]][2],globalvars.pos[edge[1]][2],None]
        z_edges += z_coords
    
    #create a trace for the edges
    trace_edges = go.Scatter3d(
        x=x_edges,
        y=y_edges,
        z=z_edges,
        mode='lines',
        line=dict(color='black', width=2),
        hoverinfo='none')
    
    #create a trace for the nodes
    trace_nodes = go.Scatter3d(
        x=x_nodes,
        y=y_nodes,
        z=z_nodes,
        mode='markers',
        marker=dict(symbol='circle',
                size=10,
                color='skyblue')
        )
    
    #Include the traces we want to plot and create a figure
    data = [trace_edges, trace_nodes]
    fig = go.Figure(data=data)
    fig.show()


