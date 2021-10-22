#!/bin/bash


echo "Choose what algorithm"
echo "1. Petal Routing"
echo "2. Flooding"
c=1
while [ "$c" -le "10" ]
do
   echo "RUN $c"
   python3 simulator_drone.py >out$c

   c=$(( c+1 ))
done
