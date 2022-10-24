#!/usr/bin/env python3
# Author: Maurice Kyalo
# Filename: question1_fibonacci.py


def index_fibonacci(num):
    '''
    Displays the Fibonacci number at the n-th term
    '''
    while num > 0:
        # first two terms
        sequence = [0, 1]

        while len(sequence) <= num:
            next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
            sequence.append(next_value)
        return sequence[num - 1]


position = int(input("Enter the number: "))

while position < 0:
    position = int(input("Please enter a positive number: "))

print(f'{index_fibonacci(position)} is at position {position} of the fibonacci sequence')
