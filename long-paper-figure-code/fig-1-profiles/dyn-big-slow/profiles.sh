#!/bin/bash
# Example submission script for 'hello world' program
# Nodes have 40 cores

#SBATCH --partition=defq
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --mem=2g
#SBATCH --time=80:00:00

#below use Linux commands, which will run on compute node

echo "Running on `hostname`"


../spinchain/target/release/sc -P
cd ${SLURM_SUBMIT_DIR}
echo "Finished job now"


