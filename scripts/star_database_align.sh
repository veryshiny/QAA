#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 24
#SBATCH --mem=100G
#SBATCH --output=logs/star_%j.out 
#SBATCH --error=logs/star_%j.err

conda activate QAA

/usr/bin/time -v STAR --runThreadN 8 --runMode genomeGenerate --genomeDir /home/varsheni/bgmp/bioinfo/Bi623/QAA/Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b --genomeFastaFiles /home/varsheni/bgmp/bioinfo/Bi623/QAA/mouse_fasta/Mus_musculus.GRCm39.dna.primary_assembly.fa --sjdbGTFfile /home/varsheni/bgmp/bioinfo/Bi623/QAA/mouse_fasta/Mus_musculus.GRCm39.112.gtf


exit

