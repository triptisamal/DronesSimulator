#!/bin/sh


echo "Choose what algorithm (1/0)"
echo "0. Flooding"
echo "1. Petal Routing"
read testnumber
c=1
while [ "$c" -le "40" ]
do
	echo "RUN $c"
	#python3 simulator_drone.py >out$c
	python3 simulator_drone.py $testnumber
	c=$(( c+1 ))
done
