#!env python

"""
Python script to count the number of aminoacids per sequence in a FASTA file
Call it like so: 
    python fasta_length.py sequences.fasta
"""

import sys

sequence_length = 0
fasta_sequence_lengths = []

# Getting the filename from the list of arguments
fasta_filename = sys.argv[1]

# Opening the file:
fastafile = open(fasta_filename, 'r')

# Iterating over all lines in the file:
for line in fastafile.readlines():
    if line.startswith('>'):
        if sequence_length:
            fasta_sequence_lengths.append(sequence_length)
        sequence_length = 0
    else:
        sequence_length += len(line.strip())
fasta_sequence_lengths.append(sequence_length)

# Closing the file:
fastafile.close()

print(max(fasta_sequence_lengths))

def evaluate(input):
"""
calculates and print the maximum length as well as the minimum length of the files in the .fasta file,
also prints all lengths in a sorted way.
Takes the fasta_sequence_length as input.
Call for example evaluate(fasta_sequence_lengths)
"""
    print("The maximum is {} and the minimum is {}.".format(max(input), min(input)))
    print("The sorted List is {}.".format(sorted(input)))

evaluate(fasta_sequence_lengths)
