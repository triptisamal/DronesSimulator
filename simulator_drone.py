from collections import deque
from copy import deepcopy
from petal import *
import globalvars
import re

import sys
def wireless_handler():
    '''This deals with the range of transmission while broadcast
    
       Input(s): wireless range, position of nodes
       
       '''
    print(globalvars.pos)


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



        #event = "EventID:%s, node:%d, time: %d, details: The packet is %s" %(event_id,node_id,globalvars.now,globalvars.packet)
        #globalvars.event_queue.append(event)
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
                    #convert distance to m
                    dist = 0.3048*dist
                    propagation_delay = dist/globalvars.speed
                    time = globalvars.transmission_delay + propagation_delay 
                    globalvars.now = globalvars.now + time

                    e = create_event(event_id,t,globalvars.now,globalvars.packet)
                    globalvars.event_queue.append(deepcopy(e))
                    globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])

                    #event = "EventID:%s, node:%s, time: %d, details: The packet is %s" %(event_id,t,globalvars.now,globalvars.packet)
                    #globalvars.now = globalvars.now + globalvars.now_e
                   # globalvars.event_queue.append(event)
                
    

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
                    if globalvars.state_vector[i]['receive_count'] <= 2:
                        globalvars.state_vector[i]['transmitted'] == 1 #it should be transmitted
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
        ##first find if it is inside petal
      #  _location = re.findall(r"'myLoc': (.*?), 'eccentricity'",e['details'][])
      #  location = re.findall(r"\((.*?)\)",_location[0])
      #  inside = insideOrNot(location[0])
#        inside = insideOrNot(e['details']['myLoc'])

#
#        if inside == 1:
#            globalvars.broadcast += 1
#            globalvars.node[node_id]['packet'] += 1
#            #it is inside the petal
#            print("it is inside petal")
#
#            ##backoff timer start TODO
#            #bofftime = calculate_backoff(location[0])
#            bofftime = calculate_backoff(e['details']['myLoc'])
#            print("Back off time =",bofftime, "seconds")
#            globalvars.now = globalvars.now + bofftime
#         #   event_id = "TIMEREXPIRY_%03d" % (globalvars.idn)
#         #   globalvars.idn += 1
#           # event = "EventID:%s, node:%d, time: %d, details: The packet is %s" %(event_id,node_id,globalvars.now,globalvars.packet)
#          #  globalvars.event_queue.append(event)
#
#         #   e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
#         #   globalvars.event_queue.append(deepcopy(e))
#         #   globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])
#
#            event_id = "BROADCAST_%03d" % (globalvars.idn)
#            globalvars.idn += 1
#            e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
#            globalvars.event_queue.append(deepcopy(e))
#            globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])
#            #event = "EventID:%s, node:%d, time: %d, details: The packet is %s" %(event_id,node_id,globalvars.now,globalvars.packet)
#            #globalvars.event_queue.append(event)
#        #    for i in range(globalvars.number_of_nodes):
#        #        if globalvars.state_vector[i]['node_id'] == node_id:
#        #            globalvars.state_vector[i]['pid'] = globalvars.packet['pID']
#        #            globalvars.state_vector[i]['packet_seen'] = 1
#        #            globalvars.state_vector[i]['transmitted'] = 0 #transmission is pending
#        #            globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
#        else:
#            print("it is outside petal; not broadcasting")
#        #    for i in range(globalvars.number_of_nodes):
#        #        if globalvars.state_vector[i]['node_id'] == node_id:
#        #            globalvars.state_vector[i]['pid'] = globalvars.packet['pID']
#        #            globalvars.state_vector[i]['packet_seen'] = 1
#        #            globalvars.state_vector[i]['transmitted'] = 0 #transmission is pending
#        #            globalvars.state_vector[i]['time_of_state_update'] = globalvars.now

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
                    #event = "EventID:%s, node:%s, time: %d, details: The packet is %s" %(event_id,t,globalvars.now,globalvars.packet)
                    #globalvars.event_queue.append(event)




def process_event(e):
    '''Checks what type of event is extracted, and what node initiated it
    Call node_handler for that node'''


    if "RECEIVE" in e['event_id']:
        print("it is a receive event")
        

        
        ##it is receive event, so add a future broadcast event
        ##example:
        ##EventID:RECEIVE_008, node:198, time: 1, details: The packet is {'pID': 0, 'dLoc': (0.57229507, 0.025313331, 0.18988311), 'tLoc': (0.17912914, 0.76912647, 0.88080639), 'sLoc': (0.26650634, 0.79798305, 0.8773067), 'myLoc': (0.17912914, 0.76912647, 0.88080639), 'eccentricity': 0.6, 'tUB1': 0.002, 'tUB2': 0.0005, 'zoneType': 'SINGLE'}
        ##Node 30 received packet <pid> from node 152 at 1 seconds
        ##whoever received will create the broadcast event
        
        ## find the node id of the node where the receive happened (the same will broadcast if inside petal)
       # node_idstr = re.findall(r"node:(.*?),",e)
       # node_id = int(node_idstr[0])
        node_id = e['node']
        #update state vector
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
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
        for i in range(globalvars.number_of_nodes):
            if globalvars.node[i]['loc'] == globalvars.packet['dLoc']:
                dest_id = globalvars.node[i]['nodeID']
                break
        #start back off timer for future broadcast only if the receiver is not destination
        #if node_id != dest_id and globalvars.node[node_id]['packet'] == 0:
        if node_id != dest_id:
            node_handler(node_id,"START_BACKOFF",e)
            #node_handler(node_id,"INITIATE_BROADCAST",e)
        else:
            print("THE PACKET REACHED DESTINATION")
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
        #EventID:BROADCAST_002, node:19, time: 1, details: The packet is {'pID': 0, 'dLoc': (0.3179515, 0.75904512, 0.032490466), 'tLoc': (0.036272522, 0.19901623, 0.51243943), 'sLoc': (0.033281673, 0.24830705, 0.4337596), 'myLoc': (0.036272522, 0.19901623, 0.51243943), 'eccentricity': 0.6, 'tUB1': 0.002, 'tUB2': 0.0005, 'zoneType': 'SINGLE'}
        
        ## find the node id of the node where the receive happened (the same will broadcast if inside petal)
       # node_idstr = re.findall(r"node:(.*?),",e)
       # node_id = int(node_idstr[0])
        
        node_id = e['node']
        print(node_id)
        node_handler(node_id,"INITIATE_RECEIVE",e)

    
    if "BACKOFF" in e['event_id']:
        print("it is a back off timer expiry event")
        node_id = e['node']
        node_handler(node_id,"INITIATE_BROADCAST",e)
         

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
        #item = globalvars.event_queue.popleft()
        #print("\nEvent occuring: ",str(item))
        print("\nEvent occuring: ",item)
        process_event(item)
        #process_event(str(item))
        print("\nEVENT QUEUE:\n")
        print("-----------------")
        print(*globalvars.event_queue,sep="\n")

    print("Total number of broadcasts = ",globalvars.broadcast)
if __name__=="__main__":
    main()

