#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 24
#SBATCH --mem=100G
#SBATCH --output=logs/star_align_19_3F_%j.out 
#SBATCH --error=logs/star_align_19_3F_%j.err

conda activate QAA

/usr/bin/time -v STAR \
--runThreadN 8 \
--runMode alignReads --outFilterMultimapNmax 3 \
--outSAMunmapped Within KeepPairs \
--alignIntronMax 1000000 --alignMatesGapMax 1000000 \
--readFilesCommand zcat \
--readFilesIn /home/varsheni/bgmp/bioinfo/Bi623/QAA/trimmomatic_output/19_3F_fox_paired_R1.fastq.gz \
/home/varsheni/bgmp/bioinfo/Bi623/QAA/trimmomatic_output/19_3F_fox_paired_R2.fastq.gz \
--genomeDir /home/varsheni/bgmp/bioinfo/Bi623/QAA/Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b \
--outFileNamePrefix 19_3F_fox

exit