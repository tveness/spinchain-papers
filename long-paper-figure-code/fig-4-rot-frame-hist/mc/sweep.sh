#!/usr/bin/bash

#for ed in {-0.3,-0.31,-0.32,-0.33,-0.34,-0.35,-0.36,-0.37,-0.38,-0.39,-0.40,-0.41,-0.42,-0.43,-0.44,-0.45,-0.46,-0.47,-0.48,-0.49,-0.50,-0.51,-0.52,-0.53}
#for ed in {-0.345,-0.346,-0.347,-0.348,-0.349,-0.351,-0.352,-0.353,-0.354,-0.355}
#for ed in {-0.09,-0.08,-0.07,-0.06,-0.05,-0.12,-0.13,-0.14,-0.16,-0.17,-0.18,-0.19}
for ed in {-0.113,-0.107}
do
	sed -i "s/^ednsty.*/ednsty = $ed/" config.toml 
#	cat config.toml
	sc -m
	mv mc_live.dat mc_live-e$ed.dat
	
done