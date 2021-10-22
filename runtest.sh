#!/bin/bash

c=1
while [ "$c" -le "2" ]
do
   echo "RUN $c"
   python3 simulator_drone.py >out$i

   c=$(( c+1 ))
done
