#!/usr/bin/bash
# Author: Maurice Kyalo
# Filename: question3_reversed.py


def reverse_string(sentence):
    '''
    Returns a string of words in reverse order concatenated by a single space
    '''
    words = sentence.split()
    words = list(reversed(words))
    return " ".join(words)

s = input("Enter the string s: ")
s_reversed = reverse_string(s)
print(s_reversed)