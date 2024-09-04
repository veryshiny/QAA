#!/usr/bin/env python
import numpy
from matplotlib import pyplot as plt
import gzip
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="to create a paired histogram of trimmed read lengths from fastq files R1 and R2")
    parser.add_argument("-r1", "--inputfileR1", help="input_file_R1", type= str)
    parser.add_argument("-r2", "--inputfileR2", help="input_file_R2", type= str)
    parser.add_argument("-l", "--readlength", help="length of read", type= str)
    parser.add_argument("-o", "--output", help="picture output", type= str)
    return parser.parse_args()

args = get_args()

input_file_r1= args.inputfileR1 #"7_2E_fox_paired_R1.fastq.gz"
input_file_r2= args.inputfileR2#"7_2E_fox_paired_R2.fastq.gz"
read_length= args.readlength#101
output_fig_title=args.output#"7_2E_trimmed_read_distribution_hist.png"

def read_length_distribution(file):

    '''reads in 2 fastq files and puts the lengths of all the sequences into a list'''
    list_read_lengths=[]
    i=0
    with gzip.open(file,'rt') as fh:
        for line in fh:
            i+=1
            if i%4==2:
                line=line.strip('\n')
                #if len(line) != 101:
                list_read_lengths.append(len(line))
    return list_read_lengths

R1_list=read_length_distribution(input_file_r1)
R2_list=read_length_distribution(input_file_r2)

fig = plt.figure()
plt.style.use('seaborn-v0_8-poster')
bins=66
plt.hist([R1_list, R2_list], bins, label=['R1', 'R2'],color=["lightcoral","cornflowerblue"],edgecolor="black")
plt.legend(loc='upper left')
plt.xlabel("Length of read (in bp)")
plt.ylabel("Number of reads")
plt.yscale("log")
title=f'{output_fig_title.split("_trimmed")[0]}'
plt.title(f'Distribution of Read lengths for {title}')
fig.set_size_inches(12, 12, forward=True)
plt.savefig(output_fig_title,dpi=fig.dpi)

