#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import numpy as np
import gzip
import bioinfo



def get_args():
    parser = argparse.ArgumentParser(description="to create a histogram of quality score of reads from fastq file")
    parser.add_argument("-f", "--file", help="input_file", type= str)
    parser.add_argument("-l", "--length", help="length of read", type= str)
    parser.add_argument("-o", "--output", help="picture output", type= str)
    return parser.parse_args()

args = get_args()

length= int(args.length)
filename= args.file


def init_list(lst: list, number: int, value: float) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with 101 values of 0.0.'''
    lst=number*[float(value)]
    return lst


def populate_list(file: str) -> tuple[list, int]:
    """Open the file, initialize a line counter as i, and the empty list as list_quality_score,
    go through every line in the file and for the 4th line which has the quality scores,
    divide it by every index of the string the line is made up of. now for every index, add it to the
    list of scores for the particular index"""
    list_quality_score=[]
    with gzip.open(file, 'rt') as fh:
        i=0
        list_quality_score=init_list(list_quality_score, length, 0)
        for line in fh:
            i+=1
            line = line.strip('\n')
            if i%4==0:
                for index_of_score in range(0,len(line)):
                    list_quality_score[index_of_score]=bioinfo.convert_phred(line[index_of_score])+list_quality_score[index_of_score]
    return list_quality_score, i
          
my_list, num_lines = populate_list(filename)


for base_pair_index in range(0,len(my_list)):
    my_list[base_pair_index]=my_list[base_pair_index]/(num_lines/4)

## plotting the plots, x and y are the x axis (keys) and y axis(values) from the dictionary
x= range(0,length)
y= my_list
# print(x,y)

fig = plt.figure()
plt.bar(x,y,color='crimson', edgecolor="orange", width=0.5)
# plt.yscale('log')
plt.xlabel("Position of Read")
plt.ylabel("Mean PHRED score of base-pair")
plt.title(f'Mean PHRED score values for each position of the Illumina {args.output[:-9]}')
fig.set_size_inches(15, 10, forward=True)
plt.savefig(args.output, dpi=fig.dpi)
            