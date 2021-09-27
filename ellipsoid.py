#find if a point is inside an ellipsoid
import plotly.graph_objects as go
import networkx as nx
import random
import math
pos = []
e = 0.6
focus1_key=0
focus2_key=0
a=0
b=0
c=0


def insideOrNot(x,y,z):
    global focus1_key
    global focus2_key
    global a
    global b
    global c
    #eq of the ellipsoid centered at (h,k,f)

    h= (pos[focus1_key][0]+pos[focus2_key][0])/2
    k= (pos[focus1_key][1]+pos[focus2_key][1])/2
    f= (pos[focus1_key][2]+pos[focus2_key][2])/2
    print(a)
    print(b)
    print(c)
    sol = (x-h)*(x-h)/(a*a) + (y-k)*(y-k)/(b*b) + (x-f)*(x-f)/(c*c)
    #semi axes are of lengths a, b, c
    return sol




def spawn_drones_graph():


    global pos


    n = 30  # 10 nodes
    m = 50  # 20 edges
    seed = 20160  # seed random number generators for reproducibility

    # Use seed for reproducibility
    G = nx.gnm_random_graph(n, m, seed=seed)
    edges = G.edges()
    
    print("the adjacency list")
    for line in nx.generate_adjlist(G):
        print(line)

    pos = nx.spring_layout(G, seed=seed,dim=3,k=1,scale=10)  # Seed for reproducible layout

    x_nodes = [pos[key][0] for key in pos.keys()]
    y_nodes = [pos[key][1] for key in pos.keys()]
    z_nodes = [pos[key][2] for key in pos.keys()]
    
    #we need to create lists that contain the starting and ending coordinates of each edge.
    x_edges=[]
    y_edges=[]
    z_edges=[]
    
    #need to fill these with all of the coordinates
    for edge in edges:
        #format: [beginning,ending,None]
        x_coords = [pos[edge[0]][0],pos[edge[1]][0],None]
        x_edges += x_coords
    
        y_coords = [pos[edge[0]][1],pos[edge[1]][1],None]
        y_edges += y_coords
    
        z_coords = [pos[edge[0]][2],pos[edge[1]][2],None]
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

def main():


    global focus1_key
    global focus2_key
    global a
    global b
    global c
    spawn_drones_graph()
    print(pos)
    focus1_key = random.choice(range(len(pos)))
    print(focus1_key)
    while True:
        focus2_key = random.choice(range(len(pos)))
        if focus1_key != focus2_key:
            break
    
    print(focus2_key)

    print("Coordinates of focus 1 (source): (", pos[focus1_key][0],",", pos[focus1_key][1],",", pos[focus1_key][2],")" )
    print("Coordinates of focus 2 (destination): (", pos[focus2_key][0],",", pos[focus2_key][1],",", pos[focus2_key][2],")" )


    ff = (pos[focus2_key][0]-pos[focus1_key][0])*(pos[focus2_key][0]-pos[focus1_key][0])+(pos[focus2_key][1]-pos[focus1_key][1])*(pos[focus2_key][1]-pos[focus1_key][1])+(pos[focus2_key][2]-pos[focus1_key][2])*(pos[focus2_key][2]-pos[focus1_key][2])
    focaldist = math.sqrt(ff)
    print("Distance between two foci =", focaldist)
    print("Centre of ellipsoid = (", (pos[focus1_key][0]+pos[focus2_key][0])/2,",",(pos[focus1_key][1]+pos[focus2_key][1])/2,",",(pos[focus1_key][2]+pos[focus2_key][2])/2,")")

    print("Meridional eccentricity:",e)
    #is that of the ellipse formed by a section containing both the longest and the shortest axes (one of which will be the polar axis (x axis))
    a = focaldist/e
    print("Semi major axis, a = ", a)
    b = a * math.sqrt(1-e*e)
    print("Semi minor axis, b = ", b)
    c = b-5
    print("c = ",c)

    

    ret = insideOrNot(1,2,3)

    if ret <= 1:
        print("Inside")
    else:
        print("Outside")

if __name__=="__main__":
    main()
