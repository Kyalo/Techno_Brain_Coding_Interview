#!/usr/bin/env python3


def reverse_string(s):
    '''
    Reverse the sentence s
    '''
    words = s.split()
    words = reversed(words)
    return " ".join(words)


s = str(input("Enter the string s: "))

print(reverse_string(s))