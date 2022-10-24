# Author: Maurice Kyalo
# Filename: qustion3_reversed.py

#!/usr/bin/bash
# Returns a string of words in reverse order concatenated by a single space


def reverse_string(sentence):
    words = sentence.split()
    words = list(reversed(words))
    return " ".join(words)

s = input("Enter the string s: ")
s_reversed = reverse_string(s)
print(s_reversed)