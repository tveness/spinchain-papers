#!/usr/bin/bash
for i in log*dat
do
	tail -n 9000 $i >> dyn.dat
done
