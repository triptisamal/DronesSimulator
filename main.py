import igraph as ig


def spawn_drones_graph():

    print("Spawing drones graph")
    ##create fully connected graph 
    g = ig.Graph.Full(n=20)

    ##assign location (coordinates)
    layout = g.layout(layout='auto')
    coords_subgraph = layout[:10]
    print(coords_subgraph)
    
    ##view graph
    ig.plot(g)


def initialize_petal_parameters():

    print("Initializing Petal Routing parameters")

def share_locations_with_all():

    print("Initializing Petal routing for sharing locations with all")

def main():

    spawn_drones_graph()
    initialize_petal_parameters()
    share_locations_with_all()

if __name__=="__main__":
    main()
