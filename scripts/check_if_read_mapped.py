#!/usr/bin/env python

import argparse


def get_args():
    parser = argparse.ArgumentParser(description="to check if the reads are mapped")
    parser.add_argument("-f", "--inputfile", help="input file in the format dnaAligned.out.sam", type= str)

    return parser.parse_args()

args = get_args()

file = args.inputfile

mapped_reads=0
unmapped_reads=0
with open(file,'r') as ip:
    for line in ip:
        if line.startswith("@"):
            continue
        flag=int(line.split('\t')[1])
        if ((flag & 256) != 256):       
            if ((flag & 4) != 4):
                
                mapped_reads+=1
            else:
                unmapped_reads+=1

print(f'Number of mapped reads\t{mapped_reads}\nNumber of unmapped reads\t{unmapped_reads}')
