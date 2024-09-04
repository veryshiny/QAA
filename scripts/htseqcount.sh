#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 24
#SBATCH --mem=100G
#SBATCH --output=logs/htseq_%j.out 
#SBATCH --error=logs/htseq_%j.err

conda activate QAA

/usr/bin/time -v htseq-count --stranded=yes 7_2e_star_output_part_3/7_2E_foxAligned.out.sam mouse_fasta/Mus_musculus.GRCm39.112.gtf > 7_2E_foxAligned_stranded.genecount

/usr/bin/time -v htseq-count --stranded=reverse 7_2e_star_output_part_3/7_2E_foxAligned.out.sam mouse_fasta/Mus_musculus.GRCm39.112.gtf > 7_2E_foxAligned_reverse.genecount

/usr/bin/time -v htseq-count --stranded=yes 19_3f_star_output_part_3/19_3F_foxAligned.out.sam mouse_fasta/Mus_musculus.GRCm39.112.gtf > 19_3F_foxAligned_stranded.genecount

/usr/bin/time -v htseq-count --stranded=reverse 19_3f_star_output_part_3/19_3F_foxAligned.out.sam mouse_fasta/Mus_musculus.GRCm39.112.gtf > 19_3F_foxAligned_reverse.genecount

exit
