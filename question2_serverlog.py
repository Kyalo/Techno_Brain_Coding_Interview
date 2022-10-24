#!/usr/bin/env python3
# Author: Maurice Kyalo
# Filename: question3_serverlog.py

import re


def get_ips():
    '''
    Returns the 10 IP addresses that accesed the server the most

    '''

    # opening and reading the file
    with open('serverlog.txt') as fh:
        string = fh.readlines()
    # pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    
    # initializing the list objects
    ips =[]
    
    # extracting the IP addresses
    for line in string:
        line = line.split(',')
        line = line[len(line) - 1].strip()
        result = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", line)

        # valid IP addresses
        if result:
            ips.append(line)

    # list of unique ips
    new_ips = []
    for ip in ips:
        if ip not in new_ips:
            new_ips.append(ip)

    # create dict of ip address and frequency of occurence
    ip_dict = {}
    for ip in new_ips:
        indices = [i for i, x in enumerate(ips) if x == ip]
        ip_dict[ip] = len(indices)

    # sort the dictionary of ip addresses and the frequency of occurence
    ip_dict = dict(sorted(ip_dict.items(), key=lambda item: item[1]))

    # return the ips in descending order of frequency
    ips = [x for x in list(ip_dict)[::-1]]
    return ips
        

print(get_ips())