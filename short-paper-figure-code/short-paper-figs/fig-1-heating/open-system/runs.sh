#!/usr/bin/bash

for tau in {0.1,0.5,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.5,5.0,6.0,7.0,8.0,9.0,10.0,12.0,14.0}
do
   for j in {1..9}
   do
      cd t-$tau
      sc
      sc -a
      rm log*
      cd ..
   done
done