#!/usr/bin/bash
sc
for i in log*
do
tail -n 8000 $i >> dyn.dat
done
rm log*dat
