#!/usr/bin/bash
# Author: Maurice Kyalo
# Filename: question1_fibonacci.py


def index_fibonacci(num):
    '''
    Displays the Fibonacci number at the n-th term
    '''
    if num <= 0:
        return [0]

    # first two terms
    sequence = [0, 1]

    while len(sequence) <= num:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)
    return sequence[num - 1]


position = int(input("Enter the number: "))

print(f'{index_fibonacci(position)} is at position {position} of the fibonacci sequence')
