#!/usr/bin/bash
for i in {1..1000}
do
	sc
	for j in log*dat
	do
		tail -n1 $j >> dyn-samples.dat
	done
	rm log*dat


done

	
