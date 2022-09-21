#!/bin/bash
# Example submission script for 'hello world' program
# Nodes have 40 cores

#SBATCH --nodes=2
#SBATCH --ntasks-per-node=40
#SBATCH --mem=2g
#SBATCH --time=168:00:00

#below use Linux commands, which will run on compute node

sc -P
	


echo "Running on `hostname`"

cd ${SLURM_SUBMIT_DIR}


echo "Finished job now"


