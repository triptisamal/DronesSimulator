import igraph as ig
import random
from collections import deque


##global data structures
packet = {
            'pID':0,    #packet ID
            'dLoc':(0,0,0),   #destination location
            'tLoc':(0,0,0),    #transmitter (intermediate node) location
            'sLoc':(0,0,0), #source location
            'myLoc':(0,0,0), #my location 
            
            #petal parameters 
            'eccentricity':0.5, #of the major axis plane (?)

            #back off time parameters
            'tUB1':0.002, #seconds;tB1 -> back-off time proportional to the distance from destination. 
                          #This is bounded above by tUb1.
            'tUB2':0.0005, #seconds;tB2 -> back-off time proportional to the distance from the source-destination 
                           #line. This is bounded above by tUb2.


            #SINGLE zone means petal does not change
            'zoneType':"SINGLE"

        }#message

def add_event(event):
    '''This method is called by the simulation engine to create events and add to event queue'''
    print(packet)




def wireless_handler():
    '''This deals with the range of transmission while broadcast
    
       Input(s): wireless range, position of nodes
       
       '''

def node_handler():
    '''This handles everything that a node is supposed to do:
        1. Find if it is inside a petal
        2. Calculate the back off time
        3. Adds future events that should be triggered from an action
        4. Deletes future events, if encounters a transmission from another node that is closer to the source-destination line
        
        Input(s): Node ID (because this is a common handler for all nodes)
        NOTE: memory for each node will be separate, maintained by the simulator'''


def spawn_drones_graph():

    global coords_subgraph
    print("Creating drones network")

    ##TODO Read from file specifications for graph
    total_number_of_nodes = 5
    total_number_of_edges = 5

    ##create fully connected graph 
    g = ig.Graph(n=total_number_of_nodes)
    adj = []
    adj = g.get_adjacency()
    print("Adjacency matrix": adj)
    ##assign location (coordinates)
    layout = g.layout(layout='auto',dim=3)
    coords_subgraph = layout[:total_number_of_nodes]

    drone_ids = []
    drone_ids = [0 for i in range(total_number_of_nodes)] 
    for i in range(len(coords_subgraph)):
        drone_ids[i] = i
        print("Drone ",drone_ids[i],": ",coords_subgraph[i])
    
    
    ##view graph
    ig.plot(g)


def main():
    
    '''Simulation engine'''
    create_drones_network()
    add_event("BROADCAST",src)

if __name__=="__main__":
    main()

