from collections import deque
from petal import *
import globalvars

##global data structures
#pos = []
#e = 0.6
#focus1_key=0
#focus2_key=0
#a=0
#b=0
#c=0

packet = {
            'pID':0,    #packet ID
            'dLoc':(0,0,0),   #destination location
            'tLoc':(0,0,0),    #transmitter (intermediate node) location
            'sLoc':(0,0,0), #source location
            'myLoc':(0,0,0), #my location 
            
            #petal parameters 
            'eccentricity':0.6, #of the segment corresponding to orbital eccentricity 

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
    print(globalvars.pos)

def node_handler():
    '''This handles everything that a node is supposed to do:
        1. Find if it is inside a petal
        2. Calculate the back off time
        3. Adds future events that should be triggered from an action
        4. Deletes future events, if encounters a transmission from another node that is closer to the source-destination line
        
        Input(s): Node ID (because this is a common handler for all nodes)
        NOTE: memory for each node will be separate, maintained by the simulator'''





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
    add_event("BROADCAST")

if __name__=="__main__":
    main()

