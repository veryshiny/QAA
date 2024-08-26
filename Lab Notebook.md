# Lab Notebook :rose: :heart: :rainbow:

# Part 1 

## Create a new conda environment called `QAA` and install `FastQC`. 

```bash
$conda create --name QAA
$conda activate QAA 
$conda install FastQC
$fastqc --version                                                 
    FastQC v0.12.1                
```

## Files I've been assigned and their file paths

```bash
Varsheni        19_3F_fox_S14_L008      7_2E_fox_S6_L008
```

**File paths:**

`/projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz`

`/projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R2_001.fastq.gz`

`/projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz`

`/projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz`

## Initial data exploration

### Number of lines

```bash
zcat /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz | wc -l

zcat /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R2_001.fastq.gz | wc -l
65393020

```
number of lines for this file = 65393020

```bash 
zcat /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz | wc -l

zcat /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz | wc -l
```
number of lines for this file = 21113700

### number of duplicate sequences


```bash
zcat /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz | sed -n '2~4p' | sort | uniq -c | sort -nr |
 head
   2348 CTTTTACTTCCTCTAGATAGTCAAGTTCGACCGTCTTCTCAGCGCTCCGCCAGGGCCGTGGGCCGACCCCGGCGGGGCCGATCCGAGGGCCTCACTAAACC
   1880 CTCGTTTGAATATTTGCTACTACCACCAAGATCTGCACCTGCGGCGGCTCCACCCGGGCCCGCGCCCTAGGCTTCAAGGCTCACCGCAGCGGCCCTCCTAC
   1519 CCCGGCCGTCCCTCTTAATCATGGCCTCAGTTCCGAAAACCAACAAAATAGAACCGCGGTCCTATTCCATTATTCCTAGCTGCGGTATCCAGGCGGCTCGG
   1472 CTCGTTCATGGGGAATAATTGCAATCCCCGATCCCCATCACGAATGGGGTTCAACGGGTTACCCGCGCCTGCCGGCGTAGGGTAGGCACACGCTGAGCCAG
   1417 ACGACTTTTACTTCCTCTAGATAGTCAAGTTCGACCGTCTTCTCAGCGCTCCGCCAGGGCCGTGGGCCGACCCCGGCGGGGCCGATCCGAGGGCCTCACTA
   1351 CTCCTACTCGTCGCGGCGTAGCGTCCGCGGGGCCCGACGCCGCGGGGGCGAAACCCGGCGCGCGGAGGGGAGGCGGGGGACGGGCCCCCGCCACGCACCCC
   1306 CGACTTTTACTTCCTCTAGATAGTCAAGTTCGACCGTCTTCTCAGCGCTCCGCCAGGGCCGTGGGCCGACCCCGGCGGGGCCGATCCGAGGGCCTCACTAA
   1261 GGCAGACGTTCGAATGGGTCGTCGCCGCCACGGGGGGCGTGCGATCGGCCCGAGGTTATCTAGAGTCACCAAAGCCGCCGGCGCCCGACCCCCGGCCGGAG
   1235 CTTGATTAATGAAAACATTCTTGGCAAATGCTTTCGCTCTGGTCCGTCTTGCGCCGGTCCAAGAATTTCACCTCTAGCGGCGCAATACGAATGCCCCCGGC
   1209 CCCCAGTCAAACTCCCCACCTGGCACTGTCCCCGGAGCGGGTCGCGCCCGCCCGCACGCGCGGGACGGACGCTTGGCGCCAGAAGCGAGAGCCCCTCGGGG

```

### Length of sequences 

```bash 
 zcat /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz | sed -n '2~4p' | head -100000 | awk '{print length}' | uniq  
101
```

## Fastqc Command

```bash
fastqc -o output/ -t 8 /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R2_001.fastq.gz
```

# Part 2


## Packages to install

installed `cutadapt` and `Trimmomatic` in QAA environment

```bash 

conda install cutadapt
conda install Trimmomatic

```

```bash

$cutadapt --version
4.9

$trimmomatic -version
0.39
```
 
## Adapter sequence finding

### IDT for Illumina TruSeq DNA and RNA UD Indexes
These unique dual (UD) index adapters are arranged in the plate to enforce the recommended pairing
strategy.

`https://knowledge.illumina.com/library-preparation/general/library-preparation-general-reference_material-list/000001314`

#### Adapter Trimming
The following sequences are used for adapter trimming.

```bash
Read 1
AGATCGGAAGAGCACACGTCTGAACTCCAGTCA
Read 2
AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT
```
## Command for cutadapt

the -j 0 helps automatically detect and use all the cores available

```bash

/usr/bin/time -v cutadapt  -j 0  -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT  -o 19_3F_fox_trimmed.R1.fastq.gz -p 19_3F_fox_trimmed.R2.fastq.gz  /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R2_001.fastq.gz

/usr/bin/time -v cutadapt  -j 0  -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT  -o 7_2E_fox_trimmed.R1.fastq.gz -p 7_2E_fox_trimmed.R2.fastq.gz  /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz
```

## Time taken for cutadapt (very fast)

19_3F_fox

```bash 
        Command being timed: "cutadapt -j 0 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o 19_3F_fox_trimmed.R1.fastq.gz -p 19_3F_fox_trimmed.R2.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/19_3F_fox_S14_L008_R2_001.fastq.gz"
        User time (seconds): 237.36
        System time (seconds): 17.59
        Percent of CPU this job got: 710%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:35.90
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 124496
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 3770964
        Voluntary context switches: 559560
        Involuntary context switches: 5857
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
```
7_2E_fox

```bash
Command being timed: "cutadapt -j 0 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o 7_2E_fox_trimmed.R1.fastq.gz -p 7_2E_fox_trimmed.R2.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz"
        User time (seconds): 78.67
        System time (seconds): 5.91
        Percent of CPU this job got: 718%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:11.77
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 124820
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 1404159
        Voluntary context switches: 180701
        Involuntary context switches: 2254
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
```

## Output for cutadapt

**19_3F_fox**

```bash
=== Summary ===

Total read pairs processed:         16,348,255
  Read 1 with adapter:                 546,623 (3.3%)
  Read 2 with adapter:                 676,564 (4.1%)
Pairs written (passing filters):    16,348,255 (100.0%)

Total basepairs processed: 3,302,347,510 bp
  Read 1: 1,651,173,755 bp
  Read 2: 1,651,173,755 bp
Total written (filtered):  3,294,067,204 bp (99.7%)
  Read 1: 1,647,303,006 bp
  Read 2: 1,646,764,198 bp

=== First read: Adapter 1 ===

Sequence: AGATCGGAAGAGCACACGTCTGAACTCCAGTCA; Type: regular 3'; Length: 33; Trimmed: 546623 times

Minimum overlap: 3
No. of allowed errors:
1-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-33 bp: 3

Bases preceding removed adapters:
  A: 23.6%
  C: 30.4%
  G: 28.3%
  T: 17.7%
  none/other: 0.1%

Overview of removed sequences
length  count   expect  max.err error counts
3       302874  255441.5        0       302874
4       70131   63860.4 0       70131
5       26599   15965.1 0       26599
6       13011   3991.3  0       13011
7       11300   997.8   0       11300
8       9710    249.5   0       9710
9       9128    62.4    0       8806 322
10      8257    15.6    1       7780 477
11      7592    3.9     1       7285 307
12      6944    1.0     1       6711 233
13      6330    0.2     1       6120 210
14      5898    0.1     1       5694 204
15      5598    0.0     1       5423 175
16      5315    0.0     1       5111 204
17      4834    0.0     1       4649 185
18      4368    0.0     1       4163 198 7
19      3993    0.0     1       3819 172 2
20      3517    0.0     2       3368 130 19
21      3227    0.0     2       3045 164 18
22      3058    0.0     2       2900 135 23
23      2725    0.0     2       2595 116 14
24      2508    0.0     2       2373 123 12
25      2388    0.0     2       2252 117 19
26      2215    0.0     2       2052 141 22
27      2012    0.0     2       1888 110 14
28      1935    0.0     2       1818 101 15 1
29      1720    0.0     2       1613 93 14
30      1562    0.0     3       1475 74 9 4
31      1371    0.0     3       1266 81 12 12
32      1290    0.0     3       1201 61 20 8
33      1200    0.0     3       1103 73 16 8
34      1073    0.0     3       999 62 4 8
35      1010    0.0     3       941 56 9 4
36      1003    0.0     3       939 53 10 1
37      939     0.0     3       873 52 9 5
38      869     0.0     3       822 35 6 6
39      842     0.0     3       773 54 9 6
40      706     0.0     3       651 42 7 6
41      620     0.0     3       576 31 9 4
42      524     0.0     3       490 23 9 2
43      499     0.0     3       458 32 4 5
44      455     0.0     3       418 25 9 3
45      429     0.0     3       402 23 2 2
46      396     0.0     3       372 21 3
47      417     0.0     3       386 23 6 2
48      358     0.0     3       337 18 2 1
49      364     0.0     3       342 16 5 1
50      334     0.0     3       309 21 4
51      244     0.0     3       218 23 2 1
52      261     0.0     3       240 14 3 4
53      218     0.0     3       203 13 1 1
54      213     0.0     3       193 17 1 2
55      191     0.0     3       183 6 1 1
56      174     0.0     3       161 10 2 1
57      179     0.0     3       166 10 1 2
58      142     0.0     3       128 10 1 3
59      130     0.0     3       118 11 1
60      134     0.0     3       117 14 2 1
61      104     0.0     3       94 9 1
62      102     0.0     3       92 6 2 2
63      100     0.0     3       85 10 2 3
64      77      0.0     3       71 4 2
65      60      0.0     3       55 2 0 3
66      49      0.0     3       46 2 1
67      47      0.0     3       44 2 0 1
68      38      0.0     3       32 3 2 1
69      31      0.0     3       29 2
70      33      0.0     3       32 1
71      38      0.0     3       32 3 2 1
72      20      0.0     3       16 3 0 1
73      19      0.0     3       17 2
74      14      0.0     3       11 3
75      26      0.0     3       20 3 3
76      20      0.0     3       18 2
77      15      0.0     3       12 2 1
78      16      0.0     3       13 1 1 1
79      11      0.0     3       11
80      4       0.0     3       4
81      10      0.0     3       8 2
82      14      0.0     3       12 2
83      27      0.0     3       27
84      14      0.0     3       13 1
85      14      0.0     3       12 1 1
86      2       0.0     3       2
87      16      0.0     3       16
88      4       0.0     3       3 0 1
89      17      0.0     3       17
90      3       0.0     3       3
91      10      0.0     3       8 1 0 1
92      4       0.0     3       3 1
93      9       0.0     3       6 3
94      3       0.0     3       3
95      8       0.0     3       7 0 1
96      7       0.0     3       7
97      4       0.0     3       4
98      4       0.0     3       2 1 1
99      3       0.0     3       2 0 1
100     1       0.0     3       1
101     291     0.0     3       7 206 73 5


=== Second read: Adapter 2 ===

Sequence: AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT; Type: regular 3'; Length: 33; Trimmed: 676564 times

Minimum overlap: 3
No. of allowed errors:
1-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-33 bp: 3

Bases preceding removed adapters:
  A: 26.9%
  C: 31.8%
  G: 29.2%
  T: 12.1%
  none/other: 0.0%

Overview of removed sequences
length  count   expect  max.err error counts
3       400345  255441.5        0       400345
4       93132   63860.4 0       93132
5       30163   15965.1 0       30163
6       14397   3991.3  0       14397
7       11515   997.8   0       11515
8       9864    249.5   0       9864
9       9482    62.4    0       8954 528
10      8645    15.6    1       7910 735
11      7915    3.9     1       7391 524
12      7117    1.0     1       6820 297
13      6429    0.2     1       6238 191
14      5982    0.1     1       5828 154
15      5674    0.0     1       5494 180
16      5387    0.0     1       5223 164
17      4905    0.0     1       4760 145
18      4418    0.0     1       4217 200 1
19      4044    0.0     1       3900 143 1
20      3576    0.0     2       3412 128 36
21      3291    0.0     2       3148 125 18
22      3109    0.0     2       2976 109 24
23      2798    0.0     2       2681 88 29
24      2565    0.0     2       2420 122 23
25      2443    0.0     2       2275 138 30
26      2261    0.0     2       2107 131 23
27      2059    0.0     2       1940 97 21 1
28      1992    0.0     2       1855 112 25
29      1769    0.0     2       1649 103 16 1
30      1613    0.0     3       1503 79 15 16
31      1424    0.0     3       1303 85 24 12
32      1333    0.0     3       1231 83 15 4
33      1263    0.0     3       1166 66 20 11
34      1134    0.0     3       1053 53 14 14
35      1048    0.0     3       967 56 16 9
36      1051    0.0     3       973 52 15 11
37      977     0.0     3       901 61 13 2
38      921     0.0     3       856 39 14 12
39      890     0.0     3       814 55 16 5
40      762     0.0     3       695 41 12 14
41      662     0.0     3       597 45 11 9
42      570     0.0     3       514 33 17 6
43      542     0.0     3       487 37 9 9
44      498     0.0     3       446 32 15 5
45      485     0.0     3       429 35 9 12
46      453     0.0     3       402 34 5 12
47      474     0.0     3       422 32 5 15
48      399     0.0     3       358 30 6 5
49      411     0.0     3       369 29 9 4
50      382     0.0     3       329 27 10 16
51      295     0.0     3       245 27 15 8
52      306     0.0     3       256 25 8 17
53      254     0.0     3       212 26 7 9
54      258     0.0     3       210 23 16 9
55      236     0.0     3       195 20 14 7
56      211     0.0     3       176 24 6 5
57      210     0.0     3       178 22 4 6
58      181     0.0     3       153 15 8 5
59      148     0.0     3       125 14 7 2
60      166     0.0     3       141 12 4 9
61      137     0.0     3       108 17 9 3
62      128     0.0     3       101 16 6 5
63      129     0.0     3       104 11 8 6
64      106     0.0     3       81 12 6 7
65      90      0.0     3       67 9 8 6
66      72      0.0     3       53 6 7 6
67      74      0.0     3       53 14 5 2
68      59      0.0     3       45 6 5 3
69      58      0.0     3       38 9 7 4
70      68      0.0     3       49 8 4 7
71      68      0.0     3       50 8 4 6
72      44      0.0     3       31 8 4 1
73      41      0.0     3       24 11 4 2
74      36      0.0     3       22 6 5 3
75      45      0.0     3       30 7 5 3
76      38      0.0     3       25 7 1 5
77      24      0.0     3       17 3 4
78      27      0.0     3       21 3 1 2
79      27      0.0     3       16 3 3 5
80      11      0.0     3       8 0 2 1
81      18      0.0     3       12 1 2 3
82      16      0.0     3       14 2
83      30      0.0     3       25 2 2 1
84      16      0.0     3       13 2 0 1
85      17      0.0     3       12 3 0 2
86      4       0.0     3       2 1 1
87      17      0.0     3       17
88      4       0.0     3       3 1
89      17      0.0     3       15 2
90      3       0.0     3       3
91      10      0.0     3       8 1 1
92      5       0.0     3       4 0 0 1
93      9       0.0     3       5 4
94      4       0.0     3       3 0 0 1
95      9       0.0     3       8 0 1
96      8       0.0     3       7 0 0 1
97      4       0.0     3       4
98      3       0.0     3       1 2
99      4       0.0     3       3 0 1
100     2       0.0     3       0 0 1 1
101     248     0.0     3       4 202 37 5
```

**7_2E_fox**

```bash
=== Summary ===

Total read pairs processed:          5,278,425
  Read 1 with adapter:                 173,473 (3.3%)
  Read 2 with adapter:                 212,512 (4.0%)
Pairs written (passing filters):     5,278,425 (100.0%)

Total basepairs processed: 1,066,241,850 bp
  Read 1:   533,120,925 bp
  Read 2:   533,120,925 bp
Total written (filtered):  1,063,261,392 bp (99.7%)
  Read 1:   531,725,257 bp
  Read 2:   531,536,135 bp

=== First read: Adapter 1 ===

Sequence: AGATCGGAAGAGCACACGTCTGAACTCCAGTCA; Type: regular 3'; Length: 33; Trimmed: 173473 times

Minimum overlap: 3
No. of allowed errors:
1-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-33 bp: 3

Bases preceding removed adapters:
  A: 21.6%
  C: 30.3%
  G: 32.4%
  T: 15.5%
  none/other: 0.1%

Overview of removed sequences
length  count   expect  max.err error counts
3       97285   82475.4 0       97285
4       22139   20618.8 0       22139
5       7102    5154.7  0       7102
6       2604    1288.7  0       2604
7       2232    322.2   0       2232
8       2203    80.5    0       2203
9       2176    20.1    0       2067 109
10      2158    5.0     1       2016 142
11      1962    1.3     1       1862 100
12      1955    0.3     1       1874 81
13      1839    0.1     1       1774 65
14      1693    0.0     1       1624 69
15      1678    0.0     1       1635 43
16      1550    0.0     1       1481 69
17      1581    0.0     1       1515 66
18      1520    0.0     1       1436 81 3
19      1398    0.0     1       1348 47 3
20      1381    0.0     2       1319 49 13
21      1310    0.0     2       1248 54 8
22      1250    0.0     2       1170 66 14
23      1137    0.0     2       1081 47 9
24      1080    0.0     2       1023 54 3
25      1076    0.0     2       1012 54 10
26      973     0.0     2       916 50 7
27      907     0.0     2       844 58 4 1
28      875     0.0     2       821 48 6
29      826     0.0     2       782 40 4
30      739     0.0     3       687 44 4 4
31      702     0.0     3       665 26 6 5
32      625     0.0     3       573 40 6 6
33      605     0.0     3       566 31 6 2
34      547     0.0     3       513 29 5
35      511     0.0     3       475 34 1 1
36      463     0.0     3       423 34 5 1
37      419     0.0     3       390 22 5 2
38      388     0.0     3       364 15 8 1
39      409     0.0     3       384 19 5 1
40      351     0.0     3       328 19 2 2
41      320     0.0     3       287 25 5 3
42      275     0.0     3       247 23 4 1
43      284     0.0     3       265 15 1 3
44      217     0.0     3       201 12 2 2
45      200     0.0     3       186 13 1
46      177     0.0     3       165 10 2
47      188     0.0     3       171 15 2
48      143     0.0     3       131 9 1 2
49      139     0.0     3       129 8 1 1
50      134     0.0     3       126 6 1 1
51      125     0.0     3       113 11 1
52      111     0.0     3       104 4 1 2
53      97      0.0     3       89 7 1
54      86      0.0     3       79 6 1
55      97      0.0     3       88 4 2 3
56      76      0.0     3       70 5 0 1
57      64      0.0     3       59 2 1 2
58      55      0.0     3       52 2 1
59      85      0.0     3       80 4 0 1
60      57      0.0     3       52 3 2
61      62      0.0     3       59 3
62      54      0.0     3       49 3 2
63      57      0.0     3       50 6 0 1
64      46      0.0     3       42 1 2 1
65      43      0.0     3       38 3 1 1
66      38      0.0     3       35 1 1 1
67      34      0.0     3       30 1 1 2
68      38      0.0     3       34 3 0 1
69      41      0.0     3       38 2 1
70      35      0.0     3       29 5 1
71      29      0.0     3       26 3
72      14      0.0     3       12 1 1
73      30      0.0     3       28 2
74      19      0.0     3       17 1 1
75      18      0.0     3       15 2 0 1
76      16      0.0     3       10 4 2
77      9       0.0     3       7 2
78      12      0.0     3       9 1 1 1
79      9       0.0     3       7 0 0 2
80      3       0.0     3       3
81      3       0.0     3       3
82      1       0.0     3       1
84      1       0.0     3       1
85      3       0.0     3       3
87      3       0.0     3       3
88      4       0.0     3       4
89      1       0.0     3       1
91      1       0.0     3       1
92      3       0.0     3       2 1
93      1       0.0     3       1
94      1       0.0     3       1
96      1       0.0     3       1
97      1       0.0     3       1
98      2       0.0     3       2
99      2       0.0     3       2
101     259     0.0     3       6 201 47 5


=== Second read: Adapter 2 ===

Sequence: AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT; Type: regular 3'; Length: 33; Trimmed: 212512 times

Minimum overlap: 3
No. of allowed errors:
1-9 bp: 0; 10-19 bp: 1; 20-29 bp: 2; 30-33 bp: 3

Bases preceding removed adapters:
  A: 25.9%
  C: 29.0%
  G: 34.7%
  T: 10.2%
  none/other: 0.1%

Overview of removed sequences
length  count   expect  max.err error counts
3       127576  82475.4 0       127576
4       27218   20618.8 0       27218
5       7815    5154.7  0       7815
6       3257    1288.7  0       3257
7       2374    322.2   0       2374
8       2233    80.5    0       2233
9       2322    20.1    0       2107 215
10      2296    5.0     1       2043 253
11      2078    1.3     1       1911 167
12      2031    0.3     1       1933 98
13      1884    0.1     1       1831 53
14      1760    0.0     1       1699 61
15      1713    0.0     1       1639 74
16      1583    0.0     1       1514 69
17      1620    0.0     1       1552 68
18      1548    0.0     1       1483 63 2
19      1427    0.0     1       1357 69 1
20      1421    0.0     2       1336 72 13
21      1342    0.0     2       1273 60 9
22      1290    0.0     2       1220 52 18
23      1174    0.0     2       1113 51 10
24      1107    0.0     2       1029 64 14
25      1111    0.0     2       1034 61 16
26      1004    0.0     2       948 46 10
27      943     0.0     2       882 43 18
28      914     0.0     2       849 48 16 1
29      854     0.0     2       791 53 9 1
30      780     0.0     3       715 43 14 8
31      736     0.0     3       678 44 8 6
32      657     0.0     3       597 42 15 3
33      636     0.0     3       573 46 12 5
34      576     0.0     3       532 32 7 5
35      533     0.0     3       482 42 7 2
36      487     0.0     3       452 28 5 2
37      452     0.0     3       411 31 4 6
38      412     0.0     3       371 26 5 10
39      427     0.0     3       388 28 8 3
40      381     0.0     3       331 38 8 4
41      348     0.0     3       313 17 10 8
42      304     0.0     3       271 20 5 8
43      308     0.0     3       272 25 7 4
44      246     0.0     3       219 18 5 4
45      220     0.0     3       202 8 5 5
46      213     0.0     3       185 17 8 3
47      200     0.0     3       181 13 2 4
48      170     0.0     3       143 20 2 5
49      157     0.0     3       143 12 2
50      166     0.0     3       142 12 10 2
51      147     0.0     3       124 14 5 4
52      126     0.0     3       116 7 3
53      125     0.0     3       106 11 2 6
54      101     0.0     3       84 12 4 1
55      120     0.0     3       100 12 5 3
56      101     0.0     3       85 10 3 3
57      88      0.0     3       72 9 5 2
58      75      0.0     3       62 7 3 3
59      107     0.0     3       81 15 4 7
60      72      0.0     3       60 7 2 3
61      74      0.0     3       63 5 3 3
62      72      0.0     3       55 10 5 2
63      72      0.0     3       53 13 3 3
64      60      0.0     3       48 6 3 3
65      58      0.0     3       47 3 5 3
66      50      0.0     3       43 5 2
67      58      0.0     3       46 4 3 5
68      56      0.0     3       49 3 4
69      56      0.0     3       48 5 2 1
70      44      0.0     3       36 5 2 1
71      41      0.0     3       34 4 1 2
72      28      0.0     3       22 4 1 1
73      43      0.0     3       31 5 2 5
74      28      0.0     3       21 3 1 3
75      25      0.0     3       21 1 2 1
76      25      0.0     3       18 5 2
77      15      0.0     3       10 2 1 2
78      13      0.0     3       12 0 1
79      15      0.0     3       12 2 1
80      10      0.0     3       7 1 2
81      5       0.0     3       3 2
82      7       0.0     3       1 2 2 2
83      3       0.0     3       1 0 0 2
84      1       0.0     3       1
85      8       0.0     3       4 1 1 2
87      5       0.0     3       3 0 1 1
88      5       0.0     3       4 0 0 1
89      1       0.0     3       0 1
90      1       0.0     3       0 0 1
91      1       0.0     3       1
92      3       0.0     3       1 2
93      1       0.0     3       1
94      1       0.0     3       1
96      1       0.0     3       0 1
97      1       0.0     3       1
98      2       0.0     3       1 1
99      2       0.0     3       1 1
101     255     0.0     3       6 196 48 5

```

## Sanity check
Use your Unix skills to search for the adapter sequences in your datasets and confirm the expected sequence orientations. Report the commands you used, the reasoning behind them, and how you confirmed the adapter sequences.

### Commands used and why

```bash
zcat bioinfo/Bi623/QAA/7_2E_fox_trimmed.R2.fastq.gz | grep "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT" 

No output
```
reverse complement

need to check whether reverse complements play a factor 


Searching R2 for rev_comp of R1 adapter
```bash
zcat /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz | grep -c "TGACTGGAGTTCAGACGTGTGCTCTTCCGATCT" 
0
```

Searching R2 FOR rev_comp of R2

```bash
zcat /projects/bgmp/shared/2017_sequencing/demultiplexed/7_2E_fox_S6_L008_R2_001.fastq.gz | grep -c "ACACTCTTTCCCTACACGACGCTCTTCCGATCT"
0
```


```bash
 zcat 7_2E_fox_trimmed.R1.fastq.gz | wc -l
21113700
zcat 7_2E_fox_trimmed.R2.fastq.gz | wc -l
21113700
```

The line counts are the same before and after using cutadapt which makes sense.

The reads must be of different lengths then now lets double check that

```bash



zcat 7_2E_fox_trimmed.R1.fastq.gz  | sed -n '2~4p' | awk '{print length}'
 | sort -nr | uniq -c
5104952 101
  97285 98
  22139 97
   7102 96
   2604 95
   2232 94
   2203 93
   2176 92
   2158 91
   1962 90
   1955 89
   1839 88
   1693 87
   1678 86
   1550 85
   1581 84
   1520 83
   1398 82
   1381 81
   1310 80
   1250 79
   1137 78
   1080 77
   1076 76
    973 75
    907 74
    875 73
    826 72
    739 71
    702 70
    625 69
    605 68
    547 67
    511 66
    463 65
    419 64
    388 63
    409 62
    351 61
    320 60
    275 59
    284 58
    217 57
    200 56
    177 55
    188 54
    143 53
    139 52
    134 51
    125 50
    111 49
     97 48
     86 47
     97 46
     76 45
     64 44
     55 43
     85 42
     57 41
     62 40
     54 39
     57 38
     46 37
     43 36
     38 35
     34 34
     38 33
     41 32
     35 31
     29 30
     14 29
     30 28
     19 27
     18 26
     16 25
      9 24
     12 23
      9 22
      3 21
      3 20
      1 19
      1 17
      3 16
      3 14
      4 13
      1 12
      1 10
      3 9
      1 8
      1 7
      1 5
      1 4
      2 3
      2 2
    259 0

```

## Trimmomatic

  - LEADING: quality of 3
  - TRAILING: quality of 3
  - SLIDING WINDOW: window size of 5 and required quality of 15
  - MINLENGTH: 35 bases


We're using trimmomatic on the files outputted from cutadapt because the adapter sequences have been trimmed using that command. 

```bash
/usr/bin/time  -v trimmomatic PE 7_2E_fox_trimmed.R1.fastq.gz 7_2E_fox_trimmed.R2.fastq.gz 7_2E_fox_paired_R1.fastq.gz 7_2E_fox_unpaired_R1.fastq.gz 7_2E_fox_paired_R2.fastq.gz 7_2E_fox_unpaired_R2.fastq.gz  LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35
```

```bash
/usr/bin/time  -v trimmomatic PE 19_3F_fox_trimmed.R1.fastq.gz 19_3F_fox_trimmed.R2.fastq.gz 19_3F_fox_paired_R1.fastq.gz 19_3F_fox_unpaired_R1.fastq.gz 19_3F_fox_paired_R2.fastq.gz 19_3F_fox_unpaired_R2.fastq.gz  LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35
```

```bash
Multiple cores found: Using 4 threads
Quality encoding detected as phred33
Input Read Pairs: 5278425 Both Surviving: 4882703 (92.50%) Forward Only Surviving: 388376 (7.36%) Reverse Only Surviving: 3803 (0.07%) Dropped: 3543 (0.07%)
TrimmomaticPE: Completed successfully
        Command being timed: "trimmomatic PE 7_2E_fox_trimmed.R1.fastq.gz 7_2E_fox_trimmed.R2.fastq.gz 7_2E_fox_paired_R1.fastq.gz 7_2E_fox_unpaired_R1.fastq.gz 7_2E_fox_paired_R2.fastq.gz 7_2E_fox_unpaired_R2.fastq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35"
        User time (seconds): 267.14
        System time (seconds): 6.84
        Percent of CPU this job got: 217%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 2:05.91
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 399924
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 45620
        Voluntary context switches: 59638
        Involuntary context switches: 2754
        Swaps: 0
        File system inputs: 0
        File system outputs: 864
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
```

```bash
Multiple cores found: Using 4 threads
Quality encoding detected as phred33
Input Read Pairs: 16348255 Both Surviving: 15899268 (97.25%) Forward Only Surviving: 428450 (2.62%) Reverse Only Surviving: 14868 (0.09%) Dropped: 5669 (0.03%)
TrimmomaticPE: Completed successfully
        Command being timed: "trimmomatic PE 19_3F_fox_trimmed.R1.fastq.gz 19_3F_fox_trimmed.R2.fastq.gz 19_3F_fox_paired_R1.fastq.gz 19_3F_fox_unpaired_R1.fastq.gz 19_3F_fox_paired_R2.fastq.gz 19_3F_fox_unpaired_R2.fastq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35"
        User time (seconds): 815.96
        System time (seconds): 18.73
        Percent of CPU this job got: 216%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 6:24.67
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 402636
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 50495
        Voluntary context switches: 175790
        Involuntary context switches: 5189
        Swaps: 0
        File system inputs: 0
        File system outputs: 2464
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0

```

```bash
zcat 7_2E_fox_paired_R1.fastq.gz | wc -l
19530812
zcat 7_2E_fox_paired_R2.fastq.gz | wc -l
19530812
```

previously, both the original and the cutadapt output had 21113700 lines :: there's been a reduction!

## Plotting the trimmed read lengths

use conda environment bgmp_py312 to run script `read_length_distribution.py`

this script helps make 2 histograms on a single plot for R1 and R2.

Feel like putting in the untrimmed reads will skew the plot: lets do a sanity check :smiley:



commands to run

```bash
./read_length_distribution.py  -r1 7_2E_fox_paired_R1.fastq.gz -r2
7_2E_fox_paired_R2.fastq.gz -l 101 -o 7_2E_trimmed_read_distribution_hist.png

 ./read_length_distribution.py  -r1 19_3F_fox_paired_R1.fastq.gz -r
219_3F_fox_paired_R2.fastq.gz -l 101 -o 19_3F_trimmed_read_distribution_hist.png

```
