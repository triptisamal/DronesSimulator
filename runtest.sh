#!/bin/sh


echo "Choose what test scenario (1/0)"
echo "0. Effect of increase in number of nodes"
echo "1. Effect of increase in eccentricity"
echo "2. Check mobility"
echo "3. Check petal vs flooding"
echo "4. Static"
echo "5. Packet copies"
echo "6. Density"
echo "7. Cylinder petal"
read testnumber

if [ "$testnumber" -eq "7" ]
then
	echo "TEST NUMBER IS 7"

	##Static
	echo '0' > velocity_for_all

	echo "Choose experiment: 1 2 3"
	read exp


	c=1
	while [ "$c" -le "10" ]
	do
		if [ "$exp" -eq "2" ]
		then
			python3 simulator_drone.py 1 125 0.1 0 0 0 $c 0 1 $exp >out_$c #experiment2
		elif [ "$exp" -eq "3" ] 
		then
			python3 simulator_drone.py 1 125 0.1 1 0 0 $c 0 1 $exp >out_$c #experiment3 
		else
			python3 simulator_drone.py 1 125 0.1 0 0 0 $c 1 1 $exp >out_$c #experiment1
		fi
		#python3 simulator_drone.py petal numderofnodes ecc lattice singlezone nodesstatic itr sd_random cylinder 
		#python3 simulator_drone.py argv1 argv2 argv3 argv4 argv5 argv6 $c argv8 argv9 >out_$c
		c=$(( c+1 ))
	done

#	mv network_*.txt density/
#	mv *.c density/
#	mv out_* density/
fi

if [ "$testnumber" -eq "6" ]
then
	echo "TEST NUMBER IS 6"

	##Static
	echo '0' > velocity_for_all
	c=1
	while [ "$c" -le "1" ]
	do
		python3 simulator_drone.py 1 512 0.1 0 0 0 $c 0 
		#python3 simulator_drone.py petal numderofnodes ecc lattice singlezone nodesstatic itr sd_random 
		#python3 simulator_drone.py 1 512 0.4 1 0 0 $c 0 1 >out_$c
		#python3 simulator_drone.py argv1 argv2 argv3 argv4 argv5 argv6 $c argv8 argv9 >out_$c
		c=$(( c+1 ))
	done

#	mv network_*.txt density/
#	mv *.c density/
#	mv out_* density/
fi
#read mobility
if [ "$testnumber" -eq "5" ]
then
	echo "TEST NUMBER IS 5"

	##Static
	echo '0' > velocity_for_all
	c=1
	while [ "$c" -le "650" ]
	do
		python3 simulator_drone.py 1 343 0.4 1 1 0 $c 1
		c=$(( c+1 ))
	done

	mv *.txt testcase5/0
	mv *.c testcase5/0

	echo '2' > velocity_for_all

	c=1
	while [ "$c" -le "650" ]
	do
		python3 simulator_drone.py 1 343 0.4 1 1 1 $c 1
		c=$(( c+1 ))
	done

	mv *.txt testcase5/2
	mv *.c testcase5/2

	echo '4' > velocity_for_all

	c=1
	while [ "$c" -le "650" ]
	do
		python3 simulator_drone.py 1 343 0.4 1 1 1 $c 1
		c=$(( c+1 ))
	done

	mv *.txt testcase5/4
	mv *.c testcase5/4


	echo '6' > velocity_for_all
	c=1
	while [ "$c" -le "650" ]
	do
		python3 simulator_drone.py 1 343 0.4 1 1 1 $c 1
		c=$(( c+1 ))
	done

	mv *.txt testcase5/6
	mv *.c testcase5/6


	echo '8' > velocity_for_all
	c=1
	while [ "$c" -le "650" ]
	do
		python3 simulator_drone.py 1 343 0.4 1 1 1 $c 1
		c=$(( c+1 ))
	done

	mv *.txt testcase5/8
	mv *.c testcase5/8


fi


if [ "$testnumber" -eq "4" ]
then
	echo "TEST NUMBER IS 4"
#
#	c=1
#	while [ "$c" -le "10" ]
#	do
#		python3 simulator_drone.py 1 27 0.4 1 1 0 $c 2 
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase4/petal27
#	mv *.c testcase4/petal27
	
#       c=1
#       while [ "$c" -le "6" ]
#       do
#       	python3 simulator_drone.py 1 64 0.4 1 1 0 $c 2
#       	c=$(( c+1 ))
#       done
#
#	mv *.txt testcase4/petal64
#	mv *.c testcase4/petal64
#temp change to flood
	c=1
	while [ "$c" -le "100" ]
	do
		python3 simulator_drone.py 1 125 0.4 1 1 0 $c 2
		c=$(( c+1 ))
	done
#	mv *.txt testcase4/petal125
#	mv *.c testcase4/petal125

#
#	c=1
#	while [ "$c" -le "20" ]
#	do
#		python3 simulator_drone.py 1 216 0.4 1 1 0 $c 2
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase4/petal216
#	mv *.c testcase4/petal216
#
#
#	c=1
#	while [ "$c" -le "20" ]
#	do
#		python3 simulator_drone.py 1 343 0.4 1 1 0 $c 2
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase4/petal343
#	mv *.c testcase4/petal343
#
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		python3 simulator_drone.py 1 512 0.4 0 1 0 $c 2 
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase4/petal512
#	mv *.c testcase4/petal512

fi

if [ "$testnumber" -eq "3" ]
then
	echo "TEST NUMBER IS 3"

##	cp sd27/*500* .
#	c=1
#	while [ "$c" -le "70" ]
#	do
#		python3 simulator_drone.py 1 27 0.4 1 1 1 $c 2 
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase3/petal27
#	mv *.c testcase3/petal27
	
	
#	cp sd27/*500* .
	c=1
	while [ "$c" -le "500" ]
	do
		python3 simulator_drone.py 0 27 0.4 1 1 1 $c 2
		c=$(( c+1 ))
	done
	mv *.txt testcase3/flood27
	mv *.c testcase3/flood27

#       cp sd64/*500* .
#       c=1
#       while [ "$c" -le "70" ]
#       do
#       	python3 simulator_drone.py 1 64 0.4 1 1 1 $c 2
#       	c=$(( c+1 ))
#       done
#
#	mv *.txt testcase3/petal64
#	mv *.c testcase3/petal64


#	cp sd64/*500* .
	c=1
	while [ "$c" -le "500" ]
	do
		python3 simulator_drone.py 0 64 0.4 1 1 1 $c 2
		c=$(( c+1 ))
	done
	mv *.txt testcase3/flood64
	mv *.c testcase3/flood64


#	cp sd125/*500* .
#	c=1
#	while [ "$c" -le "600" ]
#	do
#		python3 simulator_drone.py 1 125 0.4 1 1 1 $c 2
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase3/petal125
#	mv *.c testcase3/petal125


	cp sd125/*500* .
	c=1
	while [ "$c" -le "500" ]
	do
		python3 simulator_drone.py 0 125 0.4 1 1 1 $c 2
		c=$(( c+1 ))
	done
	mv *.txt testcase3/flood125
	mv *.c testcase3/flood125
#
#
##	cp sd216/*500* .
#	c=1
#	while [ "$c" -le "600" ]
#	do
#		python3 simulator_drone.py 1 216 0.4 1 1 1 $c 2
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase3/petal216
#	mv *.c testcase3/petal216


#	cp sd216/*500* .
	c=1
	while [ "$c" -le "500" ]
	do
		python3 simulator_drone.py 0 216 0.4 1 1 1 $c 2
		c=$(( c+1 ))
	done
	mv *.txt testcase3/flood216
	mv *.c testcase3/flood216


##	cp sd343/*500* .
#	c=1
#	while [ "$c" -le "70" ]
#	do
#	#	python3 simulator_drone.py 1 343 0.4 0 1 1 $c 0 
#		python3 simulator_drone.py 1 343 0.4 1 1 1 $c 2
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase3/petal343
#	mv *.c testcase3/petal343

#	cp sd343/*500* .
	c=1
	while [ "$c" -le "500" ]
	do
		python3 simulator_drone.py 0 343 0.4 1 1 1 $c 2
		c=$(( c+1 ))
	done
	mv *.txt testcase3/flood343
	mv *.c testcase3/flood343


#	cp sd512/*500* .
#	c=1
#	while [ "$c" -le "5" ]
#	do
#		python3 simulator_drone.py 1 512 0.4 0 1 1 0 0 >out512_$c
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase3/petal512
#	mv *.c testcase3/petal512
#
#	cp sd512/*500* .
#	c=1
#	while [ "$c" -le "5" ]
#	do
#		python3 simulator_drone.py 0 512 0.4 0 1 1 0 0
#		c=$(( c+1 ))
#	done
#	mv *.txt testcase3/flood512
#	mv *.c testcase3/flood512

fi

if [ "$testnumber" -eq "2" ]
then


	c=1
	while [ "$c" -le "30" ]
	do
		echo "RUN $c"
		#multi-zone
		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
		python3 simulator_drone.py 1 27 0.4 1 1 1 $c 1
	#	python3 simulator_drone.py 0 27 0.4 1 1 1 $c 0
		c=$(( c+1 ))
	done

	#move files
	mv petal_source.txt model1/27
	mv petal_dest.txt model1/27
	mv flood_source.txt model1/27
	mv flood_dest.txt model1/27
	mv *500* model1/27
	mv *.c model1/27

#	c=1
#	while [ "$c" -le "700" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 64 0.4 1 1 1 $c 1
#		python3 simulator_drone.py 0 64 0.4 1 1 1 $c 0
#		c=$(( c+1 ))
#	done
#
#	#move files
#	mv petal_source.txt model1/64
#	mv petal_dest.txt model1/64
#	mv flood_source.txt model1/64
#	mv flood_dest.txt model1/64
#	mv *500* model1/64
#	mv *.c model1/64
	
#	
#	c=1
#	while [ "$c" -le "700" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 125 0.4 1 1 1 $c 1
#		python3 simulator_drone.py 0 125 0.4 1 1 1 $c 0
#       	c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model1/125
#	mv petal_dest.txt model1/125
#	mv flood_source.txt model1/125
#	mv flood_dest.txt model1/125
#	mv *500* model1/125
#	mv *.c model1/125

#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 216 0.4 1 1 1 $c 1
#		python3 simulator_drone.py 0 216 0.4 1 1 1 $c 0
#		c=$(( c+1 ))
#	done
#	#move files
#	mv petal_source.txt model1/216
#	mv petal_dest.txt model1/216
#	mv flood_source.txt model1/216
#	mv flood_dest.txt model1/216
#	mv *500* model1/216
#	mv *.c model1/216
#	#mobility 2
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 64 0.4 1 1 2 $c 1
#		python3 simulator_drone.py 0 64 0.4 1 1 2 $c 0
#		c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model2/64
#	mv petal_dest.txt model2/64
#	mv flood_source.txt model2/64
#	mv flood_dest.txt model2/64
#	mv *500* model2/64
#	mv *.c model2/64
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 125 0.4 1 1 2 $c 1
#		python3 simulator_drone.py 0 125 0.4 1 1 2 $c 0
#		c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model2/125
#	mv petal_dest.txt model2/125
#	mv flood_source.txt model2/125
#	mv flood_dest.txt model2/125
#	mv *500* model2/125
#	mv *.c model2/125
#	c=1
#	while [ "$c" -le "500" ]
#	do
#	#	echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 216 0.4 1 1 2 $c 1
#		python3 simulator_drone.py 0 216 0.4 1 1 2 $c 0
#		c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model2/216
#	mv petal_dest.txt model2/216
#	mv flood_source.txt model2/216
#	mv flood_dest.txt model2/216
#	mv *500* model2/216
#	mv *.c model2/216
#	c=1
#	while [ "$c" -le "500" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 343 0.4 1 1 2 $c 1
#		python3 simulator_drone.py 0 343 0.4 1 1 2 $c 0
#		c=$(( c+1 ))
#	done
#		#move files
#	mv petal_source.txt model2/343
#	mv petal_dest.txt model2/343
#	mv flood_source.txt model2/343
#	mv flood_dest.txt model2/343
#	mv *500* model2/343
#	mv *.c model2/343
	#mobility1
#	c=1
#	while [ "$c" -le "150" ]
#	do
#		echo "RUN $c"
#		#multi-zone
#		#python3 simulator_drone.py $algorithm 64 0.4 $topology 1 $mobility $c $sd_random
#		python3 simulator_drone.py 1 343 0.4 1 1 1 $c 1
#		python3 simulator_drone.py 0 343 0.4 1 1 1 $c 0
#		c=$(( c+1 ))
#	done
#	#move files
#	mv petal_source.txt model1/343
#	mv petal_dest.txt model1/343
#	mv flood_source.txt model1/343
#	mv flood_dest.txt model1/343
#	mv *500* model1/343
#	mv *.c model1/343
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
