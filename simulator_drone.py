from collections import deque
from petal import *
import globalvars

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
        #This is the first node, src
        print("Source ",node_id," is creating the packet")
        create_packet()
        event = "Packet %d created at %s at %d seconds" %(globalvars.packet['pID'],globalvars.packet['sLoc'],globalvars.now)
        globalvars.now = globalvars.now + globalvars.now_e
        ##TODO now_e will be calculated as propagation delay (dist/c) and other delays
        event = "Packet %d broadcast at %s at %d seconds" %(globalvars.packet['pID'],globalvars.packet['sLoc'],globalvars.now)
        print("Event ",event," getting added to the queue")
        globalvars.event_queue.append(event)
        #Read adjacency list and create receive events
        for s, nbrs in globalvars.G.adjacency():
            if s == node_id:
                for t, data in nbrs.items():
                    event = "Node %d received packet from node %d at %d seconds" %(t,node_id,globalvars.now)
                    print("Event ",event," getting added to the queue")
                    globalvars.event_queue.append(event)
            


        #Then broadcast
    if action == "FORWARDING_TX":
        #find if inside a petal
       print("") 
        



def main():
    
    '''Simulation engine'''
    
    globalvars.init()
    create_drones_network()
    initiate_petal_parameters()
   

    print("EVENTS")
    print("-------")
    globalvars.event_queue = deque()
   

    #find the node ID of src and send to node handler
    src = 0
    for i in range(globalvars.number_of_nodes):
        if globalvars.node[i]['loc'] == (globalvars.pos[globalvars.focus1_key][0], globalvars.pos[globalvars.focus1_key][1], globalvars.pos[globalvars.focus1_key][2]):
            src = globalvars.node[i]['nodeID'] = i
            break
    node_handler(src,"INITIATE_TX")
    print("EVENT QUEUE:\n")
    print(globalvars.event_queue)
    
    while globalvars.event_queue:
        item = globalvars.event_queue.popleft()
        print("Event occuring: ",str(item))
        #process event TODO
        #call node_handler() TODO
        print("EVENT QUEUE:\n")
        print(globalvars.event_queue)

if __name__=="__main__":
    main()

