from collections import deque
from petal import *
import globalvars

def add_event(event):
    '''This method is called by the simulation engine to create events and add to event queue'''

    print("Event ",event," getting added to the queue")
    print(globalvars.packet)




def wireless_handler():
    '''This deals with the range of transmission while broadcast
    
       Input(s): wireless range, position of nodes
       
       '''
    print(globalvars.pos)


def create_packet():
    '''This method is for creating a packet. It is called by each source node'''
    globalvars.packet['pID'] = globalvars.pid
    globalvars.pid += 1



def node_handler(node_id, action):
    '''This handles everything that a node is supposed to do:
        1. Find if it is inside a petal
        2. Calculate the back off time
        3. Adds future events that should be triggered from an action
        4. Deletes future events, if encounters a transmission from another node that is closer to the source-destination line
        
        Input(s): Node ID (because this is a common handler for all nodes)
        action: what the node is supposed to do at first
        NOTE: memory for each node will be separate, maintained by the simulator'''

    loc = (0,0,0)
    #find the location of the node corresponding to node_id
    for i in range(globalvars.number_of_nodes):
        if globalvars.node[i]['nodeID'] == node_id:
            loc = globalvars.node[i]['loc']

    if action == "INITIATE_TX":
        #This node is the source, so create packet first
       print("Source is creating the packet")
       create_packet()
       event = "Packet %d created at %s at %d seconds" %(globalvars.packet['pID'],globalvars.packet['sLoc'],globalvars.now)
    globalvars.event_queue.append(event)
    globalvars.now = globalvars.now + globalvars.now_e
    ##now_e will be calculated as propagation delay (dist/c)
    event = "Packet %d broadcast at %s at %d seconds" %(globalvars.packet['pID'],globalvars.packet['sLoc'],globalvars.now)
    globalvars.event_queue.append(event)


        #Then broadcast
    if action == "FORWARDING_TX":
        #find if inside a petal
       print("") 
        
    add_event("BROADCAST")



def main():
    
    '''Simulation engine'''
    
    globalvars.init()
    create_drones_network()
    globalvars.focus1_key = random.choice(range(len(globalvars.pos)))
    print(globalvars.focus1_key)
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

    globalvars.event_queue = deque()
   

    #find the node ID of src and send to node handler

    node_handler(2,"INITIATE_TX")
    print("EVENT QUEUE:\n")
    print(globalvars.event_queue)
    
    while globalvars.event_queue:
        item = globalvars.event_queue.popleft()
        print("Event occuring: ",str(item))
        print("EVENT QUEUE:\n")
        print(globalvars.event_queue)

if __name__=="__main__":
    main()

