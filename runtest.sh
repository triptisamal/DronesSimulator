#!/bin/sh


echo "Choose what algorithm (1/2)"
echo "1. Petal Routing"
echo "2. Flooding"
read testnumber
c=1
if [ "$testnumber" -eq "1" ]
then
	while [ "$c" -le "20" ]
	do
		echo "RUN $c"
   		#python3 simulator_drone.py >out$c
   		python3 simulator_drone.py
		c=$(( c+1 ))
	done
fi 
