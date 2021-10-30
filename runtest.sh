#!/bin/sh


echo "Choose what test scenario (1/0)"
echo "0. Effect of increase in number of nodes"
echo "1. Effect of increase in eccentricity"
read testnumber


echo "Choose what algorithm (1/0)"
echo "0. Flooding"
echo "1. Petal Routing"
read algorithm



if [ "$testnumber" -eq "0" ]
then
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 64 0.4
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.4
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 216 0.4
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 343 0.4
		c=$(( c+1 ))
	done
fi


if [ "$testnumber" -eq "1" ]
then
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.4
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.5
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.6
		c=$(( c+1 ))
	done
	c=1
	while [ "$c" -le "500" ]
	do
		echo "RUN $c"
		python3 simulator_drone.py $algorithm 125 0.7
		c=$(( c+1 ))
	done
fi
