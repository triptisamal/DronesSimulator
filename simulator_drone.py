from collections import deque
from copy import deepcopy
from petal import *
import globalvars
import re
import sys

def update_packet(loc):
    '''This method is for creating a packet. It is called by each source node'''
    globalvars.packet['tLoc'] = loc
    globalvars.packet['myLoc'] = loc



def create_event(eventid,nodeid,timeofevent,packetdetails):
    event = {'event_id':"DEFAULT", 'node':0,'time':0, 'details':"Packet details"}
    event['event_id'] = eventid
    event['node'] = nodeid
    event['time'] = timeofevent
    event['details'] = packetdetails

    return event


def node_handler(node_id, action,e):
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
    

    if action == "INITIATE_TRANSMISSION":
        #This is the first node, src
        print("Source ",node_id," is creating the packet, ", globalvars.packet['pID']," at",globalvars.now, "seconds." )
        update_packet(loc)
        #pid is incremented the only after a source creates a packet
        #in the next round of petal routing, this new pid will be used
        globalvars.pid += 1
        event_id = "BROADCAST_%03d" % (globalvars.idn)
        globalvars.idn += 1

        e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
        globalvars.event_queue.append(deepcopy(e))

        #sort queue according to the simulated real time (time of event happening)
        globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])


        #Update state vector of the source
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
                globalvars.state_vector[i]['pid'] = globalvars.packet['pID']
                globalvars.state_vector[i]['packet_seen'] = 1
                globalvars.state_vector[i]['transmitted'] = 1 #source is transmittn=ing
                globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
                break
        
        #Read adjacency list and create receive events
        for s, nbrs in globalvars.G.adjacency():
            if s == node_id:
                for t, data in nbrs.items():
                    globalvars.copies_transmitted += 1
                    event_id = "RECEIVE_%03d" % (globalvars.idn)
                    globalvars.idn += 1
                    
                    receiverloc = (0,0,0)
                    #find the location of the node corresponding that is receiving this packet
                    for i in range(globalvars.number_of_nodes):
                        if globalvars.node[i]['nodeID'] == t:
                            receiverloc = globalvars.node[i]['loc']
                            break
                    update_packet(receiverloc)
                    dist = distance(s, t)
                    #convert distance to m
                    dist = 0.3048*dist
                    propagation_delay = dist/globalvars.speed
                    time = globalvars.transmission_delay + propagation_delay 
                    globalvars.now = globalvars.now + time

                    e = create_event(event_id,t,globalvars.now,globalvars.packet)
                    globalvars.event_queue.append(deepcopy(e))
                    globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])

    

    if action == "START_BACKOFF":

        #check if the node is inside petal or not
        inside = insideOrNot(e['details']['myLoc'])
        if inside == 1:
            globalvars.node[node_id]['packet'] += 1
            #it is inside the petal
            print("it is inside petal")

            ##backoff timer start 
            bofftime = calculate_backoff(e['details']['myLoc'])
            print("Back off time =",bofftime, "seconds")
            globalvars.now = globalvars.now + bofftime
            event_id = "BACKOFFTIMEREXPIRY_%03d" % (globalvars.idn)
            globalvars.idn += 1

            e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
            globalvars.event_queue.append(deepcopy(e))
            globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])

        else:
            print("it is outside petal")



    if action == "INITIATE_BROADCAST":

        print("checking for broadcast")
        print("node id is ",node_id)
        print("state is:")
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
                print("PID: ",globalvars.state_vector[i]['pid'])
                print("packet seen? ",globalvars.state_vector[i]['packet_seen'])
                print("transmitted? ",globalvars.state_vector[i]['transmitted'])
                print("receive_count: ",globalvars.state_vector[i]['receive_count'])
                print("time of state update: ",globalvars.state_vector[i]['time_of_state_update'])


        #check the receive count
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
                if globalvars.state_vector[i]['transmitted'] == 0: #transmission is pending
                    if globalvars.protocol == 1:
                        #if petal protocol
                        if globalvars.state_vector[i]['receive_count'] <= 2:
                            globalvars.state_vector[i]['transmitted'] = 1 #it should be transmitted
                            globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
                            
                            print("Initializing broadcast")
                            globalvars.broadcast += 1
                            event_id = "BROADCAST_%03d" % (globalvars.idn)
                            globalvars.idn += 1
                            e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
                            globalvars.event_queue.append(deepcopy(e))
                            globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])
                        else:
                            print("receive count is ",globalvars.state_vector[i]['receive_count'])
                    if globalvars.protocol == 0:
                        #if flooding
                        globalvars.state_vector[i]['transmitted'] = 1 #it should be transmitted
                        globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
        
                        print("Initializing broadcast")
                        globalvars.broadcast += 1
                        event_id = "BROADCAST_%03d" % (globalvars.idn)
                        globalvars.idn += 1
                        e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
                        globalvars.event_queue.append(deepcopy(e))
                        globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])
                break


    if action == "INITIATE_RECEIVE":
        ##Look for all neighboring nodes and add events for receive
        #Read adjacency list and create receive events
        for s, nbrs in globalvars.G.adjacency():
            if s == node_id:
                for t, data in nbrs.items():
                    event_id = "RECEIVE_%03d" % (globalvars.idn)
                    globalvars.idn += 1
                    
                    receiverloc = (0,0,0)
                    #find the location of the node corresponding that is receiving this packet
                    for i in range(globalvars.number_of_nodes):
                        if globalvars.node[i]['nodeID'] == t:
                            receiverloc = globalvars.node[i]['loc']
                            break
                    update_packet(receiverloc)
                    dist = distance(s, t)
                    print("DISTANCE = ", dist)
                    #convert distance to m
                    dist = 0.3048*dist
                    propagation_delay = dist/globalvars.speed
                    time = globalvars.transmission_delay + propagation_delay 
                    globalvars.now = globalvars.now + time
                    e = create_event(event_id,t,globalvars.now,globalvars.packet)
                    globalvars.event_queue.append(deepcopy(e))
                    globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])




def process_event(e):
    '''Checks what type of event is extracted, and what node initiated it
    Call node_handler for that node'''


    if "RECEIVE" in e['event_id']:
        print("it is a receive event")
        
        initiate_backoff_or_broadcast = 0
        
        ##it is receive event, so add a future broadcast event
        ##whoever received will create the broadcast event
        
        ## find the node id of the node where the receive happened (the same will broadcast if inside petal)
        node_id = e['node']


        #Check if already transmitted
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
                if globalvars.state_vector[i]['transmitted'] == 1: #transmission already done once
                    print("Already transmitted this packet once")
                    break
                else:
                    initiate_backoff_or_broadcast = 1
                    break

        if initiate_backoff_or_broadcast == 1:
            initiate_backoff_or_broadcast = 0
            #update state vector of the pid at receiver
            globalvars.state_vector[i]['pid'] = globalvars.packet['pID']
            globalvars.state_vector[i]['packet_seen'] = 1
            globalvars.state_vector[i]['transmitted'] = 0 #transmission is pending
            globalvars.state_vector[i]['receive_count'] += 1
            globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
            #print state
            for i in range(globalvars.number_of_nodes):
                if globalvars.state_vector[i]['node_id'] == node_id:
                    print("node id: ",globalvars.state_vector[i]['node_id'])
                    print("PID: ",globalvars.state_vector[i]['pid'])
                    print("packet seen? ",globalvars.state_vector[i]['packet_seen'])
                    print("transmitted? ",globalvars.state_vector[i]['transmitted'])
                    print("receive_count: ",globalvars.state_vector[i]['receive_count'])
                    print("time of state update: ",globalvars.state_vector[i]['time_of_state_update'])


            #find destination id
            for j in range(globalvars.number_of_nodes):
                if globalvars.node[j]['loc'] == globalvars.packet['dLoc']:
                    dest_id = globalvars.node[j]['nodeID']
                    break
            #start back off timer for future broadcast only if the receiver is not destination
            #if node_id != dest_id and globalvars.node[node_id]['packet'] == 0:
            if node_id != dest_id:
                if globalvars.protocol == 1:
                    node_handler(node_id,"START_BACKOFF",e)
                if globalvars.protocol == 0:
                    #if it is flooding, then directly broadcast
                    node_handler(node_id,"INITIATE_BROADCAST",e)
            else:
                print("THE PACKET REACHED DESTINATION")
                globalvars.copies_delivered += 1
               # for i in range(globalvars.number_of_nodes):
               #     if globalvars.state_vector[i]['node_id'] == node_id:
               #         if globalvars.state_vector[i]['receive_count'] == 1:
               #             print("THE PACKET REACHED DESTINATION")
               #             break
               #         else:
               #             print("DESTINATION HAS RECEIVED THE PACKET ALREADY")
               #             break



    if "BROADCAST" in e['event_id']:
        print("it is a broadcast event")
        
        node_id = e['node']
        print(node_id)
        node_handler(node_id,"INITIATE_RECEIVE",e)

    
    if "BACKOFF" in e['event_id']:
        print("it is a back off timer expiry event")
        node_id = e['node']
        node_handler(node_id,"INITIATE_BROADCAST",e)
         

def main():
    
    '''Simulation engine'''
    
    #parse arguments
    if len(sys.argv) < 2:
        print("Usage: simulator_drone.py <protocol number>")
        print("Flooding: 0")
        print("Petal: 1")
        sys.exit();
    
    globalvars.init()
    create_drones_network()
    initiate_petal_parameters()
   
    globalvars.protocol = int(sys.argv[1])

    print("EVENTS")
    print("-------")
    globalvars.event_queue = deque()
   

    #find the node ID of src and send to node handler
    src = 0
    for i in range(globalvars.number_of_nodes):
        if globalvars.node[i]['loc'] == (globalvars.pos[globalvars.focus1_key][0], globalvars.pos[globalvars.focus1_key][1], globalvars.pos[globalvars.focus1_key][2]):
            src = globalvars.node[i]['nodeID'] = i
            print("Source node ID: ",src)
            break
    for i in range(globalvars.number_of_nodes):
        if globalvars.node[i]['loc'] == (globalvars.pos[globalvars.focus2_key][0], globalvars.pos[globalvars.focus2_key][1], globalvars.pos[globalvars.focus2_key][2]):
            des = globalvars.node[i]['nodeID'] = i
            print("Destination node ID: ",des)
            break
    
    #define data structure for state for the packet id for each node
    globalvars.state_vector = [{'pid':0, 'node_id':i, 'packet_seen':0,'transmitted':0,'receive_count':0,'time_of_update':0} for i in range(globalvars.number_of_nodes)]

    node_handler(src,"INITIATE_TRANSMISSION",0)
    print("\nEVENT QUEUE:\n")
    print("-----------------")
    print(*globalvars.event_queue,sep="\n")
    
    while globalvars.event_queue:
        item = globalvars.event_queue.pop(0)
        print("\nEvent occuring: ",item)
        process_event(item)
        print("\nEVENT QUEUE:\n")
        print("-----------------")
        print(*globalvars.event_queue,sep="\n")

    print("Total number of broadcasts = ",globalvars.broadcast)
    if globalvars.copies_delivered > 0:
        print("Copy Delivery Ratio = ",globalvars.copies_transmitted/globalvars.copies_delivered)
    else:
        print("copies transmitted by source = ",globalvars.copies_transmitted, "copies delivered at dest =", globalvars.copies_delivered)

    original_stdout = sys.stdout
    if globalvars.protocol == 1:
        with open('bcast','a') as f:
            sys.stdout = f
            print(globalvars.broadcast)
            if globalvars.copies_delivered > 0:
                print(globalvars.copies_transmitted/globalvars.copies_delivered)
            else:
                print("copies transmitted by source = ",globalvars.copies_transmitted, "copies delivered at dest =", globalvars.copies_delivered)
            print("Density of the network = ", 1000000/((globalvars.number_of_nodes*4*3.14*(25)**3)/3))
            print("Number of nodes in the network = ", globalvars.number_of_nodes)


    if globalvars.protocol == 0:
        with open('flood','a') as f:
            sys.stdout = f
            print(globalvars.broadcast)
            if globalvars.copies_delivered > 0:
                print(globalvars.copies_transmitted/globalvars.copies_delivered)
            else:
                print("copies transmitted by source = ",globalvars.copies_transmitted, "copies delivered at dest =", globalvars.copies_delivered)
            print("Density of the network = ", 1000000/((globalvars.number_of_nodes*4*3.14*(25)**3)/3))
            print("Number of nodes in the network = ", globalvars.number_of_nodes)


    sys.stdout = original_stdout


if __name__=="__main__":
    main()
