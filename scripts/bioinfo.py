#!/usr/bin/env python

# Author: Varsheni <varshenivijay18@gmail.com>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.3"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = {'A', 'T', 'C','G','N'}  
RNA_bases = {'A', 'U', 'C','G','N'}  

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    return ord(letter)-33

def qual_score(phred_score: str) -> float:
    """takes the original, unmodified phred_score string as
    a parameter. This function should calculate the average
    quality score of the whole phred string.
    sum_of_phred gives us the whole sum of every phred score,
    and index_sum gives us the total number of phred scores in the sequence"""
    sum_of_phred=0
    index_sum=0
    for index, score in enumerate(phred_score):
        sum_of_phred+=convert_phred(score)
        index_sum+=1
    return sum_of_phred/index_sum 

def validate_base_seq(seq: str, RNAflag: bool=False)-> bool:
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    
    seq = seq.upper()    
    seq = set(seq)        
    if RNAflag:                       
        return set.issubset(seq,RNA_bases) 
                                        
    else:
        return set.issubset(seq,DNA_bases)    

def gc_content(DNA):
    '''Returns GC content of a DNA sequence as a decimal between 0 and 1.'''
    assert validate_base_seq(DNA), "String contains invalid characters - are you sure you used a DNA sequence?"
    DNA = DNA.upper()
    return (DNA.count("G")+DNA.count("C"))/len(DNA)

def calc_median(lst: list) -> float:
     '''Given a sorted list, returns the median value of the list'''
     if len(lst)%2==1:
        median=lst[len(lst)//2]
     else:
        median=(lst[int(len(lst)/2)]+lst[int(len(lst)/2-1)])/2
     return median

def oneline_fasta(file_input,first_output):
    '''makes a multi-line sequence fasta file a single sequence line fasta file'''
    first_line=True
    with open(first_output,"w") as op: ##to get the files on a single line
        with open(file_input,"r") as file:
    
            for line in file:
                line=line.strip('\n')
                if line.startswith(">"):
                    if first_line==True:
                        op.writelines([line,'\n'])
                        first_line=False
                    else:
                        op.writelines(['\n',line,'\n'])
                else:
                    op.writelines(line)



if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    # These tests are run when you execute this file directly (instead of importing it)
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    assert convert_phred("6") == 21, "wrong phred score for '6'"
    assert convert_phred("+") == 10, "wrong phred score for '+'"

    print("Your convert_phred function is working! Nice job")
    
    #qual_score
    assert qual_score("A") == 32.0, "wrong average phred score for 'A'"
    assert qual_score("AC") == 33.0, "wrong average phred score for 'AC'"
    assert qual_score("@@##") == 16.5, "wrong average phred score for '@@##'"
    assert qual_score("EEEEAAA!") == 30.0, "wrong average phred score for 'EEEEAAA!'"
    assert qual_score("$") == 3.0, "wrong average phred score for '$'"
    assert qual_score("(>.<)") == 16.8, "wrong average phred score for '(>.<)'"
    assert qual_score("BADDIE") == 211/6, "wrong average phred score for 'BADDIE'"

    print("Your qual_score function is working! Nice job")

    #calc_median
    assert calc_median([1,2,3]) == 2, "wrong median for [1,2,3]"
    assert calc_median([5,6,7,8]) == 6.5, "wrong median for [5,6,7,8]"
    assert calc_median([1,1,1,1,1,1,1,1,100]) == 1, "wrong median for [1,1,1,1,1,1,1,1,100]"
    assert calc_median([7]) == 7, "wrong median for [7]"
    assert calc_median([50,100]) == 75, "wrong median for [50,100]"
    assert calc_median([1,2,3,4,5,6,7,8,9]) == 5, "wrong median for [1,2,3,4,5,6,7,8,9]"
    assert calc_median([11,12,13,14]) == 12.5, "wrong median for [11,12,13,14]"
    print("Your calc_median function is working! Nice job")
 
    #test_gc_content
    assert gc_content("GCGCGC") == 1, "test_gc_content failed on the string 'GCGCGC'"
    assert gc_content("AATTATA") == 0, "test_gc_content failed on the string 'AATTATA'"
    assert gc_content("GCATCGAT") == 0.5,"test_gc_content failed on the string 'GCATCGAT'"
    assert gc_content("CATATATATA") == 0.1,"test_gc_content failed on the string 'CATATATATA'"
    

    print("Your test_gc_content function is working! Nice job")


    #test validate base
    assert validate_base_seq("AATAGAT"), "Validate base seq does not work on DNA"
    assert validate_base_seq("AAUAGAU", True), "Validate base seq does not work on RNA"
    assert validate_base_seq("R is the best!")==False, "Why is a string reading as a sequence?"
    assert validate_base_seq("aatagat"), "Validate base seq does not work on lowercase DNA"
    assert validate_base_seq("aauagau", True), "Validate base seq does not work on lowercase RNA"
    assert validate_base_seq("My name is Varsheni!!",True)==False, "Why is a string reading as a sequence?"

    print("Your validate_base_seq function is working! Nice job")

    