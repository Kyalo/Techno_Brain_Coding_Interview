#!/usr/bin/bash
# Author: Maurice Kyalo
# Filename: question3_reverse.py


def reverse_string(s){
    '''
    Reverse the order of the words of a string
    '''
    return s.split().reverse()
}

s = str(input("Enter the string s: "))

reversed_string = reverse_string(s)
print(reversed_string)