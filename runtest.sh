#!/bin/sh


echo "Choose what test scenario (1/0)"
echo "0. Effect of increase in number of nodes"
echo "1. Effect of increase in eccentricity"
echo "2. Check delay related"
read testnumber


echo "Choose what algorithm (1/0)"
echo "0. Flooding"
echo "1. Petal Routing"
read algorithm

echo "Choose what topology (1/0)"
echo "0. Lattice"
echo "1. Guassian Perturbed Lattice"
read topology

#echo "Choose what zone (1/0)"
#echo "0. Single"
#echo "1. Multi"
#read zone
echo "Choose what mobility model (2/1/0)"
echo "0. No mobility"
echo "1. All nodes moving with same velocity"
echo "2. Some nodes moving with same velocity"
read mobility

if [ "$testnumber" -eq "2" ]
then
	c=37
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 64 0.7 $topology 1 $mobility $c 
		c=$(( c+1 ))
	done
fi



if [ "$testnumber" -eq "0" ]
then
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 64 0.9 $topology 0 $c 
	#	python3 simulator_drone.py $algorithm 64 0.4 $topology 1 
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.9 $topology 0 $c
	#	python3 simulator_drone.py $algorithm 125 0.4 $topology 1 
		c=$(( c+1 ))
	done
       c=1
       while [ "$c" -le "500" ]
       do
       	echo "RUN $c"
       	python3 simulator_drone.py $algorithm 216 0.9 $topology 0 $c 
       #	python3 simulator_drone.py $algorithm 216 0.4 $topology 1
       	c=$(( c+1 ))
       done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 343 0.9 $topology 0 $c
	#	python3 simulator_drone.py $algorithm 343 0.4 $topology 1
		c=$(( c+1 ))
	done
fi


if [ "$testnumber" -eq "1" ]
then
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		python3 simulator_drone.py $algorithm 125 0.4 $topology $zone 
#		c=$(( c+1 ))
#	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.5 $topology 0
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.6 $topology 0
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.7 $topology 0 
		c=$(( c+1 ))
	done
fi
