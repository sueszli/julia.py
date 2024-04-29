#! /bin/bash
  
# you will not have to change the SBATCH parameters
#SBATCH -p q_student
#SBATCH -N 1
#SBATCH -c 32
#SBATCH --cpu-freq=High
#SBATCH --time=5:00

# uncomment parameters accordingly

# Exercise 2.2
NPROCS=(1 2 4 8 16 24 32)
SIZE=(155 1100)
PATCH=(26)
BENCHMARK_SET=1      # c_b
OUTFILE="output_exp22_1_${SLURM_JOB_ID}.dat"
# BENCHMARK_SET=0    # c_s
# OUTFILE="output_exp22_2_${SLURM_JOB_ID}.dat"

# Exercise 2.3
# NPROCS=(32)
# SIZE=(950)
# PATCH=(1 5 10 20 55 150 400)
# BENCHMARK_SET=0    # c_s
# OUTFILE="output_exp23_${SLURM_JOB_ID}.dat"

# Exercise 2.4
# NPROCS=(16)
# SIZE=(800)
# PATCH=({1..30})
# BENCHMARK_SET=0    # c_s
# OUTFILE="output_exp24_${SLURM_JOB_ID}.dat"

NREP=3
BINARY="python3 ./julia_par.py"


# remove old output data
echo -n "" > "${OUTFILE}"

for nprocs in "${NPROCS[@]}"
do
   for size in "${SIZE[@]}"
   do
      for patch in "${PATCH[@]}"
      do
         for r in `seq 1 ${NREP}`
         do
            if ((BENCHMARK_SET)); then
               echo "${BINARY} --nprocs $nprocs --size $size --patch $patch --benchmark"
               ${BINARY} --nprocs $nprocs --size $size --patch $patch --benchmark >> "${OUTFILE}"
            else 
               echo "${BINARY} --nprocs $nprocs --size $size --patch $patch"
               ${BINARY} --nprocs $nprocs --size $size --patch $patch >> "${OUTFILE}"
            fi
         done
      done
   done
done
