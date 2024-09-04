#!/usr/bin/env python

from matplotlib import pyplot as plt
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="to plot the first position of adapter sequence")
    parser.add_argument("-f", "--inputfile", help="input_file", type= str)

    return parser.parse_args()
args = get_args()

data= args.inputfile 

dict_weehee={}

with open(data,"r") as fh:
    for line in fh:
        line=line.strip('\n')
        line=line.strip(' ')
        dict_weehee[int(line.split(' ')[1])]=int(line.split(' ')[0])


fig = plt.figure()
plt.style.use('seaborn-v0_8-poster')
plt.bar(dict_weehee.keys(),dict_weehee.values())
plt.xlabel("Position of first nucleotide of adapter")
plt.ylabel("Number of reads")
plt.title(f'Distribution of First Nucleotide position of Adapter Sequence for {data.split("/")[1].split('.txt')[0]}')
fig.set_size_inches(15, 10, forward=True)
plt.savefig(f"{data.split(".txt")[0]}_adapter_positions.png",dpi=fig.dpi)
